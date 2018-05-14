#Avance de interfaz1.0


from tkinter import *

class main(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master.title("Productos :)")
        self.master.geometry("400x250")
        self.valor = StringVar()
        self.valor.set("\n Hola \n Buen día ü \n \n Puedes iniciar sesión \n o\n crear una cuenta \n")
        Label(self.master, textvariable=self.valor).pack()
        Button(root, text="Iniciar Sesión", fg="blue", command=self.iniciar).pack()
        Button(root, text="Crear una cuenta", fg="blue", command=self.crear).pack()

    def iniciar(self):
        i = compras(root, self.valor, "Inicia Sesión", "Usuario")
        root.wait_window(i.top)
        

    def crear(self):
      i = compras(root, self.valor, "Inicia Sesión", "Usuario")
        #root.wait_window(i.top)
     #   tkMessageBox.showinfo("Crea tu propia cuenta", "Llena los campos con tus datos")

        
class compras:
    def __init__(self, parent, valor, title, labeltext = '' ):
        self.valor = valor
 
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(title) > 0: self.top.title(title)
        if len(labeltext) == 0: labeltext = 'Valor'
        Label(self.top, text=labeltext).pack()
        self.top.bind("<Return>", self.ok)
        self.e = Entry(self.top, text=valor.get())
        self.e.bind("<Return>", self.ok)
        self.e.bind("<Escape>", self.cancel)
        self.e.pack(padx=15)
        self.e.focus_set()
        b = Button(self.top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self, event=None):
        print ("Has escrito ...", self.e.get())
        self.valor.set(self.e.get())
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()


    
 
root = Tk()
a = main(root)
root.mainloop()
