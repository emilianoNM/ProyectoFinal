from tkinter import *
from tkinter import messagebox
import json
import random
from datetime import datetime
import Suministros
import pedidos
import Hacer_pedidos_conexion
import random



#importar el documento del json
class Principal():
 
  def __init__(self,master):

    self.lista = []
    self.Idd = StringVar()
    self.nombrre_p = StringVar()
    self.pprecio = StringVar()
    self.num_pe=StringVar()
    self.cstock = StringVar()
    self.provee= StringVar()
    self.fentrega = StringVar()
    
    self.stock = 10
	  
    self.master=master
    self.master.title("Productos y Facturas")
    colorFondo = "#B22222"
    colorLetra = "#FFF"
    
    self.ventana=Frame(self.master,width=1000,height=600)
    self.ventana.configure(background = colorFondo)
    self.ventana.pack()
    self.etiquetaTitulo = Label(self.ventana, text="INGRESA EL ID DEL PRODUCTO",bg=colorFondo,fg=colorLetra)
    self.etiquetaTitulo.grid(row=1,column=1)
    self.etiquetaID = Label(self.ventana, text="ID",bg=colorFondo,fg=colorLetra)
    self.etiquetaID.grid(row=2,column=1)
    self.cajaID = Entry(self.ventana, textvariable=self.Idd)
    self.cajaID.grid(row=2,column=2)

    self.etiquetaNum = Label(self.ventana, text="NUMERO DE PEDIDO", bg=colorFondo,fg=colorLetra)
    self.etiquetaNum.grid(row=3,column=1)
    self.cajaNum = Entry(self.ventana, textvariable=self.num_pe)
    self.cajaNum.grid(row=3,column=2)
    
    self.etiquetaNom = Label(self.ventana, text="NOMBRE", bg=colorFondo,fg=colorLetra)
    self.etiquetaNom.grid(row=4,column=1)
    self.cajaNom = Entry(self.ventana, textvariable=self.nombrre_p)
    self.cajaNom.grid(row=4,column=2)
   
    self.etiquetaPrec= Label(self.ventana, text="PRECIO", bg=colorFondo,fg=colorLetra)
    self.etiquetaPrec.grid(row=5,column=1)
    self.cajaPrec = Entry(self.ventana, textvariable=self.pprecio)
    self.cajaPrec.grid(row=5,column=2)
    
    self.etiquetacstock = Label(self.ventana, text="CANTIDAD EN STOCK", bg=colorFondo,fg=colorLetra)
    self.etiquetacstock.grid(row=6,column=1)
    self.cajacstock = Entry(self.ventana, textvariable=self.cstock)
    self.cajacstock.grid(row=6,column=2)
	
    self.etiquetaprovee = Label(self.ventana, text="PROVEEDOR", bg=colorFondo,fg=colorLetra)
    self.etiquetaprovee.grid(row=7,column=1)
    self.cajaprovee = Entry(self.ventana, textvariable=self.provee)
    self.cajaprovee.grid(row=7,column=2)
	
    self.etiquetafentrega = Label(self.ventana, text="FECHA", bg=colorFondo,fg=colorLetra)
    self.etiquetafentrega.grid(row=8,column=1)
    self.cajafentrega = Entry(self.ventana, textvariable=self.fentrega)
    self.cajafentrega.grid(row=8,column=2)

    self.botoGuardar = Button(self.ventana, text="Pedir", command=self.guardar, bg="#009",fg="white")
    self.botoGuardar.grid(row=9,column=3)
    self.botoPedir = Button(self.ventana, text="Realizar Pedido mayor a Stock", command=self.pedir, bg="#009",fg="white")
    self.botoPedir.grid(row=9,column=1)
    self.boton3=Button (self.ventana,text="Salir",fg="red",command=self.salir)
    self.boton3.grid(row=10,column=2)

    
    self.iniciarArchivo()
	
  def guardar(self):
    self.cargarDato()

    self.srtIdd=self.Idd.get()
    self.nom=self.nombrre_p.get()
    self.precc=self.pprecio.get()
    self.csto=self.cstock.get()
    self.prov=self.provee.get()
    self.ent=self.fentrega.get()
    self.nup=self.num_pe.get()

    
    self.lista.append(self.srtIdd+"-"+self.nom+"-"+self.precc+"-"+self.csto+"-"+self.prov+"-"+self.ent+"-")

    a=Suministros.Suministros(self.srtIdd,self.nom,self.precc,self.csto,self.prov,self.ent)
    a.save()

    b=pedidos.Pedidos(self.nup,self.srtIdd,self.nom,self.precc,self.prov,self.ent)
    b.savei()

    self.escribirContacto()

    idd=int(self.csto)
    if idd <= 0:
      removido=messagebox.askyesno("ALTO","Suministros Agotados ¿Desea hacer un pedido?")
      if removido==True:
        self.pedir()
          
  def pedir(self):
    root2=Toplevel(self.master)
    ped=Hacer_pedidos_conexion.pedido(root2)
    self.stock=10
    self.cstock.set(self.stock)
      
  def iniciar(self):
      self.stock=10

  def iniciarArchivo(self):
      archivo = open("Facturaas.txt","a")
      archivo.close()

  def escribirContacto(self):
      archivo = open("Facturaas.txt","w")
      for elemento in self.lista:
        archivo.write(elemento+"\n")
      archivo.close()

  def salir(self):   
      sal=messagebox.askyesno("Salir","¿Seguro que deseas salir?")
      if sal==True:
        quit()
		   
  def cargarDato(self):
      jsonobj={}
      f=open("Productos.dat","r")
      productos=f.read()
      jsonobj=json.loads(productos)

      sonobj={}
      f=open("Suministros.dat","r")
      productos=f.read()
      sonobj=json.loads(productos)

      datoDeVariable=self.Idd.get()
      for num in jsonobj:
        encontradon=0
        datocom=jsonobj[num]['ID']
        if datoDeVariable==datocom:
          self.nombrre_p.set(jsonobj[num]['nombre'])
          self.pprecio.set(jsonobj[num]['precio'])
          self.provee.set(jsonobj[num]['proveedor'])
          self.stock=self.stock-1
          self.cstock.set(self.stock)
          self.agregarpedido()
          encontradon=encontradon+1
          self.agregarfechaex()
          return
      if encontradon==0:
            messagebox.showinfo("Error","El ID "+self.Idd.get()+" no fue encontrado, intente de nuevo")
      pass

  def agregarfechaex(self):
      inicio = datetime(2018, 6, 30)
      final =  datetime(2018, 12, 28)
      random_date = inicio + (final - inicio) * random.random()
      print(random_date)
      self.fentrega.set(random_date)

  def agregarpedido(self):
      self.num_pe.set(int(random.randrange(100000)))
      
def main():
    root=Tk()
    ventana=Principal(root)
    root.mainloop()

if __name__ == '__main__':
      main()
