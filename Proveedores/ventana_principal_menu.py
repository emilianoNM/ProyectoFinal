import tkinter 
import interfaz_guardar_proveedores_conexion
import interfaz_buscar_proveedores_conexion

from tkinter import *

root=Tk()
#root.geometry("500x300+100+100")
root.title('Proveedores')
#Titulo
titulo=Frame(root,width=500,height=400)
titulo.pack(fill="y")
titulo1=Label(titulo,text="MENU PROVEEDORES",font=(80))
titulo1.grid(row=1,column=1)
titulo1.config(bd=10)
titulo1.config(relief="groove")

#ventana
Vetana=Frame(root,width=500,height=400)
Vetana.pack(fill="y")
Vetana.config(relief="groove")

var=StringVar()
var.set('Elige una accion')
opciones=['Agregar Proveedor','Buscar Proveedor','Validad Pedido','Aregar entrega']
opciones=OptionMenu(Vetana,var,*opciones)
opciones.config(background="white")
opciones.grid(row=2,column=1)


def ok():
    stropcion=var.get()
    print (stropcion)
    if stropcion in ("Agregar Proveedor"):
        return interfaz_agregar_proveedores_conexion
    if stropcion in ("Buscar Proveedor"):
        return interfaz_buscar_proveedores_conexion.ventanabuscar


botones=Frame(root,width=10,height=20)
botones.pack(fill="y")
OK=Button(botones,command=ok,text="Ok")
OK.grid(row=1,column=1)
#Buscar=Button(botones,command=interfaz_buscar_proveedores_conexion.ventanabuscar,text="Buscar Proveedor",background="white")
#Buscar.grid(row=1,column=2)
#Pedido=Button(botones,text="Hacer Pedido",background="gray")
#Pedido.grid(row=1,column=20)
botones.config(bd=10)
botones.config(relief="groove")
botones.config(cursor="hand2")

root.mainloop()
