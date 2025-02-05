import random
import time
import json
import tkinter as tk
from tkinter import messagebox
from typing import List, Dict
import matplotlib.pyplot as plt

class Pregunta:
  def __init__(self, texto: str, respuesta: str, opciones: List[str], categoria: str):
    self.texto = texto
    self.respuesta = respuesta
    self.opciones = opciones
    self.categoria = categoria

class JeopardyGame:
  def __init__(self, root):
    self.root = root
    self.root.title("Jeopardy Game")
    self.root.geometry("500x400")
    self.dinero_acumulado = 0
    self.rondas = 0
    self.correctas = 0
    self.incorrectas = 0
    self.ayudas = {"50/50": True, "Llamada a un amigo": True, "Preguntar al público": True}
    self.record_historico = self._cargar_record()
    self.preguntas = self._cargar_preguntas_json()
    self.actualizar_interfaz()

  def actualizar_interfaz(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    tk.Label(self.root, text=f"Dinero acumulado: ${self.dinero_acumulado}", font=("Arial", 14)).pack(pady=10)
    tk.Button(self.root, text="Iniciar Juego", font=("Arial", 12), command=self.jugar).pack(pady=5)
    tk.Button(self.root, text="Ver Estadísticas", font=("Arial", 12), command=self.mostrar_estadisticas).pack(pady=5)
    if any(self.ayudas.values()):
      tk.Label(self.root, text="Ayudas disponibles:", font=("Arial", 12)).pack(pady=5)
      for ayuda, disponible in self.ayudas.items():
        if disponible:
          tk.Button(self.root, text=ayuda, font=("Arial", 10), command=lambda a=ayuda: self.usar_ayuda(a)).pack(pady=2)

  def usar_ayuda(self, ayuda):
    if self.ayudas[ayuda]:
      messagebox.showinfo("Ayuda usada", f"Has usado: {ayuda}")
      self.ayudas[ayuda] = False
    else:
      messagebox.showwarning("No disponible", "Esta ayuda ya ha sido utilizada.")
    self.actualizar_interfaz()

  def mostrar_pregunta(self, pregunta: Pregunta):
    for widget in self.root.winfo_children():
      widget.destroy()
    tk.Label(self.root, text=f"Categoría: {pregunta.categoria}", font=("Arial", 12)).pack(pady=5)
    tk.Label(self.root, text=pregunta.texto, font=("Arial", 14), wraplength=400).pack(pady=10)
    opciones = random.sample(pregunta.opciones, len(pregunta.opciones))
    for i, opcion in enumerate(opciones):
      tk.Button(self.root, text=opcion, font=("Arial", 12), command=lambda o=opcion: self.verificar_respuesta(o, pregunta)).pack(pady=3)
    self.actualizar_interfaz()
  
  def _cargar_record(self) -> int:
    try:
      with open("record.txt", "r") as f:
        return int(f.read().strip())
    except FileNotFoundError:
      return 0
  
  def _cargar_preguntas_json(self) -> Dict[str, List[Pregunta]]:
    try:
      with open("BancoPreguntas.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

      preguntas_por_nivel = {}
      for nivel, preguntas in datos.items():
        preguntas_por_nivel[nivel] = [
          Pregunta(
            texto=p["pregunta"],
            respuesta=p["respuesta"],
            opciones=p["opciones"],
            categoria=p.get("categoria", "General")  # Usa "General" si no hay categoría
          ) for p in preguntas
        ]
      return preguntas_por_nivel

    except FileNotFoundError:
      print("¡Error! No se encontró el archivo BancoPreguntas.json")
      return {}

    except json.JSONDecodeError:
      print("¡Error! El archivo JSON no tiene el formato correcto")
      return {}
  
  def jugar(self):
    print("\n¡Bienvenido al juego de Jeopardy!")
    print(f"Récord actual: ${self.record_historico}")
    
    # Aquí puedes llamar a una función para iniciar la interfaz del juego
    self.mostrar_siguiente_pregunta()
  
  def mostrar_estadisticas(self):
    stats_window = tk.Toplevel(self.root)
    stats_window.title("Estadísticas del Juego")
    stats_window.geometry("300x200")

    tk.Label(stats_window, text=f"Récord Histórico: ${self.record_historico}", font=("Arial", 12)).pack(pady=10)
    tk.Label(stats_window, text=f"Dinero Acumulado: ${self.dinero_acumulado}", font=("Arial", 12)).pack(pady=10)
    tk.Button(stats_window, text="Cerrar", command=stats_window.destroy).pack(pady=10)

  def usar_ayuda(self, pregunta):
    self.ayuda_disponible = False  # Desactivar la ayuda para el resto del juego
    mensaje_ayuda = f"Pista: La respuesta empieza con '{pregunta.respuesta[0]}'"
    messagebox.showinfo("Ayuda", mensaje_ayuda)
    
  def mostrar_siguiente_pregunta(self):
    if not self.preguntas:
      messagebox.showinfo("Fin del Juego", f"¡Juego terminado! Dinero ganado: ${self.dinero_acumulado}")
      return
    nivel_actual = random.choice(list(self.preguntas.keys()))
    pregunta = random.choice(self.preguntas[nivel_actual])
    for widget in self.root.winfo_children():
      widget.destroy()
    tk.Label(self.root, text=f"Categoría: {pregunta.categoria}", font=("Arial", 14)).pack(pady=10)
    tk.Label(self.root, text=pregunta.texto, font=("Arial", 12)).pack(pady=10)
    opciones = pregunta.opciones.copy()
    random.shuffle(opciones)
    for opcion in opciones:
      tk.Button(self.root, text=opcion, font=("Arial", 12), command=lambda o=opcion: self.verificar_respuesta(o, pregunta.respuesta)).pack(pady=5)
    # Botón de ayuda (si está disponible)
    if self.ayuda_disponible:
      tk.Button(self.root, text="Usar ayuda", font=("Arial", 12), command=lambda: self.usar_ayuda(pregunta)).pack(pady=5)


  def verificar_respuesta(self, seleccion, correcta):
    if seleccion == correcta:
      messagebox.showinfo("Correcto", "¡Respuesta correcta! 🎉")
      self.dinero_acumulado += 100
      self.mostrar_siguiente_pregunta()  # Sigue jugando
    else:
      messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La correcta era: {correcta}")
      messagebox.showinfo("Fin del Juego", f"Juego terminado. Dinero ganado: ${self.dinero_acumulado}")
      self.root.quit()  # Cierra la ventana

if __name__ == "__main__":
  root = tk.Tk()
  juego = JeopardyGame(root)
  root.mainloop()
