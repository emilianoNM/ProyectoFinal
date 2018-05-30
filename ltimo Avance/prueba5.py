from tkinter import *
from tkinter import messagebox
import json

class Principal:
 
  def __init__(self,master):

    self.lista = []
    self.mystring1 = StringVar()
    self.mystring2 = StringVar()
    self.mystring3 = StringVar()
    self.mystring4 = StringVar()
    self.nombre = StringVar()
    self.apellidos = StringVar()
    self.rfc = StringVar()
    self.correo = StringVar()
    self.telefono = StringVar()
    self.conteliminar = StringVar()
	  
    self.master=master
    self.master.title("Facturas")
    colorFondo = "#B22222"
    colorLetra = "#FFF"
    
    self.ventana=Frame(self.master,width=1000,height=600)
    self.ventana.configure(background = colorFondo)
    self.ventana.pack()
    self.etiquetaTitulo = Label(self.ventana, text="Datos del cliente",bg=colorFondo,fg=colorLetra)
    self.etiquetaTitulo.grid(row=1,column=1)
    self.etiquetaN = Label(self.ventana, text="ID",bg=colorFondo,fg=colorLetra)
    self.etiquetaN.grid(row=2,column=1)
    self.cajaN = Entry(self.ventana, textvariable=self.mystring1)
    self.cajaN.grid(row=2,column=2)
    self.etiquetaApp = Label(self.ventana, text="NOMBRE", bg=colorFondo,fg=colorLetra)
    self.etiquetaApp.grid(row=3,column=1)
    self.cajaApp = Entry(self.ventana, textvariable=self.mystring2)
    self.cajaApp.grid(row=3,column=2)
    self.etiquetaRFC = Label(self.ventana, text="PRECIO", bg=colorFondo,fg=colorLetra)
    self.etiquetaRFC.grid(row=4,column=1)
    self.cajaRFC = Entry(self.ventana, textvariable=self.mystring3)
    self.cajaRFC.grid(row=4,column=2)
    self.etiquetaT = Label(self.ventana, text="CANTIDAD", bg=colorFondo,fg=colorLetra)
    self.etiquetaT.grid(row=5,column=1)
    self.cajaT = Entry(self.ventana, textvariable=self.mystring4)
    self.cajaT.grid(row=5,column=2)

    self.botoingresa=Button(self.ventana, text="Ingresar informacion",command=lambda:self.cargarDato(), bg="#009",fg="white")
    self.botoingresa.grid(row=7,column=3)
    self.botoGuardar = Button(self.ventana, text="Guardar", command=self.guardar, bg="#009",fg="white")
    self.botoGuardar.grid(row=6,column=2)
    self.botoEliminar = Button(self.ventana, text="Eliminar",command=self.eliminar, bg="#009",fg="white")
    self.botoEliminar.grid(row=2,column=10)
    self.boton3=Button (self.ventana,text="Salir",fg="red",command=self.salir)
    self.boton3.grid(row=7,column=1)
    
    self.iniciarArchivo()
    self.consultar()

  def guardar(self):
    self.cargarDato()
    
    n = self.mystring1.get()
    ap = self.mystring2.get()
    rf = self.mystring3.get()
    c = self.correo.get()
    t = self.mystring4.get()
    
    self.lista.append(n+"-"+ap+"-"+rf+"-"+t+"-"+c)
    self.escribirContacto()
    
    messagebox.showinfo("Guardado","Los datos del cliente han sido guardados con exito")
    
    self.nombre.set("")
    self.apellidos.set("")
    self.rfc.set("")
    self.correo.set("")
    self.telefono.set("")
    self.consultar()

  def eliminar(self):
      eliminado = self.conteliminar.get()
      removido = False

      for elemento in self.lista:
        arreglo = elemento.split("-")
        if self.conteliminar.get() == arreglo[0]:
          removido=messagebox.askyesno("Eliminar","¿Seguro que deseas eliminar?")
          self.lista.remove(elemento)
          removido = True
      self.escribirContacto()
      self.consultar()
      if removido:
        messagebox.showinfo("Eliminar",eliminado+" ha sido eliminado")

  def consultar(self):
      r = Text(self.ventana, width=85, height=15)
      self.lista.sort()
      valores = []
      r.insert(INSERT, "ID\t\tNombre\t\tPrecio\t\tCantidad\t\n")
      for elemento in self.lista:
        arreglo = elemento.split("-")
        valores.append(arreglo[0])
        r.insert(INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
      r.place(x=20,y=250)
      self.spinNombre = Spinbox(self.ventana, value=(valores),textvariable=self.conteliminar).place(x=500,y=50)
      if self.lista ==[]:
        self.spinNombre = Spinbox(self.ventana, value=(valores)).place(x=500,y=50)
      r.config(state=DISABLED)

  def iniciarArchivo(self):
      archivo = open("Facturaas.txt","a")
      archivo.close()

  def escribirContacto(self):
      archivo = open("Facturaas.txt","w")
      self.lista.sort()
      for elemento in self.lista:
        archivo.write(elemento+"\n")
      archivo.close()

  def salir(self):   
      sal=messagebox.askyesno("Salir","¿Seguro que deseas salir?")
      if sal==True:
        quit()
		   
  def cargarDato(self):
      #read productos
      f=open("productos.json","r")
      productos=f.read()
      jsonobj=json.loads(productos)
      #jsonobj={"1":"dato", "2":"info" }
      datoDeVariable=self.mystring1.get()
      self.mystring2.set(jsonobj[datoDeVariable][0])
      self.mystring3.set(jsonobj[datoDeVariable][1])
      self.mystring4.set(jsonobj[datoDeVariable][2])
      pass

def main():
    root=Tk()
    ventana=Principal(root)
    root.mainloop()

if __name__ == '__main__':
      main()
