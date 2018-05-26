import tkinter

from tkinter import messagebox

root =tkinter.Tk()
root.geometry("500x300+100+100")

def sCallBack():
    messagebox.showinfo("¡AVISO!","¿Deseas continuar con esta accion?")

#Creamos cuadro de texto
empleado=tkinter.Entry(root,width=40).place(x=100,y=20)

#Creamos etiqueta
registro=tkinter.Label(root,text="ACCIONES").place(x=250,y=0)
nombre=tkinter.Label(root,text="Nombre del Empleado").place(x=10,y=20)

#Creamos Boton
bdespido=tkinter.Button(root,text="Despido",command=sCallBack).place(x=150,y=50)
beditar=tkinter.Button(root,text="Editar").place(x=250,y=50)
bexit=tkinter.Button(root,text="Cancelar").place(x=350,y=50)

#Llamamos lo botones
bdespido.pack()


roop.mainloop()
