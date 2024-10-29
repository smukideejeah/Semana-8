#Programa: LAB05_EJER_11.py
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

list = tk.Listbox(window, width=30, selectmode=tk.MULTIPLE)
list.pack()

carParts = ["Motor", "Ruedas", "Puertas", "Ventanas", "Parabrisas", "Asientos", "Espejos", "Luces", "Frenos", "Aire Acondicionado"]
for part in carParts:
    list.insert(tk.END, part)


button = tk.Button(window, text="Ver seleccionados", command=selected)
button.pack()

window.mainloop()
