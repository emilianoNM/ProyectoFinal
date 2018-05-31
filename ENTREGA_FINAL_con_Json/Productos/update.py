# importar todos los modulos
from tkinter import *
import sqlite3
import tkinter.messagebox



conn = sqlite3.connect("C:\Store Management Software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT Max(id) from inventory")
for r in result:
	id = r[0]

class database1(Frame):
	def __init__(self, master1=None, *args, **kwargs):

		Frame.__init__(self, master1=None)
		self.master1 = master1
		self.heading = Label(master1, text="Actualiza la base de datos", font=('arial 40 bold'), fg='steelblue')
		self.heading.place(x=350, y=0)

		# label y entrada del ID
		self.id_le = Label(master1, text="Ingresa ID", font=('arial 18 bold'))
		self.id_le.place(x=0, y=70)

		self.id_leb = Entry(master1, fon=('arial 18 bold'), width=10)
		self.id_leb.place(x=600, y=70)

		self.btn_search = Button(master1, text="Buscar", width=15, height=2, bg='orange', command=self.search)
		self.btn_search.place(x=750, y=70)

		# labels para la ventana
		self.name_l = Label(master1, text="Ingresa el Nombre del Producto", font=('arial 18 bold'))
		self.name_l.place(x=0, y=120)

		self.stock_l = Label(master1, text="Ingresa la Cantidad de Producto", font=('arial 18 bold'))
		self.stock_l.place(x=0, y=170)

		self.cp_l = Label(master1, text="Ingresa el Costo del Producto", font=('arial 18 bold'))
		self.cp_l.place(x=0, y=220)

		self.sp_l = Label(master1, text="Ingresa el Precio del Producto", font=('arial 18 bold'))
		self.sp_l.place(x=0, y=270)

		self.totalcp_l = Label(master1, text="Ingresa el Costo Total del Producto", font=('arial 18 bold'))
		self.totalcp_l.place(x=0, y=320)

		self.totalsp_l = Label(master1, text="Ingresa el Precio Total del Producto", font=('arial 18 bold'))
		self.totalsp_l.place(x=0, y=370)

		self.vendor_l = Label(master1, text="Ingresa el Proveedor del Producto", font=('arial 18 bold'))
		self.vendor_l.place(x=0, y=420)

		self.vendor_phone_l = Label(master1, text="Ingresa el Numero del Proveedor del Producto", font=('arial 18 bold'))
		self.vendor_phone_l.place(x=0, y=470)

		# entries para los labels
		self.name_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.name_e.place(x=600, y=120)

		self.stock_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.stock_e.place(x=600, y=170)

		self.cp_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.cp_e.place(x=600, y=220)

		self.sp_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.sp_e.place(x=600, y=270)

		self.totalcp_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.totalcp_e.place(x=600, y=320)

		self.totalsp_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.totalsp_e.place(x=600, y=370)

		self.vendor_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.vendor_e.place(x=600, y=420)

		self.vendor_phone_e = Entry(master1, width=25, font=('arial 18 bold'))
		self.vendor_phone_e.place(x=600, y=470)

		# buoton para actualizar la base de datos
		self.btn_add = Button(master1, text="Actualizar la base de datos", width=25, height=2, bg='steelblue', fg='white', command=self.update)
		self.btn_add.place(x=520, y=520)

		# text box para las subidas
		self.tBox = Text(master1, width=50, height=18)
		self.tBox.place(x=950, y=70)
		self.tBox.insert(END, "ID ha alcanzado el numero: " + str(id))

	def search(self, *args, **kwargs):
		pass
		sql = "SELECT * FROM inventory WHERE id=?"
		result = c.execute(sql, (self.id_leb.get(), ))
		for r in result:
			self.n1 = r[1] #nombre
			self.n2 = r[2] #cantidad
			self.n3 = r[3] #costo
			self.n4 = r[4] #precio
			self.n5 = r[5] #costo total
			self.n6 = r[6] #precio total
			self.n7 = r[7] #ganancia esperada
			self.n8 = r[8] #proveedor
			self.n9 = r[9] #numero del proovedor
		conn.commit()

		# insertar a las entradas para actualizar
		self.name_e.delete(0, END)
		self.name_e.insert(0, str(self.n1))

		self.stock_e.delete(0, END)
		self.stock_e.insert(0, str(self.n2))

		self.cp_e.delete(0, END)
		self.cp_e.insert(0, str(self.n3))

		self.sp_e.delete(0, END)
		self.sp_e.insert(0, str(self.n4))

		self.vendor_e.delete(0, END)
		self.vendor_e.insert(0, str(self.n8))

		self.vendor_phone_e.delete(0, END)
		self.vendor_phone_e.insert(0, str(self.n9))

		self.totalcp_e.delete(0, END)
		self.totalcp_e.insert(0, str(self.n5))

		self.totalsp_e.delete(0, END)
		self.totalsp_e.insert(0, str(self.n6))

	def update(self, *args, **kwargs):
		# get todos los valores actualizados
		self.u1 = self.name_e.get()
		self.u2 = self.stock_e.get()
		self.u3 = self.cp_e.get()
		self.u4 = self.sp_e.get()
		self.u5 = self.totalcp_e.get()
		self.u6 = self.totalsp_e.get()
		self.u7 = self.vendor_e.get()
		self.u8 = self.vendor_phone_e.get()

		query = "UPDATE inventory SET name=?, stock=?, cp=?, sp=?, totalcp=?, totalsp=?, vendor=?, vendor_phoneno=? WHERE id=?"
		c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_leb.get()))
		conn.commit()
		tkinter.messagebox.showinfo("Victoria", "Actualizado a la base de datos")

root = Tk()
b = database1(root)

root.geometry("1366x768+0+0")
root.title("Actualiza la base de datos")
root.mainloop()
