import json

class Producto():
        ID=None
        nombre=None
        precio=None
        fecha=None
        idprov=None
        proveedor=None
        
        def __init__(self, nombre, ID, fecha, precio, idprov,proveedor):
                self.ID =ID
                self.nombre =nombre
                self.precio =precio
                self.fecha = fecha
                self.idprov=idprov
                self.proveedor=proveedor

                """listaJson={}
                jsone=self.__dict__
                print (jsone)
                listaJson[jsone['ID']]=jsone

                lista2=open("Productos.dat",'w')
                listacom=json.dumps(listaJson)
                print("El documento 'Producto' fue creado")
                lista2.write(istacom)
                lista2.close()"""

        def save(self):  
                listaJson={}
                
                lista=open("Productos.dat",'r')
                pedidolis=lista.read()
                listaJson=json.loads(pedidolis)
                
                #convierte a Json
                jsone1=self.__dict__
                print (jsone1)
                
                listaJson[jsone1['ID']]=jsone1

                lista2=open("Productos.dat",'w')
                listacom=json.dumps(listaJson)
                print("Nuevo Producto agregado")
                print(listacom)
                lista2.write(listacom)
                lista2.close()
                pass
