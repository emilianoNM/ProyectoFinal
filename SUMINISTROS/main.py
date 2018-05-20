
class objeto:
  
    def __init__(self):
        opcion=str(input("desea consultar la lista de materiales? si (s)/no (n):"))
        if opcion == "s":
           import json
           f=open("pro/productos.json","r")
           productos=f.read()
           c=json.loads(productos)
           self.productos=c
           self.output=[]
        else:
               pass   
    
    def imprimir(self):
        self.opcion1=str(input("Materiales y Piezas (MP)/ Suministros(SS):"))
        if self.opcion1 in self.productos:
           print("")
           print(self.opcion1,":",self.productos[self.opcion1])
           print("")
           
    def seleccion(self):
        self.opcion2=str(input("Ingrese el codigo del articulo que desea adquirir:"))
        #asignacion variable w
        w=(self.productos[self.opcion1][self.opcion2][2])
        if int(w)<= 0:
           self.actualizar()
        else:
           self.articulo()
##################################################
    def actualizar(self):
          print("No hay productos en existencia.")
          opc=str(input("desea ordenar este material?\n si (s) / no (n):"))
          print("")
          if opc=="s":
            #update a json from another json
            import json
            #read productos
            f2 = open("pro/productos.json","r")
            json2=f2.read()
            json3=json.loads(json2)
            #read productos2
            fp = open("pro/productos2.json","r")
            jsonp=fp.read()
            jsonp2=json.loads(jsonp)
            #updates productos
            json3.update(jsonp2)
            #overwrites the document
            f = open("pro/productos.json","w")
            json = json.dumps(json3)
            f.write(json)
            f.close()
            print("Para hacer valido el pedido cierre el programa")
            opc2=str(input("seguir comprando (s) / Cerrar programa (n)"))
            if opc2=="s":
               pass
            else:
               exit()
##################################################
    def articulo(self):
          print("usted adquirio:")
          if self.opcion2 in self.productos[self.opcion1]:
            print(self.opcion2,":",self.productos[self.opcion1][self.opcion2])
            self.output.append(self.productos[self.opcion1][self.opcion2])
            
            #read the document
            import json
            f=open("pro/productos.json","r")
            productos=f.read()
            self.productos=json.loads(productos)
            #print the quantity of the stock before the selection
            print(self.productos[self.opcion1][self.opcion2][2])
            self.productos[self.opcion1][self.opcion2][2]=int(self.productos[self.opcion1][self.opcion2][2]) - 1
            #print the quantity of the stock after the selection
            print(self.productos[self.opcion1][self.opcion2][2])
            f.close()
            #writes and modify document
            f = open("pro/productos.json","w")
            json = json.dumps(self.productos)
            f.write(json)
            f.close()
##################################################
    #hace el listado de los elementos de la self.output
    def listado(self):
        print(self.output)
        print("lista total:")
        for elemento in self.output:
          print(elemento[0],elemento[1])        
          
    #calls all the functions
    def llamado(self):
        continua="s"
        while continua=="s":
          self.imprimir()
          self.seleccion()
          continua=input("Desea agregar otro producto[s/n]?")
          print("_______________________________________")
          print("")
        self.listado() 
    
# bloque principal
productos1=objeto()
productos1.llamado()