import tkinter

from tkinter import *

root=Tk()
#root.geometry("500x300+100+100")
root.title('Proveedores')
#Titulo
titulo=Frame(root,width=500,height=400)
titulo.pack(fill="y")
titulo1=Label(titulo,text="PROVEEDORES",font=(80))
titulo1.grid(row=1,column=1)
titulo1.config(bd=10)
titulo1.config(relief="groove")
#nombre del proveedor
cuerpo=Frame(root,width=500,height=400)
cuerpo.pack(fill="x")
nombre_label=Label(cuerpo,text="Nombre Proveedor:")
nombre_label.grid(row=2,column=1,sticky="e",padx=10,pady=5)
nombre_str=StringVar()
nombre_entry=Entry(cuerpo,textvariable=nombre_str)
nombre_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
#Logo
producto_label=Label(cuerpo,text="Logo/Código:")
producto_label.grid(row=3,column=1,sticky="e",padx=10,pady=5)
producto_str=StringVar()
producto_entry=Entry(cuerpo,textvariable=producto_str)
producto_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
#Télefono
cantidad_label=Label(cuerpo,text="Telefono: ")
cantidad_label.grid(row=4,column=1,sticky="e",padx=10,pady=5)
cantidad_str=StringVar()
cantidad_entry=Entry(cuerpo,textvariable=cantidad_str)
cantidad_entry.grid(row=4,column=2,sticky="e",padx=10,pady=5)
#Correo
mail_label=Label(cuerpo,text="Correo: ")
mail_label.grid(row=5,column=1,sticky="e",padx=10,pady=5)
mail_str=StringVar()
mail_entry=Entry(cuerpo,textvariable=mail_str)
mail_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
#Direccion
mail_label=Label(cuerpo,text="Dirección: ")
mail_label.grid(row=6,column=1,sticky="e",padx=10,pady=5)
mail_str=StringVar()
mail_entry=Entry(cuerpo,textvariable=mail_str)
mail_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)

#final
botones=Frame(root,width=10,height=20)
botones.pack(fill="y")
Guardar=Button(botones,text="Guardar",relief=FLAT)
Guardar.grid(row=1,column=1)
Cancelar=Button(botones,text="Cancelar",relief=FLAT)
Cancelar.grid(row=1,column=2)
botones.config(bd=5)
botones.config(relief="groove")
botones.config(cursor="hand2")

#mainloop
root.mainloop()
