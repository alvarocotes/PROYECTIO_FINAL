import tkinter as tk
from tkinter import *
from tkinter import ttk


class Window(ttk.Frame):
    def __init__(self, ventana_de_inicio):
        self.ventana_de_inicio = ventana_de_inicio
        self.ventana_de_inicio.title("ACUARIANOS")
        self.ventana_de_inicio.geometry("1350x1000")
        label = Label(self.ventana_de_inicio, text="¡Saludos, Mundo!", font=("Arial", 16))
        label.pack(anchor = CENTER)


        self.cambiar_fondo()
        self.cambiar_icono()
        self.botones()



    def cambiar_fondo(self):
        #cambiamos su fondo a una imagen
        self.imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/interfaz_registro.png")

        #y para proyectar la imagen se crea un lienzo con la función de canvas
        self.lienzo = tk.Canvas(self.ventana_de_inicio, width=1350, height=1000)
        self.lienzo.pack()
        self.lienzo.create_image(0, 0, anchor=NW, image=self.imagen_fondo)

    def cambiar_icono(self):
        self.ventana_de_inicio.iconbitmap("C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/icono.ico")

    def botones(self):
        estilo = ttk.Style()
        estilo.configure("TButtom", foreground= "#ff0000")


        es_boton = ttk.Style()
        es_boton.configure("TButtom", foreground= "#ff0000" )

        self.otro4_boton = ttk.Button(text="NOMBRE").place(x=515, y=325)

        self.boton = ttk.Button(text="CORREO ELECTRÓNICO").place(x=725, y=325)

        self.otro1_boton = ttk.Button(text="CONTRASEÑA").place(x=515, y=375)

        self.otro2_boton = ttk.Button(text="TÉLEFONO").place(x=725, y=375)

        self.otro3_boton = ttk.Button(text="N-° DE IDENTIFICACIÓN").place(x=515, y=425)

        self.otro5_boton = ttk.Button(text="EDAD").place(x=725, y=425)

        self.otro6_boton = ttk.Button(text="GÉNERO").place(x=515, y=475)

        self.otro7_boton = ttk.Button(text="CONTINUAR").place(x=650, y=550)



Ventana_inicio = tk.Tk()
principal = Window(Ventana_inicio)
Ventana_inicio.mainloop()