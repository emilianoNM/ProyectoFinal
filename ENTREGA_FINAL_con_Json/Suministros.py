import pickle
import json
import random
from datetime import datetime
inicio = datetime(2018, 6, 30)
final =  datetime(2018, 12, 28)
random_date = inicio + (final - inicio) * random.random()
print(random_date)

class Suministros():
    IDp=None
    precio=None
    nombre=None
    cantidadstock=None
    proveedor=None
    fecha=None
    
    def __init__(self,IDp,nombre,precio,cantidadstock,proveedor,fecha):
        self.IDp=IDp
        self.precio=precio
        self.nombre=nombre
        self.cantidadstock=cantidadstock
        self.proveedor=proveedor
        self.fecha=fecha

        """listaJson={}
        jsone=self.__dict__
        print (jsone)
        listaJson[jsone['IDp']]=jsone

        lista2=open("Suministros.dat",'w')
        listacom=json.dumps(listaJson)
        print("El documento 'Suministros' fue creado")
        lista2.write(listacom)
        lista2.close()"""

    def save(self):
        jsonobj={}

        f=open("Suministros.dat","r")
        productos=f.read()
        jsonobj=json.loads(productos)
        
        #convierte a Json
        jsone1=self.__dict__
        print (jsone1)
        
        jsonobj[jsone1['IDp']]=jsone1

        f = open("Suministros.dat","w")
        jsonn = json.dumps(jsonobj)
        print("El suministro ha sido registrado con exito")
        f.write(jsonn)
        f.close()

    


    
