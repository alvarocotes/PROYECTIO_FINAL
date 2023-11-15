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
        self.textbox()
        self.ocultar_cuadro()



    def cambiar_fondo(self):
        #cambiamos su fondo a una imagen
        self.imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/interfaz_inicio_sesion.png")

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

        self.otro4_boton = ttk.Button(text="CORREO ELECTRÓNICO").place(x=495, y=325)

        self.boton = ttk.Button(text="CONTRASEÑA").place(x=495, y=375)

    def textbox(self, tkk=None):

        # Correo electrónico
        entry = ttk.Entry()
        entry.place_forget()
        entry.place(x=650, y=325)

        #Contraseña
        entry1 = ttk.Entry()
        entry1 = ttk.Entry(show = "*")
        entry1.place(x=650, y=375)

        self.cuadro_texto = Entry(self.ventana_de_inicio)
        self.boton_ocultar = Button(self.ventana_de_inicio, text="Ocultar Cuadro de Texto", command=self.ocultar_cuadro)

        # Colocar el cuadro de texto y el botón en la ventana
        self.cuadro_texto.place(x=50, y=50)
        self.boton_ocultar.place(x=50, y=80)

    def ocultar_cuadro(self):
        # Ocultar el cuadro de texto al hacer clic en el botón
        self.cuadro_texto.place_forget()







Ventana_inicio = tk.Tk()
principal = Window(Ventana_inicio)
Ventana_inicio.mainloop()