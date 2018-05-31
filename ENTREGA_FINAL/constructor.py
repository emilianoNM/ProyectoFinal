
import Clase_RecHum
import Clase_Contador
import Clase_Admin
import Clase_Gerente
import Clase_Obrero

import pickle
import json

from tkinter import *
from tkinter import messagebox


def construye(pUesto,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,jOrnada_i,jOrnada_f,sAlario,iDnt): 
    if(pUesto=="1"):
        TTD=Clase_RecHum.RecHuman(iDnt,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        TTD.save()
        messagebox.showinfo("Terminado","Nuevo trabajador de Recursos Humanos agregado")
    elif(pUesto=="2"):
        TTD=Clase_Contador.Contador(iDnt,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        TTD.save()
        messagebox.showinfo("Terminado","Nuevo Contador contratado")
    elif(pUesto=="3"):
        TTD=Clase_Admin.Admin_producto(iDnt,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        TTD.save()
        messagebox.showinfo("Terminado","Nuevo Administrador contratado")
    elif(pUesto=="4"):
        TTD=Clase_Gerente.Gerente(iDnt,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        TTD.save()
        messagebox.showinfo("Terminado","Nuevo Gerente contratado")
    elif(pUesto=="5"):
        TTD=Clase_Obrero.Obrero(iDnt,nAme,fNameP,fNameM,dIreccion,tEl,aGe,cOrreo,rFc,pAssword,COdPos,pUesto,jOrnada_i,jOrnada_f,sAlario)
        TTD.save()
        messagebox.showinfo("Terminado","Nuevo Obrero contratado")
    else:
        pass
    pass
    
