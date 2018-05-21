from tkinter import *


def reg():
    interfaz=Tk()

    interfaz.title("Registro nuevo ")
    registro = Frame(height=200,width=550)
    registro.pack()
    registro = Label(text="Registro de producto nuevo").place(x=185,y=10)
    
    producto= Label(text="Producto").place(x=0,y=50)
    entrada=StringVar()
    Campo = Entry(registro,textvariable=entrada).place(x=90,y=50)


    SKU = Label(text="SKU").place(x=0,y=80)
    entrada=StringVar()
    Campo = Entry(registro,textvariable=entrada).place(x=90,y=80)

    cantidad=Label(text="Cantidad").place(x=0,y=110)
    entrada=StringVar()
    Campo = Entry(registro,textvariable=entrada).place(x=90,y=110)


    precio=Label(text="Precio").place(x=250,y=50)
    entrada=StringVar()
    Campo = Entry(registro,textvariable=entrada).place(x=380,y=50)

    caducidad=Label(text="Fecha de caducidad").place(x=250,y=80)
    entrada=StringVar()
    Campo = Entry(registro,textvariable=entrada).place(x=380,y=80)


    boton1 = Button(registro,text="Registrar").place(x=180,y=150)
    boton2 = Button(registro,text="Limpiar").place(x=330,y=150)
               

    interfaz.mainloop()
