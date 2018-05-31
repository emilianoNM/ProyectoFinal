import Despido_RecHum
import tkinter

from tkinter import *

class ventanadespedir():

    def __init__(self,master):
        self.idnt=StringVar()

        self.master=master
        self.master.title("Recursos humanos")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="Retiro",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
         #Identificador
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="x")
        self.etiqueta_numerop=Label(self.cuerpo,text="Numero Empleado:")
        self.etiqueta_numerop.grid(row=2,column=1,sticky="e",padx=10,pady=5)
        self.numero_entry=Entry(self.cuerpo,textvariable=self.idnt)
        self.numero_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)        

        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Guardar=Button(self.botones,command=self.despedir,text="Despedir",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.Cancelar=Button(self.botones,command=self.cancelar,text="Cancelar",background="white",relief=FLAT)
        self.Cancelar.grid(row=1,column=2)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")

    def despedir(self):
        print(self.idnt.get())
        strIdnt=self.idnt.get()

        Despido_RecHum.despido(strIdnt)
            
        self.idnt.set("")
        pass
    
    def cancelar(self):
        self.idnt.set("")
        pass
    


    
def main():
    root=Tk()
    ventana=ventanadespedir(root)
    root.mainloop()

if __name__ == '__main__':
    main()

