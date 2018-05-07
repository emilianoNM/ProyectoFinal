#Estructura básica de clases
#Clase Cliente

import ClasePersona

class Cliente(Persona):
	Usuario=None
	Contraseña=None
	Producto=None
	Pregunta=None
	Tarjeta=None
	Pago=None
	Entrega=None 

def __init__(self,Usuario,Contraseña,Producto,Pregunta,Tarjeta,Pago,Entrega)
		self.Usuario=Usuario
		self.Contraseña=Contraseña
		self.Producto=Producto
		self.Pregunta=Pregunta
		self.Tarjeta=Tarjeta
		self.Pago=Pago
		self.Entrega=Entrega 
	
def Crear_Usuario(self):
	print("Crea tu cuenta para continuar con la compra")
	N=str(input("Nombre: "\t)
	E=str(input("Edad: "\t)
	G=str(input("Genero: "\t)
	U=str(input("Usuario: "\t)
	E=str(input("E-mail: "\t)
	T=str(input("Teléfono: "\t)
	E=str(input("Contraseña: "\t)

	
def Buscar_Producto(self):
	print("Puedes seleccionar varios productos\t ")
	print("Introduce la cantidad de productos que necesites")
	print("Solo das click y va directo a tu carrito")
	P=int(input("Cantidad: \t")

def Hacer_Pregunta(self):
	print("Puedes hacer una pregunta acerca del producto de tu interes")
	Pre=("Pregunta: \t Enviar \t")
def Realizar_Pedido(self):

def Elegir_Pago(self):
	print("Entrar metodo de pago")
#Opciones tarjeta credito, debito, efectivo, paypal, deposito, etc
def Elegir_Entrega(self):
	print("Entrar lugar y metodo de entrega")
	D=("Ubicacion de entrega: \t ")
def Calificar_Entrega(self):
	print("¿Llego a tiempo tu producto? \t ¿Fue lo que esperabas? \t Quejas y sugerencias \t")

	
