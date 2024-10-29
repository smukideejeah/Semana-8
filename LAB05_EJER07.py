#Programa: LAB05_EJER_07.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 28/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import tkinter as tk



def cambiar_texto():
    etiqueta.config(text="Texto cambiado!")

Ventana=tk.Tk()
etiqueta=tk.Label(Ventana, text="Texto original")
etiqueta.pack()
#Crear un boton con texto y funcion de comando 
boton1=tk.Button(Ventana, text="Cambiar", command=cambiar_texto )
boton1.pack()
    #Crear un boton con colores de fondo y texto personalizados 
boton2=tk.Button(Ventana, text="Boton 2", bg="blue", fg="white", font=("Arial", 12) )
boton2.pack()
    #Crear un boton deshabilitado
boton3=tk.Button(Ventana, text="deshabilitado", state="disabled")
boton3.pack()

Ventana.mainloop()