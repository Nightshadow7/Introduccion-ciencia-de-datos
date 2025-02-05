import streamlit as st
import json
import logging as lgg

lgg.basicConfig(level=lgg.DEBUG)

def obtener_mejor_procesador(procesadores, presupuesto_max):
  mejores_procesadores = []
  for marca in ["Intel", "AMD"]:
    if marca in procesadores:
      for generacion in procesadores[marca]:
        for modelo in generacion["Modelos"]:
          if modelo["Precio"] <= presupuesto_max:
            mejores_procesadores.append(modelo)
  
  if not mejores_procesadores:
    return None
  
  return max(mejores_procesadores, 
    key=lambda x: x["Nucleos"] * 2 + x["Hilos"] + float(x["FrecuenciaTurbo"].split()[0]) * 10)

def obtener_mejor_caja(cajas, presupuesto_max):
  todas_cajas = [c for categoria in cajas.values() for c in categoria]
  cajas_validas = [c for c in todas_cajas if c["Precio"] <= presupuesto_max]
  if not cajas_validas:
    return None
  
  return max(cajas_validas, 
    key=lambda x: x["Precio"] / 10 + len(x["VentiladoresIncluidos"] if isinstance(x["VentiladoresIncluidos"], list) else [x["VentiladoresIncluidos"]]) * 5)

with open("BaseProyecto.json", "r") as file:
  data = json.load(file)

class CalculadoraPuntajes:
  def __init__(self):
    self.tipo_peso_almacenamiento = {"SSD NVMe": 3, "SSD SATA": 2, "HDD": 1}
    self.certificacion_peso_fuente = {"80+ Gold": 3, "80+ Silver": 2, "80+ Bronze": 1}
    self.chipset_peso_placa = {"Z790": 3, "X670E": 3, "B650": 2, "H610": 1}
    self.ram_peso_placa = {"DDR5": 2, "DDR4": 1}
  
  def calcular_procesador(self, componente):
    return componente["Nucleos"] * 2 + componente["Hilos"] + float(componente["FrecuenciaTurbo"].split()[0]) * 10

  def calcular_tarjeta_grafica(self, componente):
    vram = int(componente["VRAM"].replace("GB", ""))
    return vram * 10 + (10000 / componente["Precio"])

  def calcular_ram(self, componente):
    capacidad = int(componente["Capacidad"].split()[0].replace("GB", ""))
    velocidad = int(componente["Velocidad"].replace(" MHz", ""))
    return capacidad * 5 + velocidad / 100

  def calcular_almacenamiento(self, componente):
    if componente["Tipo"] == "HDD":
      velocidad_disco = int(componente.get("Velocidad", "5400").replace(" RPM", ""))
      cache_valor = int(componente.get("Cache", "0").replace("MB", "").strip())
      return self.tipo_peso_almacenamiento["HDD"] * 10 + (velocidad_disco / 1000) + (cache_valor / 100)
    
    try:
      lectura = int(componente.get("VelocidadLectura", "500").replace(" MB/s", ""))
      return self.tipo_peso_almacenamiento[componente["Tipo"]] * 10 + lectura / 100
    except (KeyError, ValueError):
      return self.tipo_peso_almacenamiento.get(componente["Tipo"], 1) * 10

  def calcular_fuente(self, componente):
    potencia = int(componente["Potencia"].replace("W", ""))
    return potencia / 100 + self.certificacion_peso_fuente.get(componente["Certificacion"], 0)

  def calcular_caja(self, componente):
    return componente["Precio"] / 10 + len(componente["VentiladoresIncluidos"]) * 5

  def calcular_placa_base(self, componente):
    return (
      self.chipset_peso_placa.get(componente["Chipset"], 0) * 10
      + self.ram_peso_placa.get(componente["RAM"], 0) * 5
      + (10000 / componente["Precio"])
    )

def calcular_puntaje(componente, tipo):
  calculadora = CalculadoraPuntajes()
  puntaje_por_tipo = {
    "Procesador": calculadora.calcular_procesador,
    "TarjetaGrafica": calculadora.calcular_tarjeta_grafica,
    "RAM": calculadora.calcular_ram,
    "Almacenamiento": calculadora.calcular_almacenamiento,
    "FuenteDeAlimentacion": calculadora.calcular_fuente,
    "Caja": calculadora.calcular_caja,
    "PlacaBase": calculadora.calcular_placa_base,
  }
  
  if tipo in puntaje_por_tipo:
    return puntaje_por_tipo[tipo](componente)
  else:
    lgg.warning(f"Tipo de componente no soportado: {tipo}")
    return 0


# Función para seleccionar componentes
def seleccionar_componente(componentes, tipo, presupuesto_max):
  try:
    lgg.debug(f"Componentes recibidos para {tipo}: {componentes}")
    
    # Convertir a lista si es un diccionario
    if isinstance(componentes, dict) and "Basica" in componentes:
      componentes = componentes["Basica"]
    elif not isinstance(componentes, list):
      lgg.error(f"Se esperaba una lista, pero se recibió: {type(componentes)}")
      return None

    candidatos = [c for c in componentes if c["Precio"] <= presupuesto_max]
    lgg.debug(f"Candidatos válidos para {tipo}: {candidatos}")

    if not candidatos:
      return None

    # Calcular puntajes y manejar posibles errores
    puntajes_validos = []
    for c in candidatos:
      try:
        puntaje = calcular_puntaje(c, tipo)
        if puntaje is not None:
          puntajes_validos.append((c, puntaje))
          lgg.debug(f"Puntaje para {c['Modelo']}: {puntaje}")
      except Exception as e:
        lgg.warning(f"Error calculando puntaje para {c.get('Modelo', 'desconocido')}: {e}")

    if not puntajes_validos:
      return None

    mejor_componente, _ = max(puntajes_validos, key=lambda x: x[1])
    return mejor_componente
  except Exception as e:
    lgg.error(f"Error en seleccionar_componente: {e}")
    return None

# Verificar compatibilidad
def verificar_compatibilidad(configuracion):
  try:
    procesador = configuracion["Procesador"]
    placa_base = configuracion["Placa Base"]
    ram = configuracion["RAM"]
    fuente = configuracion["Fuente de Alimentación"]
    tarjeta_grafica = configuracion.get("Tarjeta Gráfica")

    # Verificar socket
    if procesador["Zocalo"] == placa_base["Socket"]:
      return False, "El socket del procesador no es compatible con la placa base."

    # Verificar RAM
    if ram["Tipo"].lower() != placa_base["RAM"].lower():
      return False, "El tipo de RAM no es compatible con la placa base."

    # Verificar velocidad de RAM
    ram_speed = int(ram["Velocidad"].split()[0])
    max_ram_speed = int(procesador["RAM_VelocidadMaxima"].split()[0])  # Extrae el valor numérico
    ram_compatibles = [
      r for r in data["RAM"] 
      if r["Tipo"] == placa_base["RAM"] 
      and r["Precio"] <= presupuesto * dist["RAM"]
      and int(r["Velocidad"].split()[0]) <= max_ram_speed  # Filtra por velocidad
    ]
    if not ram_compatibles:
      lgg.error(f"No se encontró RAM compatible con el tipo {placa_base['RAM']} y velocidad máxima {max_ram_speed}")
      return None, 0, 0

    ram = max(ram_compatibles, key=lambda x: (int(x["Capacidad"].split()[0].replace("GB", "")), int(x["Velocidad"].split()[0])))
    configuracion["RAM"] = ram
    
    if ram_speed > max_ram_speed:
      return False, f"La velocidad de RAM ({ram_speed}) excede el máximo soportado por el procesador ({max_ram_speed})"

    # Consumo total estimado (añadir 100W para otros componentes)
    consumo_total = procesador["Consumo"] + 100
    if tarjeta_grafica:
      # Estimar consumo de tarjeta gráfica si no está especificado
      consumo_gpu = tarjeta_grafica.get("Consumo", 300)  # valor estimado por defecto
      consumo_total += consumo_gpu

    if int(fuente["Potencia"].replace("W", "")) < consumo_total:
      return False, f"La fuente de {fuente['Potencia']} es insuficiente para el consumo total estimado de {consumo_total}W"

    return True, "Todos los componentes son compatibles."
  except Exception as e:
    lgg.error(f"Error en verificación de compatibilidad: {e}")
    return False, f"Error al verificar compatibilidad: {str(e)}"

# Estimar rendimiento
def estimar_rendimiento(configuracion, uso):
  puntaje = 0
  if "Procesador" in configuracion:
    puntaje += calcular_puntaje(configuracion["Procesador"], "Procesador") * 0.5
  if "Tarjeta Gráfica" in configuracion and uso != "Oficina":
    puntaje += calcular_puntaje(configuracion["Tarjeta Gráfica"], "TarjetaGrafica") * 0.4
  if "RAM" in configuracion:
    puntaje += calcular_puntaje(configuracion["RAM"], "RAM") * 0.1
  return puntaje

def seleccionar_placa_base_compatible(placas_base, procesador, presupuesto_max):
  
  placas_compatibles = [
    placa for placa in placas_base 
    if placa["Socket"] == procesador["Zocalo"] and placa["Precio"] <= presupuesto_max
  ]
  
  if not placas_compatibles:
    return None
      
  return max(placas_compatibles, key=lambda x: (x["Precio"] / 10 + (3 if x["Chipset"] in ["Z790", "X670E"] else 2 if x["Chipset"] in ["B650"] else 1)))
# Función principal para recomendar configuración

def recomendar_configuracion(uso, presupuesto):
  try:
    # Distribuir presupuesto según el uso
    distribucion = {
      "Gaming": {
        "Procesador": 0.25,
        "Tarjeta Gráfica": 0.35,
        "RAM": 0.1,
        "Almacenamiento": 0.1,
        "Placa Base": 0.1,
        "Fuente": 0.05,
        "Caja": 0.05
      },
      "Oficina": {
        "Procesador": 0.3,
        "RAM": 0.2,
        "Almacenamiento": 0.2,
        "Placa Base": 0.15,
        "Fuente": 0.1,
        "Caja": 0.05
      },
      "Diseño Gráfico": {
        "Procesador": 0.3,
        "Tarjeta Gráfica": 0.3,
        "RAM": 0.15,
        "Almacenamiento": 0.1,
        "Placa Base": 0.1,
        "Fuente": 0.05,
        "Caja": 0.05
      },
      "Programación": {
        "Procesador": 0.35,
        "RAM": 0.2,
        "Almacenamiento": 0.15,
        "Placa Base": 0.15,
        "Fuente": 0.1,
        "Caja": 0.05
      }
    }
    dist = distribucion[uso]
    configuracion = {}

    # 1. Primero seleccionar el procesador
    procesador = obtener_mejor_procesador(data["Procesadores"], presupuesto * dist["Procesador"])
    if not procesador:
      lgg.error("No se encontró un procesador dentro del presupuesto")
      return None, 0, 0

    # 2. Luego seleccionar una placa base compatible
    placa_base = seleccionar_placa_base_compatible(data["PlacasBase"], procesador, presupuesto * dist["Placa Base"])
    if not placa_base:
      lgg.error(f"No se encontró una placa base compatible con el socket {procesador['Zocalo']}")
      return None, 0, 0

    configuracion["Procesador"] = procesador
    configuracion["Placa Base"] = placa_base

    # 3. Seleccionar RAM compatible con la placa base
    ram_compatibles = [r for r in data["RAM"] if r["Tipo"] == placa_base["RAM"] and r["Precio"] <= presupuesto * dist["RAM"]]
    if not ram_compatibles:
      lgg.error(f"No se encontró RAM compatible del tipo {placa_base['RAM']}")
      return None, 0, 0
    
    ram = max(ram_compatibles, key=lambda x: int(x["Capacidad"].split()[0].replace("GB", "")))
    configuracion["RAM"] = ram

    # 4. Seleccionar el resto de componentes
    if uso != "Oficina":
      tarjeta_grafica = seleccionar_componente(data["TarjetasGraficas"], "TarjetaGrafica", presupuesto * dist.get("Tarjeta Gráfica", 0))
      if tarjeta_grafica:
        configuracion["Tarjeta Gráfica"] = tarjeta_grafica

    almacenamiento = seleccionar_componente(data["Almacenamiento"], "Almacenamiento", presupuesto * dist["Almacenamiento"])
    fuente = seleccionar_componente(data["FuentesDeAlimentacion"], "FuenteDeAlimentacion", presupuesto * dist["Fuente"])
    caja = obtener_mejor_caja(data["Cajas"], presupuesto * dist["Caja"])

    if None in [almacenamiento, fuente, caja]:
      lgg.error("Falta algún componente esencial")
      return None, 0, 0

    configuracion.update({
      "Almacenamiento": almacenamiento,
      "Fuente de Alimentación": fuente,
      "Caja": caja
    })

    # Verificar compatibilidad final
    compatibilidad, mensaje = verificar_compatibilidad(configuracion)
    if not compatibilidad:
      lgg.error(f"Configuración incompatible: {mensaje}")
      return None, 0, 0

    total = sum(c["Precio"] for c in configuracion.values() if c)
    rendimiento = estimar_rendimiento(configuracion, uso)
    
    lgg.info(f"Configuración exitosa con socket {procesador['Zocalo']} y placa {placa_base['Socket']}")
    return configuracion, total, rendimiento

  except Exception as e:
    lgg.error(f"Error en recomendar_configuracion: {e}")
    return None, 0, 0

# Interfaz de Streamlit
st.title("🛠️ Armador de PC Personalizado")
st.header("1. Define tu uso y presupuesto")

uso = st.selectbox("¿Para qué usarás la PC?", ["Gaming", "Oficina", "Diseño Gráfico", "Programación"])
presupuesto = st.slider("Presupuesto (USD)", 500, 5000, 1000)

if st.button("Generar Recomendación"):
  configuracion, total, rendimiento = recomendar_configuracion(uso, presupuesto)
  if configuracion:
    st.header("✅ Configuración Recomendada")
    st.write(f"**Procesador:** {configuracion['Procesador']['Modelo']} (${configuracion['Procesador']['Precio']})")
    if configuracion["Tarjeta Gráfica"]:
      st.write(f"**Tarjeta Gráfica:** {configuracion['Tarjeta Gráfica']['Modelo']} (${configuracion['Tarjeta Gráfica']['Precio']})")
    st.write(f"**RAM:** {configuracion['RAM']['Modelo']} (${configuracion['RAM']['Precio']})")
    st.write(f"**Almacenamiento:** {configuracion['Almacenamiento']['Modelo']} (${configuracion['Almacenamiento']['Precio']})")
    st.write(f"**Placa Base:** {configuracion['Placa Base']['Modelo']} (${configuracion['Placa Base']['Precio']})")
    st.write(f"**Fuente de Alimentación:** {configuracion['Fuente de Alimentación']['Modelo']} (${configuracion['Fuente de Alimentación']['Precio']})")
    st.write(f"**Caja:** {configuracion['Caja']['Modelo']} (${configuracion['Caja']['Precio']})")
    st.write(f"**Precio Total:** ${total}")
    st.write(f"**Rendimiento Estimado:** {rendimiento:.2f}")
  else:
    st.error("⚠️ No es posible armar un computador con ese presupuesto o no se encontraron componentes adecuados.")

