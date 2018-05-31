import proveedores
import json
import producto

import tkinter

from tkinter import *
from tkinter import messagebox

class agregarproducto():

    def __init__(self,master):
        self.numero_p=StringVar()
        self.nombre_p=StringVar()
        self.razon_social=StringVar()
        self.telefono_p=StringVar()
        self.correo_p=StringVar()
        self.direccion_p=StringVar()
        self.producto_p=StringVar()

        self.codigopro=StringVar()
        self.fechapro=StringVar()
        self.preciopr=StringVar()

        self.master=master
        self.master.title("Proveedores")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="AGREGAR PRODUCTO",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
        #Instrucciones
        self.instr=Frame(self.master,width=500,height=400)
        self.instr.pack(fill="x")
        self.etiqueta_instr=Label(self.instr,text="Rellena cualquier campo para ubicar el 'Proveedor' junto al 'PRODUCTO' a agregar")
        self.etiqueta_instr.grid(row=1,column=1,sticky="e",padx=10,pady=5)
        #Cuerpo
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="x")
        #numero del proveedor
        self.etiqueta_numerop=Label(self.cuerpo,text="Codigo Proveedor:")
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
        self.rstex=Entry(self.cuerpo,textvariable=self.razon_social)
        self.rstex.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        #Télefono
        self.etiqueta_telefono=Label(self.cuerpo,text="Telefono: ")
        self.etiqueta_telefono.grid(row=6,column=1,sticky="e",padx=10,pady=5)
        self.telefono_entry=Entry(self.cuerpo,textvariable=self.telefono_p)
        self.telefono_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
        #Correo
        self.etiqueta_correo=Label(self.cuerpo,text="Correo: ")
        self.etiqueta_correo.grid(row=7,column=1,sticky="e",padx=10,pady=5)
        self.correotex=Entry(self.cuerpo,textvariable=self.correo_p)
        self.correotex.grid(row=7,column=2,sticky="e",padx=10,pady=5)
        #Direccion
        self.etiqueta_d=Label(self.cuerpo,text="Dirección: ")
        self.etiqueta_d.grid(row=8,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.direccion_p)
        self.direccion_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)
        #Producto
        self.etiqueta_nombrep=Label(self.cuerpo,text="Producto: ")
        self.etiqueta_nombrep.grid(row=9,column=1,sticky="e",padx=10,pady=5)
        self.nombre_entry=Entry(self.cuerpo,textvariable=self.producto_p)
        self.nombre_entry.grid(row=9,column=2,sticky="e",padx=10,pady=5)
        #Codigo del producto
        self.etiqueta_copro=Label(self.cuerpo,text="ID: ")
        self.etiqueta_copro.grid(row=10,column=1,sticky="e",padx=10,pady=5)
        self.codigo_entry=Entry(self.cuerpo,textvariable=self.codigopro)
        self.codigo_entry.grid(row=10,column=2,sticky="e",padx=10,pady=5)
        #Fecha 
        self.etiqueta_fepro=Label(self.cuerpo,text="Fecha: ")
        self.etiqueta_fepro.grid(row=11,column=1,sticky="e",padx=10,pady=5)
        self.fecha_entry=Entry(self.cuerpo,textvariable=self.fechapro)
        self.fecha_entry.grid(row=11,column=2,sticky="e",padx=10,pady=5)
        #Precio
        self.etiqueta_pr=Label(self.cuerpo,text="Precio: ")
        self.etiqueta_pr.grid(row=12,column=1,sticky="e",padx=10,pady=5)
        self.pr_entry=Entry(self.cuerpo,textvariable=self.preciopr)
        self.pr_entry.grid(row=12,column=2,sticky="e",padx=10,pady=5)
        

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
        
        self.strNumero=self.numero_p.get()
        self.strNombre=self.nombre_p.get()
        self.strRs=self.razon_social.get()
        self.strTelefono=self.telefono_p.get()
        self.strCorreo=self.correo_p.get()
        self.strDir=self.direccion_p.get()
        self.strPro=self.producto_p.get()
        
        self.strCodigo=self.codigopro.get()
        self.strFecha=self.fechapro.get()
        self.strPrecio=self.preciopr.get()

        #a=proveedores.Proveedores(strNumero,strNombre,strRs,strTelefono,strCorreo,strDir,strPro)
        #a.proguctog()
        if self.strPro == "":
            messagebox.showinfo("Error","Se necesita agregar un producto")
            self.numero_p.set("")
            self.nombre_p.set("")
            self.razon_social.set("")
            self.telefono_p.set("")
            self.correo_p.set("")
            self.direccion_p.set("")
            self.producto_p.set("")
            pass
        elif self.strNumero != "" and self.strNombre != "":
            messagebox.showinfo("Error","Solo escribre un campo: Codigo o Nombre.")
            self.numero_p.set("")
            self.nombre_p.set("")
            self.razon_social.set("")
            self.telefono_p.set("")
            self.correo_p.set("")
            self.direccion_p.set("")
            self.producto_p.set("")
            pass
        elif self.strRs != "" and self.strTelefono != "" and self.strCorreo != "" and self.strDir != "":
            messagebox.showinfo("Error","Los siguientes campos deben estar vacios: Razon Social, Telefono, Correo o Direccion.")
            self.razon_social.set("")
            self.telefono_p.set("")
            self.correo_p.set("")
            self.direccion_p.set("")
            pass
        elif self.strCodigo == "" or self.strFecha == "" or self.strPrecio == "":
            messagebox.showinfo("Error","Llena todos los campos")
        else: 
            if self.strNumero != "":
                self.cargar1()
            else:
                self.cargar2()
            #self.razon_social.set("1")
            #self.telefono_p.set("2")
            #self.correo_p.set("3")
            #self.direccion_p.set("4")
            #messagebox.showinfo("Guardado","El Producto ha sido guardados con exito")
            #root4=Toplevel(self.master)
            #prodd=detalles_producto.detallespro(root4)
            pass

    def cargar2(self):
        listaJson={}
        lista=open("Proveedores.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        
        NombreProveedor=self.nombre_p.get()
        for codigo in listaJson:
            encontradon=0
            Nombrecompara=listaJson[codigo]['nombre_p']
            if NombreProveedor==Nombrecompara:
                self.numero_p.set(listaJson[codigo]['numero_p'])
                self.razon_social.set(listaJson[codigo]['razon_social'])
                self.telefono_p.set(listaJson[codigo]['telefono_p'])
                self.correo_p.set(listaJson[codigo]['correo_p'])
                self.direccion_p.set(listaJson[codigo]['direccion_p'])
                messagebox.showinfo("Guardado","El Producto "+self.producto_p.get()+" ha sido guardados con exito")
                encontradon=encontradon+1
                self.actualizar()
                return
        if encontradon==0:
            messagebox.showinfo("Error","El Proveedor "+self.nombre_p.get()+" no fue encontrado, intente de nuevo")
            
            
    def cargar1(self):
        listaJson={}
        lista=open("Proveedores.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        print(listaJson)

        CodigoProveedor=self.numero_p.get()
        for nombre in listaJson:
            encontrado=0
            codigocompara=(listaJson[nombre]["numero_p"])
            if CodigoProveedor==codigocompara:
                self.nombre_p.set(listaJson[nombre]['nombre_p'])
                self.razon_social.set(listaJson[nombre]['razon_social'])
                self.telefono_p.set(listaJson[nombre]['telefono_p'])
                self.correo_p.set(listaJson[nombre]['correo_p'])
                self.direccion_p.set(listaJson[nombre]['direccion_p'])
                messagebox.showinfo("Guardado","El Producto "+self.producto_p.get()+" ha sido guardados con exito")
                encontrado=encontrado+1
                self.actualizar()
                return
        if encontrado==0:
            messagebox.showinfo("Error","El Codigo "+self.numero_p.get()+" no fue encontrado, intente de nuevo")
                
                
    
    def cancelar(self):
        self.numero_p.set("")
        self.nombre_p.set("")
        self.razon_social.set("")
        self.telefono_p.set("")
        self.correo_p.set("")
        self.direccion_p.set("")

        self.producto_p.set("")
        self.codigopro.set("")
        self.fechapro.set("")
        self.preciopr.set("")
        pass

    def actualizar(self):
        self.strNumero=self.numero_p.get()
        self.strNombre=self.nombre_p.get()
        self.strRs=self.razon_social.get()
        self.strTelefono=self.telefono_p.get()
        self.strCorreo=self.correo_p.get()
        self.strDir=self.direccion_p.get()
        self.strPro=self.producto_p.get()
        
        self.strCodigo=self.codigopro.get()
        self.strFecha=self.fechapro.get()
        self.strPrecio=self.preciopr.get()
        
        a=producto.Producto(self.strPro,self.strCodigo,self.strFecha,self.strPrecio,self.strNumero,self.strNombre)
        a.save()
        

    
def main():
    root=Tk()
    producto=agregarproducto(root)
    root.mainloop()

if __name__ == '__main__':
    main()

