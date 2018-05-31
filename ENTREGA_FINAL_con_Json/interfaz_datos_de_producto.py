#import proveedores

import tkinter

from tkinter import *

class ventanadatosproducto():

    def __init__(self,master,producto,idnt,fecha,precio):
        self.producto=producto
        self.idnt=idnt
        self.fecha=fecha
        self.precio=precio

        self.master=master
        self.master.title("Datos de producto")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="Datos de producto",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
        
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="x")
        #Dato producto
        self.etiqueta_producto=Label(self.cuerpo,text="Producto:")
        self.etiqueta_producto.grid(row=2,column=1,sticky="e",padx=10,pady=5)        
        self.etiqueta_producto=Label(self.cuerpo,text=self.producto)
        self.etiqueta_producto.grid(row=2,column=2,sticky="e",padx=10,pady=5)
        #Dato identificador
        self.etiqueta_producto=Label(self.cuerpo,text="ID:")
        self.etiqueta_producto.grid(row=3,column=1,sticky="e",padx=10,pady=5)        
        self.etiqueta_idnt=Label(self.cuerpo,text=self.idnt)
        self.etiqueta_idnt.grid(row=3,column=2,sticky="e",padx=10,pady=5)
        #Dato fecha
        self.etiqueta_producto=Label(self.cuerpo,text="Fecha:")
        self.etiqueta_producto.grid(row=4,column=1,sticky="e",padx=10,pady=5)        
        self.etiqueta_fecha=Label(self.cuerpo,text=self.fecha)
        self.etiqueta_fecha.grid(row=4,column=2,sticky="e",padx=10,pady=5)
        #Dato precio
        self.etiqueta_producto=Label(self.cuerpo,text="Precio:")
        self.etiqueta_producto.grid(row=5,column=1,sticky="e",padx=10,pady=5)        
        self.etiqueta_precio=Label(self.cuerpo,text=self.precio)
        self.etiqueta_precio.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        

        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Aceptar=Button(self.botones,command=self.aceptar,text="Aceptar",background="white",relief=FLAT)
        self.Aceptar.grid(row=1,column=2)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")

        

    
    def aceptar(self):
        
        pass
    


    
def main():
    root=Tk()
    ventana=ventanadatosproducto(root)
    root.mainloop()

if __name__ == '__main__':
    main()

