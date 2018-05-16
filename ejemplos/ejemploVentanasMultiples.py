import Tkinter 
import ejemploVentana2
root=Tkinter.Tk()
def funcion():
    otraVentana=Tkinter.Toplevel(root)
    root.iconify()
boton = Tkinter.Button(root,text='Abrir otra ventata',command=ejemploVentana2.ventana2)
boton.pack()
root.mainloop()
