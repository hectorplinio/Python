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
#raiz.geometry("650x350")
#Cambiar configuaracion como fondo de pantalla
raiz.config(bg="blue")
#Crear el frame
miFrame=Frame()
#Empaquetar el frame, fill="x" es para expandir el frame al redimensionar fill="y", expand="True" y fill="both" redimensionar en x y en Y.
miFrame.pack(side="right", anchor="n") #Si ponemos esto al redimensionar el frame se ancla a un lateral y arriba)
#Configuarar el frame
miFrame.config(bg="red")
#Configurar el tamaño del frame, ventana se ajusta al frame
miFrame.config(width="650", height="350")
#Para cambiar grosor del borde
miFrame.config(bd="35")
#Para cambiar el borde
miFrame.config(relief="groove")
#Para cambiar forma del cursor, para ver esto ver documentacion
miFrame.config(cursor="pirate")
#Para crear la ventana, siempre al final
raiz.mainloop()