from tkinter import *

root=Tk()
root.iconbitmap("betis.ico")

miFrame=Frame(root,width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="betis.ico")
Label(miFrame, image=miImagen).place(x=100, y=200)
#Para crear un texto
miLabel=Label(miFrame, text="VIVA EL BETIS", fg="white", bg="green", font=("Comic Sans MS",18))
#En vez de empaquetar debemos de usar place para ubicarlo donde queramos
miLabel.place(x=100,y=180)
#Para ponerlo mas corto se pone y si solo usamos 1 label
#Label(miFrame, text="Hola alumnos de Python").place(x=100,y=200)
root.mainloop()