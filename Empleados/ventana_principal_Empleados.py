import tkinter 
import interfaz_contratacion_empleados
#import interfaz_buscar_proveedores_conexion

from tkinter import *

class Principal():

    def __init__(self,master):
        self.master=master
        self.master.title("Recursos Humanos")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="Menu Recursos humanos",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo2=Label(self.titulo,text="Que desea hacer?",font=(80))
        self.titulo2.grid(row=2,column=1)
        self.titulo.config(bd=10)
        self.titulo.config(relief="groove")

        self.boton=Frame(self.master,width=500,height=400)
        self.boton.pack(fill="y")
        self.Agregar=Button(self.boton,command=self.save,text="Contratacion",background="white")
        self.Agregar.grid(row=3,column=1)
        self.Buscar=Button(self.boton,command=self.load,text="Busqueda",background="white")
        self.Buscar.grid(row=3,column=5)
        self.Pedido=Button(self.boton,text="Edicion",background="white")
        self.Pedido.grid(row=4,column=1)
        self.Fecha=Button(self.boton,text="Retiro",background="white")
        self.Fecha.grid(row=4,column=5)

    def save(self):

        root2=Toplevel(self.master)
        guar=interfaz_contratacion_empleados.ventanaguardar(root2)
        

    def load(self):
        root3=Toplevel(self.master)
        car=interfaz_buscar_proveedores_conexion.ventanabuscar(root3)
        


def main():
    root=Tk()
    ventana=Principal(root)
    root.mainloop()

if __name__ == '__main__':
    main()
