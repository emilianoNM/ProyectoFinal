#import Clase_RecHum
import Contratacion_RecHum
import Edicion_RecHum
import Despido_RecHum
#import Archivo de ventana

def Ventana():
    #Apertura de ventana
    pass

def Menu_principal(op):
    if (op==1):
        Contratacion_RecHum.contratacion()
    elif (op==2):
        Despido_RecHum.despido()
    elif (op==3):
        Edicion_RecHum.edicion_carga()

    