#Programa: Imvestigación de la librería tkinter
#archivo: form.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Crear un formulario para ingresar datos personales
#Descripción del Programa: Este programa es un formulario que permite al usuario ingresar datos personales para ser almacenados en un archivo json.
import tkinter as tk
from tkinter import ttk
from UI.menu import default as initMenu

# Configuración de la ventana principal
def createForm():
    window = tk.Tk()
    window.title("Fotos Compas")
    window.resizable(False, False)
    window.geometry("800x600")

    initMenu(window)
    window.mainloop()
