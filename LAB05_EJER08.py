#Programa: LAB05_EJER_08.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 28/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import tkinter as tk

def obtener_texto():
    texto_ingresado= cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: ")

ventana= tk.Tk()

etiqueta = tk.Label(ventana, text="Texto ingresado:")
etiqueta.pack()

cuadro_texto= tk.Entry (ventana, width=30)
cuadro_texto.pack()

boton= tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

ventana.mainloop()