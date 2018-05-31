# importar todos los modulos
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("C:\Store Management Software\Database\store.db")
c = conn.cursor()

# date
date = datetime.datetime.now().date()

# sesiones tipo lista temporales
products_list = []
product_price = []
product_quantity = []
product_id = []

# lista para los labels
labels_list = []

class Application:
	def __init__(self, master, *args, **kwargs):
		self.master = master
		# frames
		self.left = Frame(master, width=700, height=768, bg='white')
		self.left.pack(side=LEFT)

		self.right = Frame(master, width=666, height=768, bg='lightblue')
		self.right.pack(side=RIGHT)

		# componentes
		self.heading = Label(self.left, text="Tienda de técnicas", font=('arial 40 bold'), bg='white')
		self.heading.place(x=0, y=0)

		self.date_l = Label(self.right, text="Fecha de hoy: " + str(date), font=('arial 16 bold'), bg='lightblue', fg='white')
		self.date_l.place(x=0, y=0)

		# nota tabla========================================================================================================
		self.tproduct = Label(self.right, text="Productos", font=('arial 18 bold'), bg='lightblue', fg='white')
		self.tproduct.place(x=0, y=60)

		self.tquantity = Label(self.right, text="Cantidad", font=('arial 18 bold'), bg='lightblue', fg='white')
		self.tquantity.place(x=300, y=60)

		self.tamount = Label(self.right, text="Monto", font=('arial 18 bold'), bg='lightblue', fg='white')
		self.tamount.place(x=500, y=60)

		# ingresar cosas
		self.enterid = Label(self.left, text="Ingresa el ID del producto", font=('arial 18 bold'), bg='white')
		self.enterid.place(x=0, y=80)

		self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
		self.enteride.place(x=320, y=80)
		self.enteride.focus()

		# boton
		self.search_btn = Button(self.left, text="Buscar", width=22, height=2, bg='orange', command=self.ajax)
		self.search_btn.place(x=480, y=120)

		# se llena despues con la funcion ajax
		self.productname = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='steelblue')
		self.productname.place(x=0, y=250)

		self.pprice = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='steelblue')
		self.pprice.place(x=0, y=290)


		# label del total
		self.total_l = Label(self.right, text="", font=('arial 40 bold'), bg='lightblue', fg='white')
		self.total_l.place(x=0, y=600)

		self.master.bind("<Return>", self.ajax)
		self.master.bind("<Up>", self.add_to_cart)
		self.master.bind("<space>", self.generate_bill)


	def ajax(self, *args, **kwargs):
		self.get_id = self.enteride.get()
		# above get la info de los productos con esa ID y llena los labels arriba
		query = "SELECT * FROM inventory WHERE id=?"
		result = c.execute(query, (self.get_id))
		for self.r in result:
			self.get_id = self.r[0]
			self.get_name = self.r[1]
			self.get_price = self.r[4]
			self.get_stock = self.r[2]
		self.productname.configure(text="Nombre del producto: " + str(self.get_name))
		self.pprice.configure(text="Precio: Rs. " + str(self.get_price))

		# crea los labels de cantidad y descuento
		self.quantity_l = Label(self.left, text="Ingresar cantidad", font=('arial 18 bold'), bg='white')
		self.quantity_l.place(x=0, y=370)

		self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
		self.quantity_e.place(x=230, y=370)
		self.quantity_e.focus()

		# descuento
		self.discount_l = Label(self.left, text="Ingresar descuento", font=('arial 18 bold'), bg='white')
		self.discount_l.place(x=0, y=410)

		self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
		self.discount_e.place(x=230, y=410)
		self.discount_e.insert(END, 0)

		# boton para añadir al carrito
		self.add_to_cart_btn = Button(self.left, text="Agregar al carrito", width=22, height=2, bg='orange', command=self.add_to_cart)
		self.add_to_cart_btn.place(x=390, y=450)

		# generar nota y cambio
		self.change_l = Label(self.left, text="Cantidad otorgada", font=('arial 18 bold'), bg='white')
		self.change_l.place(x=0, y=550)

		self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
		self.change_e.place(x=230, y=550)

		# boron de cambio
		self.change_btn = Button(self.left, text="Calcular cambio", width=22, height=2, bg='orange', command=self.change_func)
		self.change_btn.place(x=390, y=590)

		# boton de generar nota
		self.bill_btn = Button(self.left, text="Generar nota", width=100, height=2, bg='red', fg='white', command=self.generate_bill)
		self.bill_btn.place(x=0, y=640)


	def add_to_cart(self, *args, **kwargs):
		# get el valor de la cantidad de la base de datos
		self.quantity_value = int(self.quantity_e.get())
		if self.quantity_value > int(self.get_stock):
			tkinter.messagebox.showinfo("Error", "No hay tantos productos en el inventario.")
		else:
			# calcula el precio
			self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))

			products_list.append(self.get_name)
			product_price.append(self.final_price)
			product_quantity.append(self.quantity_value)
			product_id.append(self.get_id)

			self.x_index = 0
			self.y_index = 100
			self.counter = 0
			for self.p in products_list:
				self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
				self.tempname.place(x=0, y=self.y_index)
				labels_list.append(self.tempname)

				self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
				self.tempqt.place(x=300, y=self.y_index)
				labels_list.append(self.tempqt)

				self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='white')
				self.tempprice.place(x=500, y=self.y_index)
				labels_list.append(self.tempprice)

				self.y_index += 40
				self.counter +=1

				# configuracion del total
				self.total_l.configure(text="Total: Rs. " + str(sum(product_price)))

				# elimina
				self.quantity_l.place_forget()
				self.quantity_e.place_forget()
				self.discount_l.place_forget()
				self.discount_e.place_forget()
				self.productname.configure(text="")
				self.pprice.configure(text="")
				self.add_to_cart_btn.destroy()

				# autofocus a ingresar el ID
				self.enteride.focus()
				self.enteride.delete(0, END)


	def change_func (self, *args, **kwargs):
		# get la camtidad dada por el cliente y la cantidad generada por la computadora
		self.amount_given = float(self.change_e.get())
		self.our_total = float(sum(product_price))

		self.to_give = self.amount_given - self.our_total

		# label para cambio
		self.c_amount = Label(self.left, text="Cambio: " + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
		self.c_amount.place(x=0, y=600)

	def generate_bill(self, *args, **kwargs):

		# crear la nota antes de actualizar la base de datos
		directory = "C:/Store Management Software/Invoice/" + str(date) + "/"
		if not os.path.exists(directory):
			os.makedirs(directory)

		# INFO PARA LA NOTA
		company = "\t\t\t\tTecnicas de Programacion\n"
		adress = "\t\t\t\t\tCU, FI, CDMX\n"
		phone = "\t\t\t\t\t01800TECNICAS\n"
		sample = "\t\t\t\t\tNota\n"
		dt = "\t\t\t\t\t" + str(date)

		table_header = "\n\n\t\t\t--------------------------------------------------\n\t\t\tSN. \tProductos\t\tCant.\t\tMonto\n\t\t\t--------------------------------------------------"
		final = company + adress + phone + sample + dt + "\n" + table_header

		# abre un archivo para escribir en el
		file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
		f = open(file_name, 'w')
		f.write(final)
		# dinamicas de llenado
		r = 1
		i = 0
		for t in products_list:
			f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + ".......")[:7] + "\t\t" + str(product_quantity[i]) + "\t\t" + str(product_price[i]))
			i += 1
			r += 1
		f.write("\n\n\t\t\tTotal: Rs. " + str(sum(product_price)))
		f.write("\n\t\t\tGracias por visitar.")
		os.startfile(file_name, "print")
		f.close()


		# decrementar la cantidad
		self.x = 0

		initial = "SELECT * FROM inventory WHERE id=?"
		result = c.execute(initial, (product_id[self.x], ))
		
		for i in products_list:
			for r in result:
				self.old_stock = r[2]
			self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

			# actualizar la cantidad

			sql = "UPDATE inventory SET stock=? WHERE id=?"
			c.execute(sql, (self.new_stock, product_id[self.x]))
			conn.commit()

			# insterar a la transaccion
			sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
			c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
			conn.commit()
			
			self.x +=1

		for a in labels_list:
			a.destroy()

		del(products_list[:])
		del(product_id[:])
		del(product_quantity[:])
		del(product_price[:])

		self.total_l.configure(text="")
		self.c_amount.configure(text="")
		self.change_e.delete(0, END)
		self.enteride.focus()
		tkinter.messagebox.showinfo("Victoria", "Todo hecho muy bien")


root = Tk()
b = Application(root)

root.geometry("1366x768+0+0")
root.mainloop()