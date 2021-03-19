from tkinter import *
#Llamar a la raiz
raiz=Tk()
#Darle titulo a la ventana
raiz.title("Ventana de pruebas")
#Para redimensionar (Ancho,Alto), (0,0) no se puede hacer mas grande
raiz.resizable(1,1)
#Para poner una imagen como icono
raiz.iconbitmap("")
#Tamaño de la ventana
raiz.geometry("650x350")
#Cambiar configuaracion como fondo de pantalla
raiz.config(bg="blue")
#Para crear la ventana, siempre al final
raiz.mainloop()