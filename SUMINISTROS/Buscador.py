from tkinter import *

Buscador=Tk()
Buscador.title("Buscador")
buscar=Frame(height=100,width=200)
buscar.pack()
boton1 = Button(buscar,text="Buscar").place(x=15,y=20)
entrada=StringVar()
campo = Entry(buscar,textvariable=entrada).place(x=70,y=25)
Buscador.mainloop()

