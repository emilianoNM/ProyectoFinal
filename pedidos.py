import pickle

class Pedidos():
    numero_pedido_e=None
    nombre_pp=None
    cantidad=None

    p_escritura=open("pedidos.txt","wb")
    pedidos_Lista=[]
    def __init__(self,numero_pedido_e,nombre_pp,cantidad):
        self.numero_pedido_e=numero_pedido_e
        self.nombre_pp=nombre_pp
        self.cantidad=cantidad

    def save(self):
        self.pedidos_Lista.append(self)

    def close(self):
        pickle.dump(self.pedidos_Lista,self.p_escritura)
        self.p_escritura.close()

    def load(self):
        p_lectura=open("pedidos.txt","rb")
        c=pickle.load(p_lectura)
        print("numero de pedidos: "+str((len(c))))
        e_lectura.close()

    def Search(numerop):
        for p in Pedidos.pedidos_Lista:
            if(numerop==nnumero_pedido_e):
                 return p


    
