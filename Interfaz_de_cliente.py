from tkinter import *
from tkinter import ttk
import tkinter as tk

class Window(ttk.Frame):

    def __init__(self, ventana_de_inicio):
        self.ventana_de_inicio = ventana_de_inicio
        self.ventana_de_inicio.title("ACUARIANOS")
        self.ventana_de_inicio.geometry("1350x1000")
        self.cambiar_fondo()
        self.botones()
    def cambiar_fondo(self):
        #cambiamos su fondo a una imagen
        self.imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/interfaz_cliente.png")
        #y para proyectar la imagen se crea un lienzo con la función de canvas
        self.lienzo = tk.Canvas(self.ventana_de_inicio, width=1350, height=1000)
        self.lienzo.pack()
        self.lienzo.create_image(0, 0, anchor=NW, image=self.imagen_fondo)
    def botones(self):
        estilo = ttk.Style()
        estilo.configure("TButtom", foreground="#ff0000")
        self.boton = ttk.Button(text="PENSANDOLO BIEN, NO QUIERO VIVIR").place(x=0, y=0)

        self.boton = ttk.Button(text="INICIAR TU VIDA").place(x=650, y=325)
        es_boton = ttk.Style()
        es_boton.configure("TButtom", foreground="#ff0000")
        self.otro_boton = ttk.Button(text="PASO 1 PARA INICIAR TU VIDA").place(x=650, y=375)




Ventana_cliente = tk.Tk()
principal = Window(Ventana_cliente)
Ventana_cliente.mainloop()