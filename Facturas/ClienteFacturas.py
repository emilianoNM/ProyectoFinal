import pickle
import os
import json

class Clientes():
    nombre=None
    rfc=None
    telefono=None
    correo=None
    direccion=None

    def __init__(self,nombre,rfc,telefono,correo,direccion):
       
        self.nombre=nombre
        self.rfc=rfc
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion

    def save(self):
        listaJson={}

        lista1=open("Clientes.dat",'r')
        liJson=lista1.read()
        listaJson=json.loads(liJson)
        
        #convierte a Json
        jsone=self.__dict__
        
        #Crea lista desde Json
        listaJson[jsone['INfORMACION DE CLIENTE']]=jsone

        lista2=open("Clientes.dat",'w')
        listacom=json.dumps(listaJson)
        lista2.write(listacom)
        lista2.close 

   

   
