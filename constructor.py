import Clase_Persona
import Clase_Empleados
import Clase_RecHum
import Clase_Contador
import Clase_Admin_Productos
import Clase_Gerente_gerenal
import Clase_Obrero

import pickle
import json

base_empleados=open("EMPLEADOS.dat","r")

carga=base_empleados.read()
edit=json.loads(carga)

def construye(pUesto,nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,jOrnada_i,jOrnada_f,sAlario,iDnt):
    if(pUesto==1):
        #iDnt=Clase_RecHum.RecHuman(nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        edit[iDnt]={'ID':iDnt,'Nombre':nAme,'Apellido':fName,'Edad':aGe,'Telefono':tEl,'Correo':cOrreo,'Codigo-Postal':COdPos,'RFC':rFc,'Puesto':1,'Entrada':jOrnada_i,'Salida':jornada_f,'Salario':sAlario,'Contrasena':pAssword}
    elif(pUesto==2):
        #iDnt=Clase_Contador.Contador(nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        edit[iDnt]={'ID':iDnt,'Nombre':nAme,'Apellido':fName,'Edad':aGe,'Telefono':tEl,'Correo':cOrreo,'Codigo-Postal':COdPos,'RFC':rFc,'Puesto':2,'Entrada':jOrnada_i,'Salida':jornada_f,'Salario':sAlario,'Contrasena':pAssword}        
    elif(pUesto==3):
        #iDnt=Clase_Admin_Productos.Admin_producto(nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        edit[iDnt]={'ID':iDnt,'Nombre':nAme,'Apellido':fName,'Edad':aGe,'Telefono':tEl,'Correo':cOrreo,'Codigo-Postal':COdPos,'RFC':rFc,'Puesto':3,'Entrada':jOrnada_i,'Salida':jornada_f,'Salario':sAlario,'Contrasena':pAssword}      
    elif(pUesto==4):
        #iDnt=Clase_Gerente_general.Gerente(nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        edit[iDnt]={'ID':iDnt,'Nombre':nAme,'Apellido':fName,'Edad':aGe,'Telefono':tEl,'Correo':cOrreo,'Codigo-Postal':COdPos,'RFC':rFc,'Puesto':4,'Entrada':jOrnada_i,'Salida':jornada_f,'Salario':sAlario,'Contrasena':pAssword}        
    elif(pUesto==5):
        #iDnt=Clase_Obreor.Obrero(nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        edit[iDnt]={'ID':iDnt,'Nombre':nAme,'Apellido':fName,'Edad':aGe,'Telefono':tEl,'Correo':cOrreo,'Codigo-Postal':COdPos,'RFC':rFc,'Puesto':5,'Entrada':jOrnada_i,'Salida':jornada_f,'Salario':sAlario,'Contrasena':pAssword}        
    else:
        pass

f=open("EMPLEADOS.dat",'w')
cadena=json.dumps(edit)
f.write(cadena)
f.close()
    
