import proveedores
import entregas_programadas
import pedidos
import json

import pickle
listaJson={}

#class Proveedores(): 
#def __init__(self,numero_p,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):

def construye(numero_p,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):
    proveedor1=proveedores.Proveedores(numero_p,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p)
    proveedor1.save()

