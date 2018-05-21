from io import *
import pickle

class Pedido:
    producto=None
    codigo=None
    cantidad=None
    nopedido=None    #numerodepedido
    lista_pedido=[]
    arc=open("lista_pedido.txt","wb")
    def __init__(self,producto,codigo,cantidad,nopedido):
        self.producto=producto
        self.codigo=codigo
        self.cantidad=cantidad
        self.nopedido=nopedido
    def __str__(self):
            return self.lista_pedido
    def agregar(self):
        self.lista_pedido.append(self)
        pickle.dump(self.lista_pedido,self.arc)
    def guardar(self):
        self.arc.close()
    def revision(self):
        arcL=open("lista_pedido.txt")
        a=pickle.load()
        
        
        
        
    
