import tkinter 
import interfaz_guardar_proveedores_conexion
import guardar_productos

from tkinter import *

class Principal():

    def __init__(self,master):
        self.master=master
        self.master.title("Proveedores")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="MENU PROVEEDORES",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo2=Label(self.titulo,text="ELIGE UNA OPCIÓN",font=(80))
        self.titulo2.grid(row=2,column=1)
        self.titulo.config(bd=10)
        self.titulo.config(relief="groove")

        self.boton=Frame(self.master,width=500,height=400)
        self.boton.pack(fill="y")
        self.Agregar=Button(self.boton,command=self.save,text="Agregar Proveedor",background="white")
        self.Agregar.grid(row=3,column=1)
        self.Pedido=Button(self.boton,command=self.prod,text="Agregar Producto",background="white")
        self.Pedido.grid(row=3,column=2)

    def save(self):

        root2=Toplevel(self.master)
        guar=interfaz_guardar_proveedores_conexion.ventanaguardar(root2)
        

    def load(self):
        root3=Toplevel(self.master)
        car=interfaz_buscar_proveedores_conexion.ventanabuscar(root3)

    def prod(self):

        root4=Toplevel(self.master)
        prodd=guardar_productos.agregarproducto(root4)
        


def main():
    root=Tk()
    ventana=Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
