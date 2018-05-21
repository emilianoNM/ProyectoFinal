import proveedores

import tkinter

from tkinter import *

def ventanabuscar():
    root=Tk()
    #root.geometry("500x300+100+100")
    root.title('Proveedores')
    #Titulo
    titulo=Frame(root,width=500,height=400)
    titulo.pack(fill="y")
    titulo1=Label(titulo,text="BUSCAR PROVEEDORES",font=(80))
    titulo1.grid(row=1,column=1)
    titulo1.config(bd=10)
    titulo1.config(relief="groove")

    titulo2=Label(titulo,text="Elige un dato para buscar",font=(80))
    titulo2.grid(row=2,column=1)
    titulo2.config(bd=10)
    titulo2.config(relief="groove")
    
    #ventana
    Vetana=Frame(root,width=500,height=400)
    Vetana.pack(fill="y")
    Vetana.config(relief="groove")

    var=StringVar()
    var.set('Elige un dato')
    opciones=['Numero Proveedor','Nombre Proveedor','Razon Social','Correo']
    opciones=OptionMenu(Vetana,var,*opciones)
    opciones.config(background="white")
    opciones.grid(row=1,column=1)

    stropcion=var.get()
    
    #Abrimos cuerpo
    cuerpo=Frame(root,width=500,height=400)
    cuerpo.pack(fill="x")
    etiqueta_prueba=Label(cuerpo,text=stropcion)
    etiqueta_prueba.grid(row=1,column=1,sticky="e",padx=10,pady=5)
    prueba=StringVar()
    prueba_entry=Entry(cuerpo,textvariable=prueba)
    prueba_entry.grid(row=1,column=2,sticky="e",padx=10,pady=5)

    def loadex():
        strprueba=prueba.get()
        print(strprueba)
    
    #numero del proveedor
    if stropcion in ("Numero Proveedor"):
        etiqueta_numerop=Label(cuerpo,text="Ingresa Numero Proveedor:")
        etiqueta_numerop.grid(row=2,column=1,sticky="e",padx=10,pady=5)
        numero_p=StringVar()
        numero_entry=Entry(cuerpo,textvariable=numero_p)
        numero_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
    #nombre del proveedor
    if stropcion in ("Nombre Proveedor"):
        etiqueta_nombre=Label(cuerpo,text="Ingresa Nombre Proveedor:")
        etiqueta_nombre.grid(row=2,column=1,sticky="e",padx=10,pady=5)
        nombre_p=StringVar()
        nombre_entry=Entry(cuerpo,textvariable=nombre_p)
        nombre_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
    #Razon Social
    if stropcion in ("Razon Social"):
        etiqueta_rs=Label(cuerpo,text="Ingresa Razon Social: ")
        etiqueta_rs.grid(row=5,column=1,sticky="e",padx=10,pady=5)
        razon_social=StringVar()
        rs_entry=Entry(cuerpo,textvariable=razon_social)
        rs_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
    #Correo
    if stropcion in ("Correo"):
        etiqueta_correo=Label(cuerpo,text="Ingresa Correo: ")
        etiqueta_correo.grid(row=7,column=1,sticky="e",padx=10,pady=5)
        correo_p=StringVar()
        correo_entry=Entry(cuerpo,textvariable=correo_p)
        correo_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)

    def load():

        #numero del proveedor
        if stropcion in ("Numero Proveedor"):
            strNumero=numero_p.get()
            nombrep_buscado=proveedores.Proveedores.load(strNumero)
            print (nombrep_buscado)
        #nombre del proveedor
        if stropcion in ("Nombre Proveedor"):
            strNombre=nombre_p.get()
            nombrep_buscado=proveedores.Proveedores.load(strNombre)
            print (nombrep_buscado)
        #Razon Social
        if stropcion in ("Razon Social"):
            strRs=razon_social.get()
            nombrep_buscado=proveedores.Proveedores.load(strRs)
            print (nombrep_buscado)
        #Correo
        if stropcion in ("Correo"):
            strCorreo=correo_p.get()
            nombrep_buscado=proveedores.Proveedores.load(strCorreo)
            print (nombrep_buscado)

    def cancelar():
        root.destroy()

    #final
    botones=Frame(root,width=10,height=20)
    botones.pack(fill="y")

    BuscarEx=Button(botones,command=loadex,text="Buscar",background="gray",relief=FLAT)
    BuscarEx.grid(row=1,column=1)

    #Buscar=Button(botones,command=load,text="Buscar",background="gray",relief=FLAT)
    #Buscar.grid(row=1,column=1)
    Cancelar=Button(botones,command=cancelar,text="Cancelar",background="white",relief=FLAT)
    Cancelar.grid(row=1,column=2)
    botones.config(bd=5)
    botones.config(relief="groove")
    botones.config(cursor="hand2")

    #mainloop
    root.mainloop()
