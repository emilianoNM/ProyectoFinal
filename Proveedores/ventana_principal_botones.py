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
titulo1=Label(titulo,text="ELIGE UNA OPCIÓN",font=(80))
titulo1.grid(row=2,column=1)
titulo1.config(bd=10)
titulo1.config(relief="groove")


botones=Frame(root,width=10,height=20)
botones.pack(fill="y")
Agregar=Button(botones,command=interfaz_guardar_proveedores_conexion.ventanaguardar,text="Agregar Proveedor",background="white")
Agregar.grid(row=1,column=1)
Buscar=Button(botones,command=interfaz_buscar_proveedores_conexion.ventanabuscar,text="Buscar Proveedor",background="white")
Buscar.grid(row=1,column=5)
Pedido=Button(botones,text="Validar Pedido",background="white")
Pedido.grid(row=2,column=1)
Fecha=Button(botones,text="Agregar Fecha",background="white")
Fecha.grid(row=2,column=5)
botones.config(bd=5)
botones.config(relief="groove")
botones.config(cursor="hand2")

root.mainloop()
