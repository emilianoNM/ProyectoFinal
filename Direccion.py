import json
#import Clase_Persona
#import Clase_Empleado
import Main_RecHum
import Main_Admin
import Main_Gerente
import Main_Obrero

def direccion(permiso):
    if permiso==1:
        Main_RecHum.Ventana()
        pass
    elif permiso==2:
        Main_Contador.Ventana()
        pass
    elif permiso==3:
        Main_Admin.Ventana()
        pass
    elif permiso==4:
        Main_Gerente.Ventana()
        pass
    elif permiso==5:
        Main_Obrero.Ventana()
        pass
        