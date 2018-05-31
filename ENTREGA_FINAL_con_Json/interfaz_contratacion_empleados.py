
import constructor
import tkinter
import proyecto_usuario
import json

from tkinter import *
from tkinter import messagebox

class ventanaguardar():

    def __init__(self,master):
        self.idnt=StringVar()
        self.nombre=StringVar()
        self.apellidoP=StringVar()
        self.apellidoM=StringVar()
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
        #Apellido_Paterno
        self.etiqueta_ap=Label(self.cuerpo,text="Apellido Paterno:")
        self.etiqueta_ap.grid(row=4,column=1,sticky="e",padx=10,pady=5)
        self.ap_entry=Entry(self.cuerpo,textvariable=self.apellidoP)
        self.ap_entry.grid(row=4,column=2,sticky="e",padx=10,pady=5)
        #Apellido_Materno
        self.etiqueta_ap=Label(self.cuerpo,text="Apellido Materno: ")
        self.etiqueta_ap.grid(row=5,column=1,sticky="e",padx=10,pady=5)
        self.ap_entry=Entry(self.cuerpo,textvariable=self.apellidoM)
        self.ap_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
        #Edad
        self.etiqueta_edad=Label(self.cuerpo,text="Edad: ")
        self.etiqueta_edad.grid(row=6,column=1,sticky="e",padx=10,pady=5)
        self.edad_entry=Entry(self.cuerpo,textvariable=self.edad)
        self.edad_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
        #Direccion
        self.etiqueta_direccion=Label(self.cuerpo,text="Direccion: ")
        self.etiqueta_direccion.grid(row=7,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.direccion)
        self.direccion_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)
        #Telefono
        self.etiqueta_telefono=Label(self.cuerpo,text="Telefono: ")
        self.etiqueta_telefono.grid(row=8,column=1,sticky="e",padx=10,pady=5)
        self.telefono_entry=Entry(self.cuerpo,textvariable=self.telefono)
        self.telefono_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)
        #Codigo postal
        self.etiqueta_d=Label(self.cuerpo,text="Codigo postal: ")
        self.etiqueta_d.grid(row=9,column=1,sticky="e",padx=10,pady=5)
        self.direccion_entry=Entry(self.cuerpo,textvariable=self.cod_pos)
        self.direccion_entry.grid(row=9,column=2,sticky="e",padx=10,pady=5)
        #Correo_electronico
        self.etiqueta_correo=Label(self.cuerpo,text="Correo electronico: ")
        self.etiqueta_correo.grid(row=10,column=1,sticky="e",padx=10,pady=5)
        self.correo_entry=Entry(self.cuerpo,textvariable=self.correo)
        self.correo_entry.grid(row=10,column=2,sticky="e",padx=10,pady=5)        
        #RFC
        self.etiqueta_rfc=Label(self.cuerpo,text="RFC: ")
        self.etiqueta_rfc.grid(row=11,column=1,sticky="e",padx=10,pady=5)
        self.rfc_entry=Entry(self.cuerpo,textvariable=self.rfc)
        self.rfc_entry.grid(row=11,column=2,sticky="e",padx=10,pady=5)
        #Contrasena
        self.etiqueta_cont=Label(self.cuerpo,text="Contrasena: ")
        self.etiqueta_cont.grid(row=12,column=1,sticky="e",padx=10,pady=5)
        self.cont_entry=Entry(self.cuerpo,textvariable=self.pasword)
        self.cont_entry.grid(row=12,column=2,sticky="e",padx=10,pady=5)
        #Puesto
        self.etiqueta_puesto=Label(self.cuerpo,text="Puesto: ")
        self.etiqueta_puesto.grid(row=13,column=1,sticky="e",padx=10,pady=5)
        self.puesto_entry=Entry(self.cuerpo,textvariable=self.puesto)
        self.puesto_entry.grid(row=13,column=2,sticky="e",padx=10,pady=5)
        #Horario_entrada
        self.etiqueta_he=Label(self.cuerpo,text="Horario de entrada: ")
        self.etiqueta_he.grid(row=14,column=1,sticky="e",padx=10,pady=5)
        self.he_entry=Entry(self.cuerpo,textvariable=self.entrada)
        self.he_entry.grid(row=14,column=2,sticky="e",padx=10,pady=5)
        #Horario_salida
        self.etiqueta_hs=Label(self.cuerpo,text="Horario de salida ")
        self.etiqueta_hs.grid(row=15,column=1,sticky="e",padx=10,pady=5)
        self.hs_entry=Entry(self.cuerpo,textvariable=self.salida)
        self.hs_entry.grid(row=15,column=2,sticky="e",padx=10,pady=5)
        #Salario_base
        self.etiqueta_sb=Label(self.cuerpo,text="Salario base: ")
        self.etiqueta_sb.grid(row=16,column=1,sticky="e",padx=10,pady=5)
        self.sb_entry=Entry(self.cuerpo,textvariable=self.salario)
        self.sb_entry.grid(row=16,column=2,sticky="e",padx=10,pady=5)        

        self.botones=Frame(self.master,width=10,height=20)
        self.botones.pack(fill="y")
        self.Guardar=Button(self.botones,command=self.save,text="Buscar Persona",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=1)
        self.Guardar=Button(self.botones,command=self.contratar,text="Contratar",background="gray",relief=FLAT)
        self.Guardar.grid(row=1,column=2)
        self.Cancelar=Button(self.botones,command=self.cancelar,text="Cancelar",background="white",relief=FLAT)
        self.Cancelar.grid(row=1,column=3)
        self.botones.config(bd=5)
        self.botones.config(relief="groove")
        self.botones.config(cursor="hand2")

    def save(self):
        strIdnt=self.idnt.get()
        strNombre=self.nombre.get()
        strApellidoP=self.apellidoP.get()
        strApellidoM=self.apellidoM.get()
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

        if strIdnt == "" and strNombre == "":
            messagebox.showinfo("Error","Se necesita agregar un identificador o nombre")
        elif strIdnt != "" and strNombre != "":
            messagebox.showinfo("Error","Solo agrega un identificador o nombre")
        elif strPuesto == "":
            messagebox.showinfo("Error","Agrega un puesto")
        else:
            messagebox.showinfo("Cargando","Cargando datos de la persona")
            if strIdnt == "":
                self.cargardatos1()
                
            else:
                self.cargardatos2()
                
            
        pass
    def cargardatos1(self):
        listaJson={}
        lista=open("Usuario.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)

        Nombreusuario=self.nombre.get()
        for idnt in listaJson:
            encontradon=0
            Nombrecompara=listaJson[idnt]['Nombre']
            if Nombreusuario==Nombrecompara:
                strIdnt=self.idnt.set(listaJson[idnt]['Ide'])
                strApellidoP=self.apellidoP.set(listaJson[idnt]['APaterno'])
                strApellidoM=self.apellidoM.set(listaJson[idnt]['AMaterno'])
                strEdad=self.edad.set(listaJson[idnt]['Edad'])
                strDireccion=self.direccion.set(listaJson[idnt]['Direccion'])
                strTelefono=self.telefono.set(listaJson[idnt]['Telefono'])
                strCodPos=self.cod_pos.set(listaJson[idnt]['CP'])
                strCorreo=self.correo.set(listaJson[idnt]['Correo'])
                strRFC=self.rfc.set(listaJson[idnt]['RFC'])
                encontradon=encontradon+1
                messagebox.showinfo("Siguiente","Llena los campos restantes")
                #constructor.construye(strPuesto,strNombre,strApellidoP,strApellidoM,strDireccion,strTelefono,strEdad,strCorreo,strRFC,strPassword,strCodPos,strEntrada,strSalida,strSalario,strIdnt)
                return
        if encontradon==0:
            messagebox.showinfo("Error","El Usuario "+self.nombre.get()+" no fue encontrado, intente de nuevo")
            rir=messagebox.askyesno("Ingresar","¿Deseas agregar usuario?")
            rir = True
            if rir:
                self.irusuario()
            pass
        
    def cargardatos2(self):
        listaJson={}
        lista=open("Usuario.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)

        Numerousuario=self.idnt.get()
        for nombre in listaJson:
            encontradon=0
            Numerocompara=listaJson[nombre]['Ide']
            if Numerousuario==Numerocompara:
                strNombre=self.nombre.set(listaJson[nombre]['Nombre'])
                strApellidoP=self.apellidoP.set(listaJson[nombre]['APaterno'])
                strApellidoM=self.apellidoM.set(listaJson[nombre]['AMaterno'])
                strEdad=self.edad.set(listaJson[nombre]['Edad'])
                strDireccion=self.direccion.set(listaJson[nombre]['Direccion'])
                strTelefono=self.telefono.set(listaJson[nombre]['Telefono'])
                strCodPos=self.cod_pos.set(listaJson[nombre]['CP'])
                strCorreo=self.correo.set(listaJson[nombre]['Correo'])
                strRFC=self.rfc.set(listaJson[nombre]['RFC'])
                encontradon=encontradon+1
                messagebox.showinfo("Siguiente","Llena los campos restantes")
                #constructor.construye(strPuesto,strNombre,strApellidoP,strApellidoM,strDireccion,strTelefono,strEdad,strCorreo,strRFC,strPassword,strCodPos,strEntrada,strSalida,strSalario,strIdnt)
                return
        if encontradon==0:
            messagebox.showinfo("Error","El Usuario "+self.nombre.get()+" no fue encontrado, intente de nuevo")
            return

    def contratar(self):
        strIdnt=self.idnt.get()
        strNombre=self.nombre.get()
        strApellidoP=self.apellidoP.get()
        strApellidoM=self.apellidoM.get()
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
        
        if strIdnt == "" and strNombre == "":
            messagebox.showinfo("Error","Se necesita agregar un identificador o nombre")
        elif strPassword == ""  or strEntrada == "" or strSalida == "" or strSalario == "":
            messagebox.showinfo("Error","Llene todos los campos")
        else:
            messagebox.showinfo("Exito","Contratacion exitosa")
            constructor.construye(strPuesto,strNombre,strApellidoP,strApellidoM,strDireccion,strTelefono,strEdad,strCorreo,strRFC,strPassword,strCodPos,strEntrada,strSalida,strSalario,strIdnt)

    def irusuario(self):
        root2=Toplevel(self.master)
        usuar=proyecto_usuario.Usu(root2)
        
        
    def cancelar(self):
        self.idnt.set("")
        self.nombre.set("")
        self.apellidoP.set("")
        self.apellidoM.set("")
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

