import proveedores
import guardar_productos

import tkinter

from tkinter import *

class ventanaguardar():

    def __init__(self,master):
        self.numero_p=StringVar()
        self.nombre_p=StringVar()
        self.razon_social=StringVar()
        self.telefono_p=StringVar()
        self.correo_p=StringVar()
        self.direccion_p=StringVar()

        self.master=master
        self.master.title("Proveedores")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="AGREGAR PROVEEDOR",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
        #numero del proveedor
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="x")
        self.etiqueta_numerop=Label(self.cuerpo,text="Numero Proveedor:")
        self.etiqueta_numerop.grid(row=2,column=1,sticky="e",padx=10,pady=5)
        self.numero_entry=Entry(self.cuerpo,textvariable=self.numero_p)
        self.numero_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
        #nombre del proveedor
        self.etiqueta_nombre=Label(self.cuerpo,text="Nombre Proveedor:")
        self.etiqueta_nombre.grid(row=3,column=1,sticky="e",padx=10,pady=5)
        self.nombre_entry=Entry(self.cuerpo,textvariable=self.nombre_p)
        self.nombre_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
        #Razon Social
        self.etiqueta_rs=Label(self.cuerpo,text="Razon Social: ")
        self.etiqueta_rs.grid(row=5,column=1,sticky="e",padx=10,pady=5)
        self.rs_entry=Entry(self.cuerpo,textvariable=self.razon_social)
        self.rs_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        #Télefono
        self.etiqueta_telefono=Label(self.cuerpo,text="Telefono: ")
        self.etiqueta_telefono.grid(row=6,column=1,sticky="e",padx=10,pady=5)
        self.telefono_entry=Entry(self.cuerpo,textvariable=self.telefono_p)
        self.telefono_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
        #Correo
        self.etiqueta_correo=Label(self.cuerpo,text="Correo: ")
        self.etiqueta_correo.grid(row=7,column=1,sticky="e",padx=10,pady=5)
        self.correo_entry=Entry(self.cuerpo,textvariable=self.correo_p)
        self.correo_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)
        #Direccion
        self.etiqueta_d=Label(self.cuerpo,text="Dirección: ")
        self.etiqueta_d.grid(row=8,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.direccion_p)
        self.direccion_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)

        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Guardar=Button(self.botones,command=self.save,text="Guardar",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.Cancelar=Button(self.botones,command=self.cancelar,text="Cancelar",background="white",relief=FLAT)
        self.Cancelar.grid(row=1,column=2)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")

    def save(self):
        print(self.numero_p.get())
        strNumero=self.numero_p.get()
        strNombre=self.nombre_p.get()
        strRs=self.razon_social.get()
        strTelefono=self.telefono_p.get()
        strCorreo=self.correo_p.get()
        strDir=self.direccion_p.get()

        a=proveedores.Proveedores(strNumero,strNombre,strRs,strTelefono,strCorreo,strDir)
        a.save()
        
        self.numero_p.set("")
        self.nombre_p.set("")
        self.razon_social.set("")
        self.telefono_p.set("")
        self.correo_p.set("")
        self.direccion_p.set("")
        pass
    
    def cancelar(self):
        self.numero_p.set("")
        self.nombre_p.set("")
        self.razon_social.set("")
        self.telefono_p.set("")
        self.correo_p.set("")
        self.direccion_p.set("")
        pass

    


    
def main():
    root=Tk()
    ventana=ventanaguardar(root)
    root.mainloop()

if __name__ == '__main__':
    main()

