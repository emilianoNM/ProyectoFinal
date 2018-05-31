import persona

import tkinter

from tkinter import *

class Usu():
        def __init__(self,master):
                
                self.Ide_U=StringVar()	
                self.Nombre_U=StringVar()
                self.APaterno_U=StringVar()
                self.AMaterno_U=StringVar()
                self.Telefono_U=StringVar()
                self.Direccion_U=StringVar()
                self.CP_U=StringVar()
                self.edad=StringVar()
                self.correo=StringVar()
                self.rfc=StringVar()

                self.master=master

	
		#root.geometry("500x300+100+100")
                self.master.title('Uusario')
		#Titulo
                self.titulo=Frame(self.master,width=500,height=400)
                self.titulo.pack(fill="y")
                self.titulo1=Label(self.titulo,text="USUARIOS",font=(80))
                self.titulo1.grid(row=1,column=1)
                self.titulo1.config(bd=10)
                self.titulo1.config(relief="groove")
		#Id
                self.cuerpo=Frame(self.master,width=500,height=400)
                self.cuerpo.pack(fill="x")
                self.etiqueta_iden=Label(self.cuerpo,text="Identificacion:")
                self.etiqueta_iden.grid(row=2,column=1,sticky="e",padx=10,pady=5)
                self.iden_entry=Entry(self.cuerpo,textvariable=self.Ide_U)
                self.iden_entry.grid(row=2,column=2,sticky="e",padx=10,pady=5)
		#nombre usuario
                self.etiqueta_nombres=Label(self.cuerpo,text="Nombre Usuario:")
                self.etiqueta_nombres.grid(row=3,column=1,sticky="e",padx=10,pady=5)
                self.nombres_entry=Entry(self.cuerpo,textvariable=self.Nombre_U)
                self.nombres_entry.grid(row=3,column=2,sticky="e",padx=10,pady=5)
		#APaterno
                self.etiqueta_APA=Label(self.cuerpo,text="Apellido Paterno:")
                self.etiqueta_APA.grid(row=4,column=1,sticky="e",padx=10,pady=5)
                self.APA_entry=Entry(self.cuerpo,textvariable=self.APaterno_U)
                self.APA_entry.grid(row=4,column=2,sticky="e",padx=10,pady=5)
		#AMaterno
                self.etiqueta_AMA=Label(self.cuerpo,text="Apellido Materno: ")
                self.etiqueta_AMA.grid(row=5,column=1,sticky="e",padx=10,pady=5)
                self.AMA_entry=Entry(self.cuerpo,textvariable=self.AMaterno_U)
                self.AMA_entry.grid(row=5,column=2,sticky="e",padx=10,pady=5)
		#Telefono
                self.etiqueta_TTelefono=Label(self.cuerpo,text="Telefono: ")
                self.etiqueta_TTelefono.grid(row=6,column=1,sticky="e",padx=10,pady=5)
                self.TTelefono_entry=Entry(self.cuerpo,textvariable=self.Telefono_U)
                self.TTelefono_entry.grid(row=6,column=2,sticky="e",padx=10,pady=5)
		#Direccion
                self.etiqueta_DIR=Label(self.cuerpo,text="Direccion: ")
                self.etiqueta_DIR.grid(row=7,column=1,sticky="e",padx=10,pady=5)
                self.DIR_entry=Entry(self.cuerpo,textvariable=self.Direccion_U)
                self.DIR_entry.grid(row=7,column=2,sticky="e",padx=10,pady=5)
		#CP
                self.etiqueta_CPO=Label(self.cuerpo,text="CP: ")
                self.etiqueta_CPO.grid(row=8,column=1,sticky="e",padx=10,pady=5)
                self.CPO_entry=Entry(self.cuerpo,textvariable=self.CP_U)
                self.CPO_entry.grid(row=8,column=2,sticky="e",padx=10,pady=5)
                #Correo_electronico
                self.etiqueta_d=Label(self.cuerpo,text="Correo electronico: ")
                self.etiqueta_d.grid(row=9,column=1,sticky="e",padx=10,pady=5)
                self.direccion_entry=Entry(self.cuerpo,textvariable=self.correo)
                self.direccion_entry.grid(row=9,column=2,sticky="e",padx=10,pady=5)        
                #RFC
                self.etiqueta_d=Label(self.cuerpo,text="RFC: ")
                self.etiqueta_d.grid(row=10,column=1,sticky="e",padx=10,pady=5)
                self.direccion_entry=Entry(self.cuerpo,textvariable=self.rfc)
                self.direccion_entry.grid(row=10,column=2,sticky="e",padx=10,pady=5)
                #Edad
                self.etiqueta_rs=Label(self.cuerpo,text="Edad: ")
                self.etiqueta_rs.grid(row=11,column=1,sticky="e",padx=10,pady=5)
                self.rs_entry=Entry(self.cuerpo,textvariable=self.edad)
                self.rs_entry.grid(row=11,column=2,sticky="e",padx=10,pady=5)

	        #final
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
                print(self.Ide_U.get())
                strIde=self.Ide_U.get()
                strNombre=self.Nombre_U.get()
                strAPaterno=self.APaterno_U.get()
                strAMaterno=self.AMaterno_U.get()
                strCP=self.CP_U.get()
                strDireccion=self.Direccion_U.get()
                strTelefono=self.Telefono_U.get()
                srtEdad=self.edad.get()
                strCorreo=self.correo.get()
                strRFC=self.rfc.get()
	 

                a=persona.Persona(strIde,strNombre,strAPaterno,strAMaterno,strCP,strDireccion,strTelefono,strCorreo,srtEdad,strRFC)
                a.save()

	    
                self.Ide_U.set("")
                self.Nombre_U.set("")
                self.APaterno_U.set("")
                self.AMaterno_U.set("")
                self.Direccion_U.set("")
                self.Telefono_U.set("")
                self.CP_U.set("")
        def cancelar(self):
                self.Ide_U.set("")
                self.APaterno_U.set("")
                self.AMaterno_U.set("")
                self.Telefono_U.set("")
                self.Direccion_U.set("")
                self.CP_U.set("")
                self.Nombre_U.set("")

	

def     main():      
	#mainloop
	root=Tk()
	Ventana=Usu(root)	
	root.mainloop()

if __name__=='__main__':
	main()
