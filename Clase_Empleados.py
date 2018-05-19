import Clase_Persona

class Empleado(Clase_Persona.Persona):
    Puesto=None
    jornada_i=None
    jornada_f=None
    Salario=None
    Permisos=None
    
    def __init__(self,Puesto,jornada_i,jornada_f,Salario,Permisos):
        self.Puesto=Puesto
        self.jornada_i=jornada_i
        self.jornada_f=jornada_f
        self.Salario=Salario
        self.Permisos=Permisos

    
