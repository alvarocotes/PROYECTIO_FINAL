from tkinter import *
from tkinter import ttk
import tkinter as tk

class Window(ttk.Frame):

    def __init__(self, ventana_de_inicio):
        self.ventana_de_inicio = ventana_de_inicio
        self.ventana_de_inicio.title("ACUARIANOS")
        self.ventana_de_inicio.geometry("1350x1000")
        self.cambiar_fondo()
        self.cambiar_icono()
        self.crear_barra_progreso()
    def cambiar_fondo(self):
        #cambiamos su fondo a una imagen
        self.imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/Fondo_principal.png")
        #y para proyectar la imagen se crea un lienzo con la función de canvas
        self.lienzo = tk.Canvas(self.ventana_de_inicio, width=1350, height=1000)
        self.lienzo.pack()
        self.lienzo.create_image(0, 0, anchor=NW, image=self.imagen_fondo)

    def cambiar_icono(self):
        self.ventana_de_inicio.iconbitmap("C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/icono.ico")

    def crear_barra_progreso(self):
        self.progressbar = ttk.Progressbar(orient=tk.HORIZONTAL, length=160)
        self.progressbar.place(x=625, y=380)

Ventana_inicio = tk.Tk()
principal = Window(Ventana_inicio)
Ventana_inicio.mainloop()





