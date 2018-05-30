# importar todos los modulos
from tkinter import *
import sqlite3
import tkinter.messagebox
from update import database1


conn = sqlite3.connect("C:\Store Management Software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
     id = r[0]

class Database:
     def __init__(self, master, *args, **kwargs):

          self.master = master
          self.heading = Label(master, text="Agregar a la base de datos", font=('arial 40 bold'), fg='steelblue')
          self.heading.place(x=350, y=0)

          # labels para la ventana
          self.name_l = Label(master, text="Ingresa el Nombre del Producto", font=('arial 18 bold'))
          self.name_l.place(x=0, y=70)

          self.stock_l = Label(master, text="Ingresa la Cantidad de Producto", font=('arial 18 bold'))
          self.stock_l.place(x=0, y=120)

          self.cp_l = Label(master, text="Ingresa el Costo del Producto", font=('arial 18 bold'))
          self.cp_l.place(x=0, y=170)

          self.sp_l = Label(master, text="Ingresa el Precio del Producto", font=('arial 18 bold'))
          self.sp_l.place(x=0, y=220)

          self.vendor_l = Label(master, text="Ingresa el Proveedor del Producto", font=('arial 18 bold'))
          self.vendor_l.place(x=0, y=270)

          self.vendor_phone_l = Label(master, text="Ingresa el Numero del Proveedor del Producto", font=('arial 18 bold'))
          self.vendor_phone_l.place(x=0, y=320)

          self.id_l = Label(master, text="Ingresa el ID", font=('arial 18 bold'))
          self.id_l.place(x=0, y=370)

          # entradas de los labels
          self.name_e = Entry(master, width=25, font=('arial 18 bold'))
          self.name_e.place(x=600, y=70)

          self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
          self.stock_e.place(x=600, y=120)

          self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
          self.cp_e.place(x=600, y=170)

          self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
          self.sp_e.place(x=600, y=220)

          self.vendor_e = Entry(master, width=25, font=('arial 18 bold'))
          self.vendor_e.place(x=600, y=270)

          self.vendor_phone_e = Entry(master, width=25, font=('arial 18 bold'))
          self.vendor_phone_e.place(x=600, y=320)

          self.id_e = Entry(master, width=25, font=('arial 18 bold'))
          self.id_e.place(x=380, y=370)

          # boton para agregar a la base de datos
          self.btn_add = Button(master, text="Agregar a la base de datos", width=25, height=2, bg='steelblue', fg='white', command=self.abrir)
          self.btn_add.place(x=520, y=420)

          # boton para limpiar todos los campos
          self.btn_clear = Button(master, text="Limpiar todos los campos", width=18, height=2, bg='lightgreen', fg='white', command=self.clear_all)
          self.btn_clear.place(x=350, y=420)

          # text box para las subidas
          self.tBox = Text(master, width=50, height=18)
          self.tBox.place(x=950, y=70)
          self.tBox.insert(END, "ID ha alcanzado el numero: " + str(id))

          self.master.bind('<Return>', self.get_items)
          self.master.bind('<Up>', self.clear_all)
     def get_items(self, *args, **kwargs):
          # get de las entradas
          self.name = self.name_e.get()
          self.stock = self.stock_e.get()
          self.cp = self.cp_e.get()
          self.sp = self.sp_e.get()
          self.vendor = self.vendor_e.get()
          self.vendor_phone = self.vendor_phone_e.get()

          # entradas dinamicas
          self.totalcp = float(self.cp) * float(self.stock)
          self.totalsp = float(self.sp) * float(self.stock)
          self.assumed_profit = float(self.totalsp - self.totalcp)

          if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '':
               tkinter.messagebox.showinfo("Error", "Por favor, llene todos los campos.")
          else:
               sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vendor, vendor_phoneno ) VALUES(?,?,?,?,?,?,?,?,?)"
               c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vendor, self.vendor_phone))
               conn.commit()
               # textbox insertar
               self.tBox.insert(END, "\n\nInsertado " + str(self.name) + " a la base de datos con codigo " + str(self.id_e.get()))

               tkinter.messagebox.showinfo("Victoria", "Correctamente añadido a la base de datos.")
     def clear_all(self, *args, **kwargs):
          self.name_e.delete(0, END)
          self.stock_e.delete(0, END)
          self.cp_e.delete(0, END)
          self.sp_e.delete(0, END)
          self.vendor_e.delete(0, END)
          self.vendor_phone_e.delete(0, END)
          self.id_e.delete(0, END)

     def abrir(self):
                n=Toplevel(self.master1)
                database1(n)
root = Tk()
b = Database(root)

root.geometry("1366x768+0+0")
root.title("Agregar a la base de datos")
root.mainloop()

#database1().mainloop()
