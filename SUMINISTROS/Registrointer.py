from tkinter import *

interfaz=Tk()

interfaz.title("Inventario")

inventario = Frame(height=300,width=550)
inventario.pack()
inventario = Label(text="Registro de suminsitro", font=(16)).place(x=185,y=15)

nombre = Label(text="Nombre").place(x=0,y=50)
producto= StringVar()
Campo = Entry(inventario,textvariable=producto).place(x=140,y=50)


regsitro = Label(text="No de registro").place(x=0,y=80)
codigo=StringVar()
Campo = Entry(inventario,textvariable=codigo).place(x=140,y=80)

localizacion=Label(text="Localizacion en almacen").place(x=0,y=110)
localizacion=StringVar()
Campo = Entry(inventario,textvariable=localizacion).place(x=140,y=110)


precio=Label(text="Precio del provedor").place(x=250,y=50)
precio=StringVar()
Campo = Entry(inventario,textvariable=precio).place(x=380,y=50)

provedor=Label(text="Provedor").place(x=250,y=80)
provedor=StringVar()
Campo = Entry(inventario,textvariable=provedor).place(x=380,y=80)

cantidad=Label(text="Cantidad en existencia").place(x=250,y=110)
cantidad=StringVar()
Campo = Entry(inventario,textvariable=cantidad).place(x=380,y=110)

def registro():
    print(producto.get())
    print(codigo.get())
    print(localizacion.get())
    print(cantidad.get())
    print(precio.get())
    print(provedor.get())
    strNombre=producto.get()
boton1 = Button(inventario,text="Registrar",command=registro).place(x=180,y=150)
def borrar():
    producto.set("")
    codigo.set("")
    localizacion.set("")
    cantidad.set("")
    precio.set("")
    provedor.set("")
boton2 = Button(inventario,text="Borrar",command=borrar).place(x=330,y=150)
               

interfaz.mainloop()
