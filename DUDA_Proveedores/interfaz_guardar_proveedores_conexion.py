import proveedores

import tkinter

from tkinter import *

def ventanaguardar():
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
    #numero del proveedor
    cuerpo=Frame(root,width=500,height=400)
    cuerpo.pack(fill="x")
    etiqueta_numerop=Label(cuerpo,text="Numero Proveedor:")
    etiqueta_numerop.grid(row=2,column=1,sticky="e",padx=10,pady=5)
    numero_p=StringVar()
    numero_entry=Entry(cuerpo,textvariable=numero_p)
    numero_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
    #nombre del proveedor
    etiqueta_nombre=Label(cuerpo,text="Nombre Proveedor:")
    etiqueta_nombre.grid(row=3,column=1,sticky="e",padx=10,pady=5)
    nombre_p=StringVar()
    nombre_entry=Entry(cuerpo,textvariable=nombre_p)
    nombre_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
    #Logo
    etiqueta_logo=Label(cuerpo,text="Logo/Código:")
    etiqueta_logo.grid(row=4,column=1,sticky="e",padx=10,pady=5)
    logo=StringVar()
    logo_entry=Entry(cuerpo,textvariable=logo)
    logo_entry.grid(row=4,column=2,sticky="e",padx=10,pady=5)
    #Razon Social
    etiqueta_rs=Label(cuerpo,text="Razon Social: ")
    etiqueta_rs.grid(row=5,column=1,sticky="e",padx=10,pady=5)
    razon_social=StringVar()
    rs_entry=Entry(cuerpo,textvariable=razon_social)
    rs_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
    #Télefono
    etiqueta_telefono=Label(cuerpo,text="Telefono: ")
    etiqueta_telefono.grid(row=6,column=1,sticky="e",padx=10,pady=5)
    telefono_p=StringVar()
    telefono_entry=Entry(cuerpo,textvariable=telefono_p)
    telefono_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
    #Correo
    etiqueta_correo=Label(cuerpo,text="Correo: ")
    etiqueta_correo.grid(row=7,column=1,sticky="e",padx=10,pady=5)
    correo_p=StringVar()
    correo_entry=Entry(cuerpo,textvariable=correo_p)
    correo_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)
    #Direccion
    etiqueta_d=Label(cuerpo,text="Dirección: ")
    etiqueta_d.grid(row=8,column=1,sticky="e",padx=10,pady=5)
    direccion_p=StringVar()
    direccion_entry=Entry(cuerpo,textvariable=direccion_p)
    direccion_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)

    def save():
        print(nombre_p.get())
        strNumero=numero_p.get()
        strNombre=nombre_p.get()
        strLogo=logo.get()
        strRs=razon_social.get()
        strTelefono=telefono_p.get()
        strCorreo=correo_p.get()
        strDir=direccion_p.get()

        a=proveedores.Proveedores(strNumero,strNombre,strLogo,strRs,strTelefono,strCorreo,strDir)
        a.save()
        
        numero_p.set("")
        nombre_p.set("")
        logo.set("")
        razon_social.set("")
        telefono_p.set("")
        correo_p.set("")
        direccion_p.set("")

    def cancelar():
        numero_p.set("")
        nombre_p.set("")
        logo.set("")
        razon_social.set("")
        telefono_p.set("")
        correo_p.set("")
        direccion_p.set("")

    #final
    botones=Frame(root,width=10,height=20)
    botones.pack(fill="y")
    Guardar=Button(botones,command=save,text="Guardar",background="gray",relief=FLAT)
    Guardar.grid(row=1,column=1)
    Cancelar=Button(botones,command=cancelar,text="Cancelar",background="white",relief=FLAT)
    Cancelar.grid(row=1,column=2)
    Buscar=Button(botones,text="Buscar",background="gray",relief=FLAT)
    Buscar.grid(row=1,column=20)
    botones.config(bd=5)
    botones.config(relief="groove")
    botones.config(cursor="hand2")

    


    #mainloop
    root.mainloop()
