#Avance de interfaz

from Tkinter import *

root=Tk()
var=StringVar()
label=Message(root, textvariable=var,relief=RAISED)

var.set("Buenos dias!! Como te encuentras hoy?")
var.set("Inicia sesion para comenzar")
label.pack()
root.mainloop()

top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)

L1 = Label(top, text="Password")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)


def CallBack():
    tkMessageBox.showinfo("Crea tu cuenta", "Ingresa tus datos")

CC= Tkinter.Button(top, text = "Crea mi cuenta", command=CallBack)

CC.pack()

SI= Tkinter.Button(top, text = "Iniciar Sesion", command=CallBack)

SI.pack()
 

top.mainloop()