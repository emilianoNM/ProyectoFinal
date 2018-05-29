import constructor
import tkinter

from tkinter import *

class ventanaguardar():

    def __init__(self,master):
        self.idnt=StringVar()
        self.nombre=StringVar()
        self.apellidos=StringVar()
        self.edad=StringVar()
        self.direccion=StringVar()
        self.telefono=StringVar()
        self.cod_pos=StringVar()
        self.correo=StringVar()
        self.rfc=StringVar()
        self.pasword=StringVar()
        self.puesto=StringVar()
        self.entrada=StringVar()
        self.salida=StringVar()
        self.salario=StringVar()

        self.master=master
        self.master.title("Recursos humanos")

        self.titulo=Frame(self.master,width=500,height=400)
        self.titulo.pack(fill="y")
        self.titulo1=Label(self.titulo,text="Contratacion",font=(80))
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
        #nombre
        self.etiqueta_nombre=Label(self.cuerpo,text="Nombre:")
        self.etiqueta_nombre.grid(row=3,column=1,sticky="e",padx=10,pady=5)
        self.nombre_entry=Entry(self.cuerpo,textvariable=self.nombre)
        self.nombre_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
        #Apellidos
        self.etiqueta_logo=Label(self.cuerpo,text="Apellidos:")
        self.etiqueta_logo.grid(row=4,column=1,sticky="e",padx=10,pady=5)
        self.logo_entry=Entry(self.cuerpo,textvariable=self.apellidos)
        self.logo_entry.grid(row=4,column=2,sticky="e",padx=10,pady=5)
        #Edad
        self.etiqueta_rs=Label(self.cuerpo,text="Edad: ")
        self.etiqueta_rs.grid(row=5,column=1,sticky="e",padx=10,pady=5)
        self.rs_entry=Entry(self.cuerpo,textvariable=self.edad)
        self.rs_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        #Direccion
        self.etiqueta_telefono=Label(self.cuerpo,text="Direccion: ")
        self.etiqueta_telefono.grid(row=6,column=1,sticky="e",padx=10,pady=5)
        self.telefono_entry=Entry(self.cuerpo,textvariable=self.direccion)
        self.telefono_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
        #Telefono
        self.etiqueta_correo=Label(self.cuerpo,text="Telefono: ")
        self.etiqueta_correo.grid(row=7,column=1,sticky="e",padx=10,pady=5)
        self.correo_entry=Entry(self.cuerpo,textvariable=self.telefono)
        self.correo_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)
        #Codigo postal
        self.etiqueta_d=Label(self.cuerpo,text="Codigo postal: ")
        self.etiqueta_d.grid(row=8,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.cod_pos)
        self.direccion_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)
        #Correo_electronico
        self.etiqueta_d=Label(self.cuerpo,text="Codigo postal: ")
        self.etiqueta_d.grid(row=9,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.correo)
        self.direccion_entry.grid(row=9,column=2,sticky="e",padx=10,pady=5)        
        #RFC
        self.etiqueta_d=Label(self.cuerpo,text="RFC: ")
        self.etiqueta_d.grid(row=10,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.rfc)
        self.direccion_entry.grid(row=10,column=2,sticky="e",padx=10,pady=5)
        #Contrasena
        self.etiqueta_d=Label(self.cuerpo,text="Contrasena: ")
        self.etiqueta_d.grid(row=11,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.pasword)
        self.direccion_entry.grid(row=11,column=2,sticky="e",padx=10,pady=5)
        #Puesto
        self.etiqueta_d=Label(self.cuerpo,text="Puesto: ")
        self.etiqueta_d.grid(row=12,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.puesto)
        self.direccion_entry.grid(row=12,column=2,sticky="e",padx=10,pady=5)
        #Horario_entrada
        self.etiqueta_d=Label(self.cuerpo,text="Horario de entrada: ")
        self.etiqueta_d.grid(row=13,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.entrada)
        self.direccion_entry.grid(row=13,column=2,sticky="e",padx=10,pady=5)
        #Horario_salida
        self.etiqueta_d=Label(self.cuerpo,text="Horario de salida ")
        self.etiqueta_d.grid(row=14,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.salida)
        self.direccion_entry.grid(row=14,column=2,sticky="e",padx=10,pady=5)
        #Salario_base
        self.etiqueta_d=Label(self.cuerpo,text="Salario base: ")
        self.etiqueta_d.grid(row=15,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.salario)
        self.direccion_entry.grid(row=15,column=2,sticky="e",padx=10,pady=5)        

        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Guardar=Button(self.botones,command=self.save,text="Guardar",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.Cancelar=Button(self.botones,command=self.cancelar,text="Cancelar",background="white",relief=FLAT)
        self.Cancelar.grid(row=1,column=2)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")

    def save(self):
        print(self.idnt.get())
        strIdnt=self.idnt.get()
        strNombre=self.nombre.get()
        strApellidos=self.apellidos.get()
        strEdad=self.edad.get()
        strDireccion=self.direccion.get()
        strTelefono=self.telefono.get()
        strCodPos=self.cod_pos.get()
        strCorreo=self.correo.get()
        strRFC=self.rfc.get()
        strPassword=self.pasword.get()
        strPuesto=self.puesto.get()
        strEntrada=self.entrada.get()
        strSalida=self.salida.get()
        strSalario=self.salario.get()

        constructor.construye(strPuesto,strNombre,strApellidos,strDireccion,strTelefono,strEdad,strCorreo,strRFC,strPassword,strCodPos,strPuesto,strEntrada,strSalida,strSalario)
        
        self.idnt.set("")
        self.nombre.set("")
        self.apellidos.set("")
        self.edad.set("")
        self.direccion.set("")
        self.telefono.set("")
        self.cod_pos.set("")
        self.correo.set("")
        self.rfc.set("")
        self.pasword.set("")
        self.puesto.set("")
        self.entrada.set("")
        self.salida.set("")
        self.salario.set("")
        pass
    
    def cancelar(self):
        self.idnt.set("")
        self.nombre.set("")
        self.apellidos.set("")
        self.edad.set("")
        self.direccion.set("")
        self.telefono.set("")
        self.cod_pos.set("")
        self.correo.set("")
        self.rfc.set("")
        self.pasword.set("")
        self.puesto.set("")
        self.entrada.set("")
        self.salida.set("")
        self.salario.set("")
        pass
    


    
def main():
    root=Tk()
    ventana=ventanaguardar(root)
    root.mainloop()

if __name__ == '__main__':
    main()

