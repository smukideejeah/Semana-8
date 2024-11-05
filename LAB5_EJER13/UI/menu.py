#Programa: Imvestigación de la librería tkinter
#archivo: menu.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/10/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Propósito: Crea un menú en la ventana principal
from tkinter import ttk, Menu
from UI.photos import default as showPhoto

def default(window: ttk):
    menu = Menu(window)
    window.config(menu=menu)

    compasMenu = Menu(menu, tearoff=0)

    for compa in ["Joseph", "Elmer", "Rafael", "Elvis"]:
        compasMenu.add_command(label=f"Foto de {compa}", command=lambda c = compa: showPhoto(window, c))

    menu.add_cascade(label="Foto de compas", menu=compasMenu)