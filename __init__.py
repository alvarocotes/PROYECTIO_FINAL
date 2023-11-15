from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana = Tk()
Ventana.title("NATA IS BEAUTIFULL")

Ventana.geometry("1350x1000")
imagen_fondo = PhotoImage(file="C:/Users/Famil/OneDrive/Escritorio/ACUARIANOS/Fondo_principal.png")
lienzo = Canvas(Ventana, width=1350, height=1000)
lienzo.pack()
lienzo.create_image(0, 0, anchor=NW, image=imagen_fondo)
progressbar = ttk.Progressbar(orient=tk.HORIZONTAL, length=160)
progressbar.place(x=650, y=480)
Ventana.mainloop()

