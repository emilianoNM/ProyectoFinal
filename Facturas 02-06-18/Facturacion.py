
from tkinter import *
from tkinter import messagebox

lista = []
def guardar():
    n = nombre.get()
    ap = apellidos.get()
    rf = rfc.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+"$"+ap+"$"+rf+"$"+t+"$"+c)
    escribirContacto()
    messagebox.showinfo("Guardado","Los datos del cliente han sido guardados con exito")
    nombre.set("")
    apellidos.set("")
    rfc.set("")
    correo.set("")
    telefono.set("")
    consultar()
def eliminar():
    eliminado = conteliminar.get()
    removido = False
    
   

    for elemento in lista:
        arreglo = elemento.split("$")
        if conteliminar.get() == arreglo[0]:
            removido=messagebox.askyesno("Eliminar","¿Seguro que deseas eliminar?")
            lista.remove(elemento)
            removido = True
    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo("Eliminar",eliminado+" ha sido eliminado")

def consultar():
    r = Text(ventana, width=85, height=15)
    lista.sort()
    valores = []
    r.insert(INSERT, "Nombre\t\tApellidos\t\tRFC\t\tTeléfono\t\tCorreo\n")
    for elemento in lista:
       arreglo = elemento.split("$")
       valores.append(arreglo[0])
       r.insert(INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\n")
    r.place(x=20,y=250)
    spinNombre = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=500,y=50)
    if lista ==[]:
        spinNombre = Spinbox(ventana, value=(valores)).place(x=500,y=50)
    r.config(state=DISABLED)

def iniciarArchivo():
    archivo = open("Factura.txt","a")
    archivo.close()

def cargar():
   archivo = open("Factura.txt","r")
   linea = archivo.readline()
   if linea:
       while linea:
          if linea[-1]=='\n':
               linea = linea[:-1]
          lista.append(linea)
          linea = archivo.readline()
   archivo.close()

def escribirContacto():
     archivo = open("Factura.txt","w")
     lista.sort()
     for elemento in lista:
       archivo.write(elemento+"\n")
     archivo.close()

def salir():   
    sal=messagebox.askyesno("Salir","¿Seguro que deseas salir?")
    if sal==True:
       quit() 

ventana = Tk()
nombre = StringVar()
apellidos = StringVar()
rfc = StringVar()
correo = StringVar()
telefono = StringVar()
conteliminar = StringVar()
colorFondo = "#B22222"
colorLetra = "#FFF"
iniciarArchivo()
cargar()
consultar()
ventana.title("Facturas")
ventana.geometry("1000x600")
ventana.configure(background = colorFondo)
etiquetaTitulo = Label(ventana, text="Datos del cliente",
  bg=colorFondo, fg=colorLetra).place(x=50,y=10)
etiquetaN = Label(ventana, text="Nombre", bg=colorFondo,
  fg=colorLetra).place(x=50, y=50)
cajaN = Entry(ventana, textvariable=nombre).place(x=150, y=50)
etiquetaApp = Label(ventana, text="Apellidos", bg=colorFondo,
  fg=colorLetra).place(x=50, y=80)
cajaApp = Entry(ventana, textvariable=apellidos).place(x=150, y=80)
etiquetaRFC = Label(ventana, text="RFC", bg=colorFondo,
  fg=colorLetra).place(x=50, y=110)
cajaRFC = Entry(ventana, textvariable=rfc).place(x=150, y=110)
etiquetaT = Label(ventana, text="Teléfono", bg=colorFondo,
  fg=colorLetra).place(x=50, y=140)
cajaT = Entry(ventana, textvariable=telefono).place(x=150, y=140)
etiquetaC = Label(ventana, text="Correo", bg=colorFondo,
  fg=colorLetra).place(x=50, y=170)
cajaC = Entry(ventana, textvariable=correo).place(x=150, y=170)
etiquetaEliminar = Label(ventana, text="Seleccionar cliente: ", bg= colorFondo,
  fg=colorLetra).place(x=370, y=50)

botoGuardar = Button(ventana, text="Guardar", command=guardar, bg="#009",
  fg="white").place(x=180, y=200)
botoEliminar = Button(ventana, text="Eliminar",command=eliminar, bg="#009",
  fg="white").place(x=700, y=50)
boton3=Button (ventana,text="Salir",fg="red",command=salir).place(x=50,y=500)

mainloop()
