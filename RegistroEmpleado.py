#INTERFAZ REGISTRO DE EMPLEADO

import tkinter

#Agregar un boton
from tkinter import messagebox

#Agregar campo de texto
root =tkinter.Tk()
root.geometry("500x300+100+100")

txt1=tkinter.Entry(root).place(x=80,y=20)
txt2=tkinter.Entry(root).place(x=80,y=40)
txt3=tkinter.Entry(root, width=40).place(x=80,y=60)
txt4=tkinter.Entry(root,width=10).place(x=60,y=80)
txt5=tkinter.Entry(root,width=10).place(x=60,y=100)
txt6=tkinter.Entry(root, width=10).place(x=100,y=120)
txt7=tkinter.Entry(root).place(x=100,y=140)

#Creamos Etiqueta
registro=tkinter.Label(root,text="REGISTRO DE EMPLEADO").place(x=100,y=0)
nombre=tkinter.Label(root,text="Nombre").place(x=10,y=20)
apellido=tkinter.Label(root,text="Apellidos").place(x=10,y=40)
direccion=tkinter.Label(root,text="Direccion").place(x=10,y=60)
edad=tkinter.Label(root,text="Edad").place(x=10,y=80)
rfc=tkinter.Label(root,text="RFC").place(x=10,y=100)
codpos=tkinter.Label(root,text="Codigo Postal").place(x=10,y=120)
password=tkinter.Label(root,text="Contraseña").place(x=10,y=140)

#Creamos Botones
bsave=tkinter.Button(root,text="Guardar").place(x=150,y=200)
bexit=tkinter.Button(root,text="Salir").place(x=250,y=200)

root.mainloop()

