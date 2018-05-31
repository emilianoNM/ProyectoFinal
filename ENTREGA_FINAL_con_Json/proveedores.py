import pickle

import json

class Proveedores():
    numero_p=None
    nombre_p=None
    razon_social=None
    telefono_p=None
    correo_p=None
    direccion_p=None
    producto_p=None

    def __init__(self,numero_p,nombre_p,razon_social,telefono_p,correo_p,direccion_p):
        self.numero_p=numero_p
        self.nombre_p=nombre_p
        self.razon_social=razon_social
        self.telefono_p=telefono_p
        self.correo_p=correo_p
        self.direccion_p=direccion_p

        """#POR SI ELIMINAMOS "Proveedores.dat"
        listaJson={}
        jsone=self.__dict__
        print (jsone)
        listaJson[jsone['numero_p']]=jsone

        lista2=open("Proveedores.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo Proveedor agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()"""
        
    def save(self):
        listaJson={}

        lista=open("Proveedores.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        
        #convierte a Json
        jsone=self.__dict__
        #Crea lista desde Json
        listaJson[jsone['numero_p']]=jsone

        lista2=open("Proveedores.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo Proveedor agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()

    def proguctog(self):
        listaproducto={}

        lista=open("Proveedores.dat",'r')
        lisPro=lista.read()
        listaproducto=json.loads(lisPro)
        
        #convierte a Json
        prod=self.__dict__
        
        #Crea lista desde Json
        listaproducto[prod['numero_p']]=prod

        lista3=open("Proveedores.dat",'w')
        listapro=json.dumps(listaproducto)
        print(listapro)
        lista3.write(listapro)
        lista3.close()
