import pedidos
import ventana_principal_botones

import tkinter

from tkinter import *

class pedido():
    def __init__(self,master):
        self.numeroped=StringVar()
        self.nombrepro=StringVar()
        self.cantidadpro=StringVar()
        self.direccion_p=StringVar()
        self.iddd=StringVar()

        
        self.master=master
        self.master.title('Realiza Pedido')
        
        #Titulo
        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="PEDIDOS",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
        #numero del pedido
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="y")
        self.etiqueta_numerop=Label(self.cuerpo,text="Numero de pedido:")
        self.etiqueta_numerop.grid(row=2,column=1,sticky="e",padx=10,pady=5)
        self.numeroped_entry=Entry(self.cuerpo,textvariable=self.numeroped)
        self.numeroped_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
        #ID del producto
        self.etiqueta_dd=Label(self.cuerpo,text="ID: ")
        self.etiqueta_dd.grid(row=3,column=1,sticky="e",padx=10,pady=5)
        self.dd_entry=Entry(self.cuerpo,textvariable=self.iddd)
        self.dd_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
        #nombre del producto
        self.etiqueta_np=Label(self.cuerpo,text="Nombre Producto:")
        self.etiqueta_np.grid(row=3,column=3,sticky="e",padx=10,pady=5)
        self.np_entry=Entry(self.cuerpo,textvariable=self.nombrepro)
        self.np_entry.grid(row=3,column=4,sticky="e",padx=10,pady=5)
        #Cantidad
        self.etiqueta_c=Label(self.cuerpo,text="Cantidad: ")
        self.etiqueta_c.grid(row=8,column=1,sticky="e",padx=10,pady=5)
        self.cantidad_entry=Entry(self.cuerpo,textvariable=self.cantidadpro)
        self.cantidad_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)
        #Precio
        self.etiqueta_p=Label(self.cuerpo,text="Precio: ")
        self.etiqueta_p.grid(row=8,column=3,sticky="e",padx=10,pady=5)
        self.precio_entry=Entry(self.cuerpo,textvariable=self.cantidadpro)
        self.precio_entry.grid(row=8,column=4,sticky="e",padx=10,pady=5)
        
        #Segunda seccion
        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Guardar=Button(self.botones,command=self.save,text="Generar Pedido",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")


        #Seccion Buscar
        self.cuerpo2=Frame(self.master,width=500,height=400)
        self.cuerpo2.pack(fill="y")
        self.proveedor=Label(self.cuerpo2,text="Proveedor: ")
        self.proveedor.grid(row=5,column=1,sticky="e",padx=10,pady=5)
        self.proveedors=StringVar()
        self.pe_entry=Entry(self.cuerpo2,textvariable=self.proveedors)
        self.pe_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        #Repartidor
        self.repartidore=Label(self.cuerpo2,text="Repartidor: ")
        self.repartidore.grid(row=6,column=1,sticky="e",padx=10,pady=5)
        self.repartidores=StringVar()
        self.repartidor_entry=Entry(self.cuerpo2,textvariable=self.repartidores)
        self.repartidor_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
        #Télefono
        self.etiqueta_telefono=Label(self.cuerpo2,text="Telefono: ")
        self.etiqueta_telefono.grid(row=5,column=3,sticky="e",padx=10,pady=5)
        self.telefono_p=StringVar()
        self.telefono_entry=Entry(self.cuerpo2,textvariable=self.telefono_p)
        self.telefono_entry.grid(row=5,column=4,sticky="e",padx=10,pady=5)
        #Correo
        self.etiqueta_correo=Label(self.cuerpo2,text="Correo: ")
        self.etiqueta_correo.grid(row=6,column=3,sticky="e",padx=10,pady=5)
        self.correo_p=StringVar()
        self.correo_entry=Entry(self.cuerpo2,textvariable=self.correo_p)
        self.correo_entry.grid(row=6,column=4,sticky="e",padx=10,pady=5)
        #Fecha de entrega
        self.fecha_entrega=Label(self.cuerpo2,text="Fecha de entrega: ")
        self.fecha_entrega.grid(row=7,column=2,sticky="e",padx=10,pady=5)
        self.entrega_p=StringVar()
        self.entrega_entry=Entry(self.cuerpo2,textvariable=self.entrega_p)
        self.entrega_entry.grid(row=7,column=3,sticky="e",padx=10,pady=5)

        self.boton=Frame(self.master,width=10,height=20)
        self.boton.pack(fill="y")
        self.Guardar=Button(self.boton,text="Buscar",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.Cancelar=Button(self.boton,command=self.cancelar,text="Cancelar",background="white",relief=FLAT)
        self.Cancelar.grid(row=1,column=3)
        self.Cancelar=Button(self.boton,command=self.Prov,text="Ingresar a Proveedores",background="white",relief=FLAT)
        self.Cancelar.grid(row=2,column=2)
        self.boton.config(bd=5)
        self.boton.config(relief="groove")
        self.boton.config(cursor="hand2")


    def save(self):
        print(self.numeroped.get())
        strNumerop=self.numeroped.get()
        strNombrep=self.nombrepro.get()
        strCantidadp=self.cantidadpro.get()
        strDirp=self.direccion_p.get()
            
        a=pedidos.Pedidos(strNumerop,strNombrep,strCantidadp,strDirp)
        a.savepr()
        
        self.numeroped.set("")
        self.nombrepro.set("")
        self.cantidadpro.set("")
        self.direccion_p.set("")

        self.proveedors.set("")
        self.repartidores.set("")
        self.telefono_p.set("")
        self.correo_p.set("")
        self.entrega_p.set("")

    def cancelar(self):
        self.numeroped.set("")
        self.nombrepro.set("")
        self.cantidadpro.set("")
        self.direccion_p.set("")

        self.proveedors.set("")
        self.repartidores.set("")
        self.telefono_p.set("")
        self.correo_p.set("")
        self.entrega_p.set("")

    def Prov(self):
        root4=Toplevel(self.master)
        buy=ventana_principal_botones.Principal(root4)
        

def main():
    root=Tk()
    ventana=pedido(root)
    root.mainloop()

if __name__ == '__main__':
    main()
