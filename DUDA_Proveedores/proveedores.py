import pickle
import json

class Proveedores():
    numero_p=None
    nombre_p=None
    logo=None
    razon_social=None
    telefono_p=None
    correo_p=None
    direccion_p=None

    def __init__(self,numero_p,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):
        self.numero_p=numero_p
        self.nombre_p=nombre_p
        self.logo=logo
        self.razon_social=razon_social
        self.telefono_p=telefono_p
        self.correo_p=correo_p
        self.direccion_p=direccion_p

    def save(self):
        listaJson={}

        lista=open("Proveedores.dat",'r')
        lisJson=lista.read()
        listaJson=json.loads(lisJson)
        
        #convierte a Json
        jsone=self.__dict__
        print (jsone)
        
        #Crea lista desde Json
        listaJson[jsone['numero_p']]=jsone

        lista2=open("Proveedores.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo Proveedor agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()


