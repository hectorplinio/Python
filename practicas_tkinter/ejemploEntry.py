from tkinter import *

raiz=Tk()
miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()
#El punto grid es para hacer una tabla de filas y columnas
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,pady=5, padx=5)
cuadroNombre.config(fg="red", justify="center")
#Esto es para poner contraseñas que salgan ocultas, importante poner el show
cuadroContra=Entry(miFrame)
cuadroContra.grid(row=1,column=1,pady=5, padx=5)
cuadroContra.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,pady=5, padx=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,pady=5, padx=5)
#Si ponemos Text sale un cuadro mas grande para añadir comentarios
cuadroComentario=Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=4,column=1,pady=5, padx=5)
#cuadroComentario.config(yscrollcommand=scrollVert.set)
#Para crear una barra lateral para el cuadro de comentarios, sticky para que se adapte al cuadro
scrollVert=Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")


#Sticky es para ponerlos en un lateral o arriba o bajo pegado.
#Padx y Pady es el margen con los ejes X e Y
nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e",pady=5, padx=5)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=2,column=0,sticky="e",pady=5, padx=5)

correoLabel=Label(miFrame,text="Direccion de correo: ")
correoLabel.grid(row=3,column=0,sticky="e",pady=5, padx=5)

passLabel=Label(miFrame,text="Contraseña: ")
passLabel.grid(row=1,column=0,sticky="e",pady=5, padx=5)

comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,sticky="e",pady=5, padx=5)

raiz.mainloop()