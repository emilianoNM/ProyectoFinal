from tkinter import *

from update import database1
from add_to_db import Database
#import RegistroNuevo
#import ListProd

productos1=Tk()

productos1.title("Registro de productos ü")
productos = Frame(height=150,width=250)
productos.pack()
productos = Label(text="PRODUCTOS").place(x=95,y=15)
        
productos= Label(text="Puedes seleccionar un producto de la lista \n o agregar uno nuevo").place(x=5,y=40)

lista = Button(productos,text="Lista",command=actual).place(x=35,y=80)
nuevo = Button(productos,text="Nuevo",command=nuevo).place(x=155,y=80)

def actual(self):
                 n=Toplevel(self.master)
                 n.title("Actualiza la base de datos")
                 n.geometry("1300x900")
                 database1(n)
                
def nuevo(self):
                u=Toplevel(self.master)
                u.title("Agregar a la base de datos")
                u.geometry("1300x900")
                Database(u)

productos1.mainloop()
#Database().mainloop()
#database1().mainloop()

