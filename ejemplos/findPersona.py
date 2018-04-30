import pickle
import time
import os

class Persona():
    ficheroPersonaEscritura=file("Persona.tm","w")
    Personas=[]
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.id="Persona"+str(time.time())
    def loadPersonas(self):
             if (os.path.isfile("Persona.dat") ):
                  ficheroPersonaLectura=file("Persona.dat","r")
                  self.Personas=pickle.load(ficheroPersonaLectura)
                  ficheroPersonaLectura.close()

    def save(self):
         self.Personas.append(self)
   
    def close(self):
        print (self.Personas)
        pickle.dumps(self.Personas,self.ficheroPersonaEscritura)
        self.ficheroPersonaEscritura.close()
        if (os.path.isfile("Persona.dat") ):
             os.remove("Persona.dat") 
        os.rename('Persona.tm', 'Persona.dat')



