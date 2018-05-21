from tkinter import *
import ListProd
import RegistroNuevo

productos1=Tk()

productos1.title("Registro de productos ü")
productos = Frame(height=150,width=250)
productos.pack()
productos = Label(text="PRODUCTOS").place(x=95,y=15)
        
productos= Label(text="Puedes seleccionar un producto de la lista \n o agregar uno nuevo").place(x=5,y=40)

boton1 = Button(productos,text="Lista",command=RegistroNuevo.reg).place(x=35,y=80)
boton2 = Button(productos,text="Nuevo",command=ListProd.lista).place(x=155,y=80)


productos1.mainloop()
