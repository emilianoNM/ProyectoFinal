
import pedidos
import pickle

class Proveedores():
    nombre_p=None
    logo=None
    razon_social=None
    telefono_p=None
    correo_p=None
    direccion_p=None
    
    Permisos=None
    
    def __init__(self,nombre_p,logo,razon_social,telefono_p,correo_p,direccion_p):
        self.nombre_p=nombre_p
        self.logo=logo
        self.razon_social=razon_social
        self.telefono_p=telefono_p
        self.correo_p=correo_p
        self.direccion_p=direccion_p

proveedor1=Proveedores("Sabritas","#","noe","554343","dsds@example.com","calle ejemplo numero alguno")
proveedor2=Proveedores("Doritos","#","noe","554343","dsds@example.com","calle ejemplo numero alguno")
print (proveedor1.nombre_p)
print (proveedor2.nombre_p)

f=open("proveedores1.txt","wb")
pickle.dump(proveedor1,f)
pickle.dump("\n\n\t",f)
pickle.dump(proveedor2,f)
f.close()

b=open("proveedores1.txt","rb")
c=pickle.load(b)
print(c)

b.close()

#f=open("proveedores.txt","w")
#f.write(s1+"\n")
#f.write(str(proveedor2))
#f.close()

