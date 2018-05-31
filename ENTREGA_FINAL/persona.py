import pickle
import time
import os
import uuid
import json

class Persona():
    Ide=None
    Nombre=None
    APaterno=None
    AMaterno=None
    CP=None
    Direccion=None
    Telefono=None
    Correo=None
    Edad=None
    RFC=None
 

    def __init__(self,Ide,Nombre,APaterno,AMaterno,CP,Direccion,Telefono,Correo,Edad,RFC):

        
        self.Nombre=Nombre
        self.APaterno=APaterno
        self.AMaterno=AMaterno
        self.CP=CP
        self.Direccion=Direccion
        self.Telefono=Telefono
        self.Ide=Ide
        self.Correo=Correo
        self.Edad=Edad
        self.RFC=RFC
        
	#Crer Json	
	#listaJson={}

        
        #convierte a Json
        #jsone=self.__dict__
        #print (jsone)
        
        #Crea lista desde Json
        #listaJson[jsone['Ide']]=jsone

        #lista2=open("Usuario.dat",'w')
        #listacom=json.dumps(listaJson)
        #print("Nuevo Usuario agregado")
        #print(listacom)
        #lista2.write(listacom)
        #lista2.close()
	
    def save(self):
        listaJson={}

        lista=open("Usuario.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        
        #convierte a Json
        jsone=self.__dict__
        print (jsone)
        
        #Crea lista desde Json
        listaJson[jsone['Ide']]=jsone

        lista2=open("Usuario.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo Usuario agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()
	
