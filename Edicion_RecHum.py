#import Clase_Empleados
#import Clase_RecHum
import Main_RecHum
import json

#Por aniadr metodo de captura de entradas de interfaz
def edicion_carga(IDNT):
    
    f=open("EMPLEADOS.dat",'r')
    empChain=f.read()
    empRec=json.loads(empChain)

    Id=empRec[IDNT]['ID']
    Name=empRec[IDNT]['Nombre']
    lName=empRec[IDNT]['Apellido']
    age=empRec[IDNT]['Edad']
    phone=empRec[IDNT]['Telefono']
    mail=empRec[IDNT]['Correo']
    code=empRec[IDNT]['Codigo-Postal']
    registry=empRec[IDNT]['RFC']
    spot=empRec[IDNT]['Puesto']
    entrance=empRec[IDNT]['Entrada']
    leaving=empRec[IDNT]['Salida']
    payment=empRec[IDNT]['Salario']
    passw=empRec[IDNT]['Contrasena']
    
    return (Id, Name, lName, age, phone, mail, code, registry, spot, entrance, leaving, payment, passw)

def edicion_nuevo(pUesto,nAme,fName,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,jOrnada_i,jOrnada_f,sAlario,iDnt):
    f=open("EMPLEADOS.dat",'r')
    empChain=f.read()
    empRec=json.loads(empChain)
    
    empRec[IDNT]['ID']=iDnt
    empRec[IDNT]['Nombre']=nAme
    empRec[IDNT]['Apellido']=fName
    empRec[IDNT]['Edad']=aGe
    empRec[IDNT]['Telefono']=tEl
    empRec[IDNT]['Correo']=cOrreo
    empRec[IDNT]['Codigo-Postal']=COdPos
    empRec[IDNT]['RFC']=rFc
    empRec[IDNT]['Puesto']=pUesto
    empRec[IDNT]['Entrada']=jOrnada_i
    empRec[IDNT]['Salida']=jOrnada_f
    empRec[IDNT]['Salario']=sAlario
    empRec[IDNT]['Contrasena']=pAssword
    
    f2=open("EMPLEADOS.dat",'w')
    empcadena=json.dumps(empRec)
    f2.write(empcadena)
    f2.close
    pass
    
