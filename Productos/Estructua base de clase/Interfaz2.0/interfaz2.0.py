#Avance interfaz 2.0

from tkinter import *

class main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master.title("Busqueda de Productos ü")
        self.master.geometry("400x250")
        bienvenida=Label(text="BUSQUEDA DE PRODUCTO").place(x=120,y=0)
      

        var = IntVar()
        R1 = Radiobutton(root, text="1) Por producto", variable=var, value=1).place(x=5,y=15)
        #R1.pack( anchor = W )

        R2 = Radiobutton(root, text="2) Por precio", variable=var, value=2).place(x=5,y=35)
        #R2.pack( anchor = W )

        R3 = Radiobutton(root, text="3) Por fecha de caducidad", variable=var, value=3).place(x=5,y=55)
        #R3.pack( anchor = W)
        

        Prod = Label(text="Producto").place(x=5,y=90)
        entrada=StringVar()
        Campop=Entry(master,textvariable=entrada,width=40).place(x=60,y=90)
        boton1=Button(master,text="Buscar").place(x=310,y=90)

        Nombre=Label(text="Producto").place(x=5,y=120)
        entrada2=StringVar()
        Campon=Entry(master,textvariable=entrada2,width=13).place(x=5,y=145)
        
        Precio=Label(text="Precio").place(x=100,y=120)
        entrada3=StringVar()
        Campor=Entry(master,textvariable=entrada3,width=13).place(x=100,y=145)
        
        Cantidad=Label(text="Cantidad").place(x=200,y=120)
        entrada4=StringVar()
        Campoa=Entry(master,textvariable=entrada4,width=13).place(x=200,y=145)
        
        Caducidad=Label(text="Caducidad").place(x=300,y=120)
        entrada5=StringVar()
        Campod=Entry(master,textvariable=entrada5,width=13).place(x=300,y=145) 
    
        
root=Tk()
a=main(root)
label = Label(root)
#label.pack()
root.mainloop()
        
