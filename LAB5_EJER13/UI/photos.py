#Programa: Imvestigación de la librería tkinter
#archivo: searchByProvince.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Ventana que obtiene los registros de una provincia
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import os
import tkinter as tk

def default(main: tk, compa: str):

    window = tk.Toplevel(main)
    window.title(f"Foto de {compa}")
    window.geometry("800x400")

    imageFrame = tk.Frame(window)
    imageFrame.pack()
    ROOT_DIR = os.path.abspath(os.curdir)
    image = tk.PhotoImage(file=f"{ROOT_DIR}/LAB5_EJER13/img/{compa}.png") 
    label = tk.Label(imageFrame, image=image)
    label.pack(side="left")

    window.mainloop()
