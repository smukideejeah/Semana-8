#Programa: LAB05_EJER_10.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 28/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Muestra una lista de opciones y permite seleccionar varias opciones para luego mostrarlas en consola.

import tkinter as tk

def selected():
    if var.get():
        print("Seleccionado")
    else:
        print("seleccionado")


window = tk.Tk()
var = tk.BooleanVar()

check = tk.Checkbutton(window, text="Seleccionar", variable=var, command=selected)
check.pack()

window.mainloop()
