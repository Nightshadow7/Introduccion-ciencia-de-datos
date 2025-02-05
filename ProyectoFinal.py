import streamlit as st
import json

# Cargar la base de datos desde el archivo JSON
with open("BaseProyecto.json", "r") as file:
    data = json.load(file)

# Función para obtener opciones de componentes
def get_options(category, key):
    options = []
    if category in data:
        for item in data[category]:
            options.append(item[key])
    return options

# Función para filtrar componentes por compatibilidad
def filter_components(category, filters):
    filtered = []
    if category in data:
        for item in data[category]:
            match = True
            for key, value in filters.items():
                if key in item and item[key] != value:
                  match = False
                  break
            if match:
                filtered.append(item)
    return filtered

# Interfaz de Streamlit
st.title("🛠️ Pc Select 🛠️")

# Selección de uso y presupuesto
st.header("1. Define tu uso y presupuesto")
uso = st.selectbox("¿Para qué usarás la PC?", ["Gaming", "Oficina", "Diseño Gráfico", "Programación"])
presupuesto = st.slider("Presupuesto (USD)", 500, 5000, 1000)

# Selección de procesador
st.header("2. Selecciona un Procesador")
marca_procesador = st.selectbox("Marca del Procesador", ["Intel", "AMD"])
generaciones = [gen["Generacion"] for gen in data["Procesadores"][marca_procesador]]
generacion = st.selectbox("Generación", generaciones)
modelos = [modelo["Modelo"] for modelo in data["Procesadores"][marca_procesador][generaciones.index(generacion)]["Modelos"]]
modelo_procesador = st.selectbox("Modelo", modelos)

# Obtener detalles del procesador seleccionado
procesador_seleccionado = next(
    modelo for modelo in data["Procesadores"][marca_procesador][generaciones.index(generacion)]["Modelos"]
    if modelo["Modelo"] == modelo_procesador
)

# Mostrar detalles del procesador
st.write(f"**Detalles del Procesador:**")
st.json(procesador_seleccionado)

# Selección de placa base compatible
st.header("3. Selecciona una Placa Base")
socket_procesador = "LGA 1700" if marca_procesador == "Intel" else "AM5"
placas_compatibles = filter_components("PlacasBase", {"Socket": socket_procesador})
opciones_placas = [f"{placa['Marca']} {placa['Modelo']} (${placa['Precio']})" for placa in placas_compatibles]
placa_seleccionada = st.selectbox("Placa Base Compatible", opciones_placas)

# Selección de RAM compatible
st.header("4. Selecciona Memoria RAM")
ram_compatibles = filter_components("RAM", {"Tipo": "DDR5" if "DDR5" in procesador_seleccionado["RAM_VelocidadMaxima"] else "DDR4"})
opciones_ram = [f"{ram['Marca']} {ram['Modelo']} ({ram['Capacidad']}, ${ram['Precio']})" for ram in ram_compatibles]
ram_seleccionada = st.selectbox("Memoria RAM Compatible", opciones_ram)

# Selección de almacenamiento
st.header("5. Selecciona Almacenamiento")
opciones_almacenamiento = [f"{alm['Marca']} {alm['Modelo']} ({alm['Capacidad']}, ${alm['Precio']})" for alm in data["Almacenamiento"]]
almacenamiento_seleccionado = st.selectbox("Almacenamiento", opciones_almacenamiento)

# Selección de tarjeta gráfica
st.header("6. Selecciona una Tarjeta Gráfica")
opciones_gpu = [f"{gpu['Marca']} {gpu['Modelo']} ({gpu['VRAM']}, ${gpu['Precio']})" for gpu in data["TarjetasGraficas"]]
gpu_seleccionada = st.selectbox("Tarjeta Gráfica", opciones_gpu)

# Selección de fuente de alimentación
st.header("7. Selecciona una Fuente de Alimentación")
opciones_fuente = [f"{fuente['Marca']} {fuente['Modelo']} ({fuente['Potencia']}, ${fuente['Precio']})" for fuente in data["FuentesDeAlimentacion"]]
fuente_seleccionada = st.selectbox("Fuente de Alimentación", opciones_fuente)

# Selección de caja
st.header("8. Selecciona una Caja")
opciones_caja = [f"{caja['Marca']} {caja['Modelo']} (${caja['Precio']})" for caja in data["Cajas"]["Media"]]
caja_seleccionada = st.selectbox("Caja", opciones_caja)

# Resumen de la configuración
st.header("✅ Resumen de tu Configuración")
st.write(f"**Procesador:** {marca_procesador} {modelo_procesador}")
st.write(f"**Placa Base:** {placa_seleccionada}")
st.write(f"**Memoria RAM:** {ram_seleccionada}")
st.write(f"**Almacenamiento:** {almacenamiento_seleccionado}")
st.write(f"**Tarjeta Gráfica:** {gpu_seleccionada}")
st.write(f"**Fuente de Alimentación:** {fuente_seleccionada}")
st.write(f"**Caja:** {caja_seleccionada}")

# Calcular precio total
precio_total = (
  procesador_seleccionado["Precio"]
  + next(placa["Precio"] for placa in placas_compatibles if f"{placa['Marca']} {placa['Modelo']} (${placa['Precio']})" == placa_seleccionada)
  + next(ram["Precio"] for ram in ram_compatibles if f"{ram['Marca']} {ram['Modelo']} ({ram['Capacidad']}, ${ram['Precio']})" == ram_seleccionada)
  + next(alm["Precio"] for alm in data["Almacenamiento"] if f"{alm['Marca']} {alm['Modelo']} ({alm['Capacidad']}, ${alm['Precio']})" == almacenamiento_seleccionado)
  + next(gpu["Precio"] for gpu in data["TarjetasGraficas"] if f"{gpu['Marca']} {gpu['Modelo']} ({gpu['VRAM']}, ${gpu['Precio']})" == gpu_seleccionada)
  + next(fuente["Precio"] for fuente in data["FuentesDeAlimentacion"] if f"{fuente['Marca']} {fuente['Modelo']} ({fuente['Potencia']}, ${fuente['Precio']})" == fuente_seleccionada)
  + next(caja["Precio"] for caja in data["Cajas"]["Media"] if f"{caja['Marca']} {caja['Modelo']} (${caja['Precio']})" == caja_seleccionada)
)

st.write(f"**Precio Total:** ${precio_total}")

# Verificar si el presupuesto es suficiente
if precio_total > presupuesto:
    st.error("⚠️ El precio total excede tu presupuesto.")
else:
    st.success("🎉 ¡Tu configuración está dentro del presupuesto!")