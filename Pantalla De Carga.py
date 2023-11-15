import tkinter as tk
from tkinter import *

def cargar_aplicacion():
    # Simula una operación de carga
    # Puedes personalizar la duración o la operación aquí
    for _ in range(10):
        pantalla_carga.update()
        pantalla_carga.after(1000)  # Espera 1 segundo

    # Cierra la pantalla de carga
    pantalla_carga.destroy()

# Crea la pantalla de carga
pantalla_carga = tk.Tk()
pantalla_carga.title("Cargando...")
pantalla_carga.geometry("1350x1000")
pantalla_carga

# Agrega un mensaje o una etiqueta
mensaje = tk.Label(pantalla_carga, text="Cargando, por favor espere...")
mensaje.pack(pady=20)

# Inicia la operación de carga
cargar_aplicacion()