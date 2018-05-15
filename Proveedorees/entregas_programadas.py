import producto
import pedidos
import proveedores

class Entregas():
    numero_entrega=None
    cuenta_total=None
    f_entrega=None
    nombre_repartidor=None
    estadoEntrega=None

    e_escritura=open("entregas.txt","wb")
    Entregas_lista=[]
    def __init__(self,numero_entrega,nombre_repartidor,cuenta_tota,f_entrega,estadoEntrega):
        self.numero_entrega=numero_entrega
        self.nombre_repartidor=nombre_repartidor
        self.cuenta_total=cuenta_total
        self.f_entrega=f_entrega
        self.estadoEntrega=estadoEntrega


    def save(self):
        self.Entegas_lista.append(self)

    def close(self):
        pickle.dump(self.Etregas_lista,self.e_escritura)
        self.e_escritura.close()

    def load(self):
        e_lectura=open("entregas.txt","wb")
        c=pickle.load(e_lectura)
        print("numero de entregas: "+str((len(c))))
        e_lectura.close()

    def Search(numeroe):
        for p in Entregas.Entregas_lista:
            if(numeroe==numero_entrega):
                 return p

