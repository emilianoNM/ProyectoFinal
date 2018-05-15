
import proveedores_consola
import pedidos
import entregas_programadas
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
    

    def load(numero_pp):
        print (numero_pp)
        b_lectura=open("Proveedores.dat",'r')
        c=b_lectura.read()
        listaJson=json.loads(c)

        print ("buscando..")
        numeroPP=listaJson[numero_pp]['numero_p']

        return numeroPP

        #for numero_pp in listaJson:
           # if  numero_pp==listaJson("listaJson"):
            #    numeroPP=listaJson[numero_pp]['numero_p']
             #   nombrePP=listaJson[numero_pp]['nombre_p']
              #  logoPP=listaJson[numero_pp]['logo']
               # razonSocialP=listaJson[numero_pp]['razon_social']
               # TelefonoP=listaJson[numero_pp]['telefono_p']
               # CorreoP=listaJson[numero_pp]['correo_p']
               # DireccionP=listaJson[numero_pp]['direccion_p']

                #return(numeroPP,nomprePP,logoPP,razonSocialP,TelefonoP,CorreoP,DireccionP)

    def save(self):
        listaJson={}
        
        #convierte a Json
        jsone=self.__dict__
        print(jsone['nombre_p'])

        #Crea lista desde Json
        listaJson[jsone['numero_p']]=jsone
        print (listaJson)

        lista2=open("Proveedores.dat",'w')
        listacom=json.dumps(listaJson)
        print ("lista guardada")
        lista2.write(listacom)
        lista2.close 
        pass

    def validar_pedido(numero_pedido_e):
        vp_lectura=open("pedidosp.txt","rb")
        avp=pickle.load(vp_lecutra)
        for vp in pedidos.pedidos_Lista:
            if(numero_pedido==numero_pedido_e):
                return vp

def load(numero_pp):
    print (numero_pp)
    b_lectura=open("Proveedores.dat",'r')
    c=b_lectura.read()
    print (c )
    print("\n")
    listaJsonS=json.loads(c)
    pp=Proveedores.nombre_p
    print(pp)
    print (listaJsonS['pp'])

    print ("buscando..")
