
#Programa: LAB05
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

from tkinter import*
ventana = Tk()
ventana.title("Uso de imágenes en Tkinter")
ventana.geometry("125x103")
imagen=PhotoImage(file="imagen.png")
fondo=Label (ventana, image=imagen). place (x=0,y=0) 
ventana.mainloop()