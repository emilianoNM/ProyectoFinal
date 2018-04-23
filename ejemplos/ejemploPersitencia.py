import pickle

class Persona():

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.id=

class Producto():
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

class Usuario(Persona):
    def __init__(self,passwd,nickname,nombre,edad):



persona1=Persona("Emiliano",12)
persona2=Persona("Juan",15)
print persona1.nombre
print persona2.nombre

ficheroPersona=file("Persona.dat","w")
pickle.dump(persona1,ficheroPersona)
pickle.dump(persona2,ficheroPersona)

ficheroPersona.close()

producto1=Producto("manzana",23)
producto2=Producto("pera",2)

ficheroProducto=file("Producto.dat","w")
pickle.dump(producto1,ficheroProducto)
pickle.dump(producto2,ficheroProducto)

ficheroProducto.close()

