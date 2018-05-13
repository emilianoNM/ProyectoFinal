#import Clase_Empleados
#import Clase_RecHum
import Main_RecHum


def despido(ID):
    f=open("EMPLEADOS.dat",'r')
    empChain=f.read()
    empRec=json.loads(empChain)
    
    del empRec[ID]
    
    f2=open("EMPLEADOS.dat",'w')
    empcadena=json.dumps(empRec)
    f2.write(empcadena)
    f2.close    
    pass  