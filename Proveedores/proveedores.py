import pedidos
import pickle
import time
import os
import uuid
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

        lista1=open("Proveedores.dat",'r')
        liJson=lista1.read()
        listaJson=json.loads(liJson)
        
        #convierte a Json
        jsone=self.__dict__
        
        #Crea lista desde Json
        listaJson[jsone['numero_p']]=jsone

        lista2=open("Proveedores.dat",'w')
        listacom=json.dumps(listaJson)
        lista2.write(listacom)
        lista2.close 

    def validar_pedido(numero_pedido_e):
        vp_lectura=open("pedidosp.txt","rb")
        avp=pickle.load(vp_lecutra)
        for vp in pedidos.pedidos_Lista:
            if(numero_pedido==numero_pedido_e):
                return vp

    def load(numero_pp):
        listaJsonS={}
        b_lectura=open("Proveedores.dat",'r')
        c=b_lectura.read()
        listaJsonS=json.loads(c)

        print ("buscando..")

        return listaJsonS[numero_pp]['nombre_p']
