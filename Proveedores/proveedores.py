
import pedidos
import entregas_programadas
import pickle
import time
import os
import uuid

class Proveedores():
    nombre_p=None
    logo=None
    razon_social=None
    telefono_p=None
    correo_p=None
    direccion_p=None
    
    Permisos=None
    f_escritura=open("proveedores1.txt","wb")
    Proveedores_lista=[]
    def __init__(self,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):
        self.nombre_p=nombre_p
        self.logo=logo
        self.razon_social=razon_social
        self.telefono_p=telefono_p
        self.correo_p=correo_p
        self.direccion_p=direccion_p
    

    def load(self):
        b_lectura=open("proveedores1.txt","rb")
        c=pickle.load(b_lectura)
        print("elementos en archivo= "+str((len(c))))
        b_lectura.close()

    def save(self):
        Proveedores.Proveedores_lista.append(self)

    def close(self):
        pickle.dump(Proveedores.Proveedores_lista,self.f_escritura)
        self.f_escritura.close()

    def Search(snompre_p):
        for p in Proveedores.Proveedores_lista:
            if(snompre_p==nombre_pp):
                 return p

    def validar_pedido(numero_pedido_e):
        vp_lectura=open("pedidosp.txt","rb")
        avp=pickle.load(vp_lecutra)
        for vp in pedidos.pedidos_Lista:
            if(numero_pedido==numero_pedido_e):
                return vp

        


#f=open("proveedores.txt","w")
#f.write(s1+"\n")
#f.write(str(proveedor2))
#f.close()

