class lista_productos:

def producto():
	print "Menu\n\n1)/Nuevo producto\n2)-Mostrar productos registrados\n3)eliminar producto"

def nuevo():
	print "Nuevo registro\n"
	archivo = open("agregar.csv","a")

	nombre = raw_input ("ingrese el nombre:")
	precio = raw_input("ingrese el precio:")
	print " se ha capturado:" + nombre +" , con el precio:" + precio

	archivo.write(nombre)
	archivo.write("," )
	archivo.write(precio)
	archivo.write(",")
	archivo.write(ID)
	archivo.write(",")
	archivo.write("\n")

	archivo.close()
	
	
def mostrar():
	print "Mostrar Registros\n"
	archivo =open("agregar.csv")
	print(archivo. read())
	archivo.close()
	
def eliminar():
	
	archivo =open("agregar.csv","a")
	archivo.truncate()
	print "registros eliminados"
	archivo.close()
	
producto()

opcion = raw_input("elige una obcion:")

if opcion == "1":
	
	nuevo()
	

elif opcion == "2":
	
	mostrar()
	

elif opcion == "3":
	
	eliminar()
	

else:
	print "Debes elegir una obcion anterior"

	


