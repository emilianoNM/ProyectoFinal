
import ClienteFacturas
from tkinter import *
from tkinter import messagebox

def imprime():
    messagebox.showinfo("Mensaje","La factura se imprimirá enseguida") 

def save():
    print(nombre.get())
    strNombre=nombre.get()
    Clientes.load() 
    a=Clientes.Clientes(StrNombre)
    a.save()

    messagebox.showinfo("Mensaje","La factura se guardó con éxito")

def salir():   
    sal=messagebox.askyesno("Salir","¿Seguro que deseas salir?")
    if sal==True:
       quit() 
                      
ventana = Tk()
nombre=StringVar()
numfactura=IntVar() 
fecha=StringVar()
rfc=StringVar()
direccion=StringVar()
correo=StringVar()
telefono=StringVar()
nombre.set("Escribre el nombre ")
#colorFondo="#CD5C5C"
ventana.title("Facturas")
ventana.geometry("600x400")
#ventana.configure(background=colorFondo)


etiqueta1=Label(ventana,text="Número de factura:").place(x=10,y=20)
numfacturacaja=Entry(ventana,textvariable=numfactura).place(x=130,y=20)

etiqueta2=Label(ventana,text="Fecha:").place(x=310,y=20)
fechacaja=Entry(ventana,textvariable=fecha).place(x=370,y=20)

etiqueta3=Label(ventana,text="Nombre:").place(x=10,y=50)
nombrecaja=Entry(ventana,textvariable=nombre).place(x=130,y=50)

etiqueta4=Label(ventana,text="RFC:").place(x=310,y=50)
RFCcaja=Entry(ventana,textvariable=rfc).place(x=370,y=50)

etiqueta5=Label(ventana,text="Dirección:").place(x=10,y=80)
direccioncaja=Entry(ventana,textvariable=direccion).place(x=130,y=80)

etiqueta6=Label(ventana,text="Teléfono:").place(x=310,y=80)
telefonocaja=Entry(ventana,textvariable=telefono).place(x=370,y=80)

etiqueta7=Label(ventana,text="Correo:").place(x=10,y=110)
correocaja=Entry(ventana,textvariable=correo).place(x=130,y=110)


boton1=Button (ventana, text= "Imprimir",fg="blue",command=imprime).place(x=10,y=350)
boton2=Button (ventana,text="Guardar",command=save).place(x=260,y=350)
boton3=Button (ventana,text="Salir",fg="red",command=salir).place(x=470,y=350)
ventana.mainloop()
