import proveedores
import entregas_programadas
import pedidos
import json

import pickle
listaJson={}

#class Proveedores(): 
#def __init__(self,numero_p,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):
proveedor1=proveedores.Proveedores("123","Sabritas","#","noe","554343","dsds@example.com","calle ejemplo numero alguno")
proveedor1.save()

proveedor2=proveedores.Proveedores("124","Doritos","#","noe","554342","dsdsd@example.com","calle ejemplo numero alguno")
proveedor2.save()

proveedor2.load()

