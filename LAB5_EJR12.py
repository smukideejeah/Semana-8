#Programa: LAB05_EJER_12.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 28/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Propósito: Muestra una lista de opciones y permite seleccionar varias opciones para luego mostrarlas en consola.

import tkinter as tk

def selected():
    sel = list.curselection()
    for index in sel:
        print(list.get(index))


window = tk.Tk()

var = tk.IntVar()

radio1 = tk.Radiobutton(window, text="Opción 1", value=1, command=selected, variable=var)
radio1.pack()

radio2 = tk.Radiobutton(window, text="Opción 2", value=2, command=selected, variable=var)
radio2.pack()

radio3 = tk.Radiobutton(window, text="Opción 3", value=3, command=selected, variable=var)
radio3.pack()

window.mainloop()