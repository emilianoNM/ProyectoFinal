

import json

def DspVentana():
    #abre la ventana
    pass

    
    
def despido(ID):
    f=open("EMPLEADOS.dat",'r')
    empChain=f.read()
    empRec=json.loads(empChain)

    print("Despidiendo a: "+ID)
    del empRec[ID]
    
    
    f2=open("EMPLEADOS.dat",'w')
    empcadena=json.dumps(empRec)
    f2.write(empcadena)
    f2.close    
    pass  
