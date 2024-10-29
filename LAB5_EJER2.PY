#Programa: LAB05
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 23/09/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code

import tkinter as tk

ventana = tk.Tk()

#Obtener las dimenciones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #metodo para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #metodo para obtener Alto

#Calcular las coordenadas para centrar la ventana 
ancho_ventana = 800 
alto_ventana = 600
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

#Establecer el tamaño y la posicion de la ventana 
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

ventana.mainloop()