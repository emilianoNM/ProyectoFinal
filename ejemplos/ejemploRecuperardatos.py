import tkinter as tk
from tkinter import *





root = Tk()
root.title('how to get text from textbox')

mystring = StringVar()
mystring2 = StringVar()
back = tk.Frame(master=root, width=500, height=500, bg='black')
back.pack()

def cargarDato():
    jsonobj={"1":"dato", "2":"info" }
    datoDeVariable=mystring.get()
   

    mystring2.set(jsonobj[datoDeVariable])


go = tk.Button(master=back, text='Cargar Dato', bg='black', fg='red',
                     command=lambda:cargarDato()).pack()
close = tk.Button(master=back, text='Quit', bg='black', fg='red',
                     command=lambda:quit()).pack()
info = tk.Label(master=back, text='Made by me!', bg='red',
                         fg='black').pack()


entry=Entry(root, textvariable = mystring ).pack() 

entry2=Entry(root, textvariable = mystring2 ).pack() 

root.mainloop()
