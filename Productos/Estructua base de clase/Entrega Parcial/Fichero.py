#Equipo productos 
#Archivo que guarda datos de cliente

import pickle 

import ClasePersona
import ClaseCliente
	    print("Se ha creado un nuevo cliente con el nombre de ", self.nombre")

# Metodo str Convertir en cadena de texto la informacion de un objeto
	def __str__(self):
#Devuelve los tres datos {} {} {}
	    return "{} {} {} {} {} {} {}".format(self.nombre, self.edad, self.e-mail, self.telefono, self.celular, self.rfc, self.direccion)
	    return "{} {} {} {} {} {} {}".format(self.Usuario, self.Contraseña, self.Producto, self.Pregunta, self.Tarjeta, self.Pago, self.Entrega)

#p=Persona("Sandra", "Femenino", 29)

class ListaClientes:

	clientes=[]
#Fichero externo, almacena informacion de manera permanente
#ab+ desplazar el cursor al principio
	def __init__(self):
	    listaDeC=open("ficheroExterno", "ab+")
	    listaDeC.seek(0)
	
	try:
	    self.personas=pickle.load(listaDeC)
	    print ("Se cargaron {} personas del fichero externo".format(len(self.clientes)))

#En caso de que no sea posible
	except:
	    print("El fichero está vacío")

	finally:
	    listaDeC.close()
	    del(listaDeC)
		

#Metodo para agregar personas, parametro de tipo persona para que la agregue a la lista
	def agregarClientes(self, p):
	    self.clientes.append(p)

#Metodo para leer personas, bucle for para recorrer la lista de personas
	def mostrarClientes(self):
	    for p in self.clientes:
		print(p)
#Metodo guardar personas en fichero externo
#writebite para escribir info wb
	def GenFicheroE(self):
	    listaDeC=open("ficheroExterno", "wb")
	    pickle.dump(self.clientes,listaDeC)
	    listaDeC.close()
	    del(listaDeC)

#Metodo para mostrar info del fichero externo
	def mostrar(self):
	    print("La informacion de fichero externo es la siguiente: ")
	    for p in self.clientes:
		print(p)

miLista=ListaClientes()


C=Cliente(N, E, G)
miLista.agregarClientes(p)

miLista.mostrarClientes()










