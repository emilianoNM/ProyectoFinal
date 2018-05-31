#Propuesta de clase para el módulo Facturas
import json

from tkinter import messagebox

class Contador():
    idnt=None
    Nombre=None
    ApellidoP=None
    ApellidoM=None
    Direccion=None
    Telefono=None
    Edad=None
    Correo=None
    RFC=None
    Contrasena=None
    CodPos=None
    Puesto=None
    jornada_i=None
    jornada_f=None
    Salario=None
    Permisos=None
    
    def __init__(self,idnt,Nombre,ApellidoP,ApellidoM,Direccion,Telefono,Edad,Correo,RFC,Contrasena,CodPos,Puesto,jornada_i,jornada_f,Salario,Permisos=1):
        self.idnt=idnt
        self.Nombre=Nombre
        self.ApellidoP=ApellidoP
        self.ApellidoM=ApellidoM
        self.Direccion=Direccion
        self.Telefono=Telefono
        self.Edad=Edad
        self.Correo=Correo
        self.RFC=RFC
        self.Contrasena=Contrasena
        self.CodPos=CodPos
        self.Puesto=Puesto
        self.jornada_i=jornada_i
        self.jornada_f=jornada_f
        self.Salario=Salario
        self.Permisos=Permisos
    
    def save(self):
        listaJson={}

        lista=open("EMPLEADOS.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        
        #convierte a Json
        jsone=self.__dict__
        print (jsone)
        #Crea lista desde Json
        listaJson[jsone['idnt']]=jsone

        lista2=open("EMPLEADOS.dat",'w')
        listacom=json.dumps(listaJson)
        print(listacom)
        lista2.write(listacom)
        lista2.close()
        pass 
        
    def Gen_factura():
        pass
