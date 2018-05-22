import Clientes
import lista_productos
import productos

def ():
	print "Menu\n\n1)/Nueva factura\n2)-Mostrar facturas registrados\n3)eliminar factura"

def nueva_factura():
	print "Nuevo registro\n"
	archivo1 = open("factura.txt","wb")

	numero = raw_input ("numero:")
	fecha = raw_input("ingrese la fecha:")
	total = raw_input ("total:")
	tipo_de_pago = raw_input ("tipo de pago:")

	print " se ha capturado:" + numero +" , con la fecha:" + fecha +" , con el totall a pagar:" + total + " , con la fecha:"+ tipo_de_pago +

	archivo1.write(numero)
	archivo1.write("," )
	archivo1.write(fecha)
	archivo1.write(",")
	archivo1.write(total)
	archivo1.write("," )
	archivo1.write(tipo_de_pago)
	archivo1.write("," )
	archivo1.write("\n")

	archivo1.close()
	
	
def mostrar_factura():
	print "Mostrar Registros\n"
	archivo1 =open("factura.csv")
	print(archivo. read())
	archivo1.close()
	
def eliminar_factura():
	
	archivo1 =open("factura.txt","wb")
	archivo1.truncate()
	print "registros eliminados"
	archivo1.close()
	
producto()

opcion = raw_input("elige una obcion:")

if opcion == "1":
	
	nueva_factura()
	

elif opcion == "2":
	
	mostrar_factura()
	

elif opcion == "3":
	
	eliminar_factura()
	

else:
	print "Debes elegir una obcion anterior"
