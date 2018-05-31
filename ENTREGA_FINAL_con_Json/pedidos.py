import pickle
import json

class Pedidos():
    numeropedido=None
    nombre_pp=None
    cantidad=None
    idpro=None
    precio=None
    proveedor=None
    
    def __init__(self,numeropedido,idpro,nombre_pp,precio,proveedor,cantidad):
        self.numeropedido=numeropedido
        self.nombre_pp=nombre_pp
        self.cantidad=cantidad
        self.idpro=idpro
        self.precio=precio
        self.proveedor=proveedor

        """listaJson={}
        jsone=self.__dict__
        print (jsone)
        listaJson[jsone['ID']]=jsone

        lista2=open("Pedidos.dat",'w')
        listacom=json.dumps(listaJson)
        print("El documento 'Productos' fue creado")
        lista2.write(listacom)
        lista2.close()"""
        
        
    def savei(self):
        listaJson={}

        lista=open("Pedidos.dat",'r')
        pedidolis=lista.read()
        listaJson=json.loads(pedidolis)
        
        #convierte a Json
        jsone1=self.__dict__
        
        listaJson[jsone1['numeropedido']]=jsone1

        lista2=open("Pedidos.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo pedido agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()

    def savepr(self):
        listaJson={}

        lista=open("Pedidos.dat",'r')
        pedidolis=lista.read()
        listaJson=json.loads(pedidolis)
        
        #convierte a Json
        jsone1=self.__dict__
        
        listaJson[jsone1['numeropedido']]=jsone1

        lista2=open("Pedidos.dat",'w')
        listacom=json.dumps(listaJson)
        print("Nuevo pedido agregado")
        print(listacom)
        lista2.write(listacom)
        lista2.close()

    


    
