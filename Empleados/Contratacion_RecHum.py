import Clase_Persona
import Clase_Empleados
import Clase_RecHum
import Main_RecHum
import uuid
import constructor

#Codigo omitible?
def contratacion():
    name=str(input("Nombre:\t"))
    fname=str(input("Apellidos:\t"))
    direccion=str(input("Direccion:\t"))
    tel=str(input("Telefono:\t"))
    age=int(input("Edad:\t"))
    correo=str(input("Correo:\t"))
    rfc=str(input("RFC:\t"))
    password=str(input("Contrasena:\t"))
    CodPos=int(input("CodPos:\t"))
    puesto=int(input("Codigo de puesto:\t"))
    jornada_i=int(input("Inicio de jornada:\t"))
    jornad_f=int(input("Final de jornada:\t"))
    salario=int(input("Salario base:\t")) 
    
    idnt=str(uuid.uuid4())
    pass

def guardar_nuevo():
    constructor.construye(puesto,name,fname,direccion,tel,age,correo,rfc,password,CodPos,jornada_i,jornada_f,salario,idnt)
    pass
    
#    if (salir==True):
#        salida(True)
#   elif (salir==False):
#      salida(False)
    
    
    
#def salida(exit):
#    if(exit==True):
#        Menu_principal()
#    elif(exit==False):
#        pass
    
