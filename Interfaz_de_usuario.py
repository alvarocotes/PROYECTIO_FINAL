import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Window(ttk.Frame):
    def __init__(self, ventana_de_inicio):
        self.ventana_de_inicio = ventana_de_inicio
        self.ventana_de_inicio.title("ACUARIANOS")
        self.ventana_de_inicio.geometry("1350x1000")
        self.ventana_de_inicio.resizable(width=False, height=False)


        self.cambiar_fondo()
        self.cambiar_icono()
        self.botones()



    def cambiar_fondo(self):
        #cambiamos su fondo a una imagen
        self.imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/Fondo_interfaz_usuario.png")

        #y para proyectar la imagen se crea un lienzo con la función de canvas
        self.lienzo = tk.Canvas(self.ventana_de_inicio, width=1350, height=1000)
        self.lienzo.pack()
        self.lienzo.create_image(0, 0, anchor=NW, image=self.imagen_fondo)

    def cambiar_icono(self):
        self.ventana_de_inicio.iconbitmap("C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/icono.ico")


    def iniciar_sesion(self):
        self.ventana_de_inicio.withdraw()
        iniciar_sesion= tk.Toplevel()
        iniciar_sesion.geometry("1350x1000")
        correo_e = ttk.Label(iniciar_sesion, text = "Correo Electrónico: ")
        correo_e.pack(padx = 520, pady=325, ipadx= 520)
        self.correo = ttk.Entry(iniciar_sesion)
        self.correo.place(x= 650, y= 325)
        contrasena_e = ttk.Label(iniciar_sesion, text="Contraseña: ")
        contrasena_e.pack(padx=525, pady=375, ipadx=525, ipady = 375)
        self.contrasena = ttk.Entry(iniciar_sesion, show = "*")
        self.contrasena.place(x=650, y=375)






    def usuario(self):
        self.ventana_de_inicio.withdraw()
        usuario = tk.Toplevel()
        usuario.geometry("1350x1000")
        estilos = ttk.Style()
        estilos.configure("TButtom", foreground="#ff0000")
        self.botone = ttk.Button(usuario, text="Iniciar sesión", command=self.iniciar_sesion).place(x=650, y=325)
        self.botone = ttk.Button(usuario, text="Registrarse").place(x=650, y=375)
    def empleado(self):
        self.ventana_de_inicio.withdraw()
        empleado = tk.Toplevel()
        empleado.geometry("1350x1000")



    def botones(self):
        estilo = ttk.Style()
        estilo.configure("TButtom", foreground= "#ff0000")
        self.boton = ttk.Button(text= "Usuario", command = self.usuario).place(x=650, y=325)

        es_boton = ttk.Style()
        es_boton.configure("TButtom", foreground= "#ff0000" )
        self.otro_boton = ttk.Button(text="Empleado", command = self.empleado).place(x=650, y=375)







Ventana_inicio = tk.Tk()
principal = Window(Ventana_inicio)
Ventana_inicio.mainloop()