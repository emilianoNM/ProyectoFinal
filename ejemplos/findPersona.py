import pickle
import time
import os
import uuid

class Persona():
    ficheroPersonaEscritura=file("Persona.tm","w")
    ListaPersonas=[]
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.id="Persona"+str(uuid.uuid4())


    def save(self):
         Persona.ListaPersonas.append(self)
   
  
#Metodo de Modulo
def findPersona(idPersona):

    for persona in  Persona.ListaPersonas:
        if(idPersona==persona.id):
            return persona

def loadListaPersonas():
            if (os.path.isfile("Persona.dat") ):
                ficheroPersonaLectura=file("Persona.dat","r")
                Persona.ListaPersonas=pickle.load(ficheroPersonaLectura)
                print("Numero de Personas recuperadas "+str(len(Persona.ListaPersonas)))
                ficheroPersonaLectura.close()
def close():
        pickle.dump(Persona.ListaPersonas,Persona.ficheroPersonaEscritura)
        Persona.ficheroPersonaEscritura.close()
        if (os.path.isfile("Persona.dat") ):
            os.remove("Persona.dat") 
        os.rename('Persona.tm', 'Persona.dat')




