import tkinter
import proyecto_usuario
import ventana_principal_Empleados
import interfaz_suministros

from tkinter import *

class ventanaAcceso():
    
    def __init__(self,master):
        self.master=master
        
        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="Acceso",font=(80))
        self.titulo1.grid(row=1,column=1)
        self.titulo1.config(bd=10)
        self.titulo1.config(relief="groove")
        
        self.cuerpo=Frame(self.master,width=500,height=400)
        self.cuerpo.pack(fill="x")        
        
        
        self.master.title("Acceso")
        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        
        self.Empleado=Button(self.botones,command=self.Empleado,text="Empleado",background="white",relief=FLAT)
        self.Empleado.grid(row=3,column=2)
        
        self.spaace=Label(self.cuerpo,text="     Ingresar como      ")
        self.spaace.grid(row=3,column=3,sticky="e",padx=10,pady=5)
        
        self.Usuario=Button(self.botones,command=self.Usuario,text="Agregar Usuario",background="white",relief=FLAT)
        self.Usuario.grid(row=3,column=4)
        
        self.Compras=Button(self.botones,command=self.Compras,text="Compras",background="white",relief=FLAT)
        self.Compras.grid(row=5,column=2)        
        
        self.botones.config(bd=5)        
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2") 
        
    def Empleado(self):
        root2=Toplevel(self.master)
        eml= ventana_principal_Empleados.Principal(root2)                    
        pass
    
    def Usuario(self):
        root3=Toplevel(self.master)
        usr=proyecto_usuario.Usu(root3)             
        pass
    
    def Compras(self):
        root4=Toplevel(self.master)
        buy=interfaz_suministros.Principal(root4)
        pass
        
def main():
            root=Tk()
            ventana=ventanaAcceso(root)
            root.mainloop()
        
if __name__ == '__main__':
            main()
