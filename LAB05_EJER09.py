#Programa: LAB05_EJER_09.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 28/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import tkinter as tk

def obtener_seleccion():
    seleccionados= cuadro_lista.cursoselection()
    for index in seleccionados:
        elemento= cuadro_lista.get(index)
        print("Elemento seleccionado")

ventana= tk.Tk()

cuadro_lista= tk.Listbox(ventana,width=30, selectmode="multiple")
cuadro_lista.pack()

elementos= ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton= tk.Button(ventana, text="obtener", command=obtener_seleccion)
boton.pack()

ventana.mainloop()