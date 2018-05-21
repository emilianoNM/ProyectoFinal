from tkinter import *

def lista():
    
    root = tkinter.Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    mylist = Listbox(root, yscrollcommand = scrollbar.set )
    for line in range(75012345120,75012345141,1):
       mylist.insert(END, "Producto " + str(line))

    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )

    root.mainloop()
