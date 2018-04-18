from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.pack()
        self.etiqueta = Label(root, text="etiqueta")
        self.etiqueta.grid(row=0,column=0)
        self.etiqueta2 = Label(root, text="etiqueta2")
        self.etiqueta2.grid(row=1,column=0)
        #self.etiqueta.pack()


        self.entrythingy = Entry()
        #self.entrythingy.pack(padx=1, pady=2)
        self.entrythingy.grid(row=0,column=1)
        self.entrythingy2 = Entry()
        self.entrythingy2.grid(row=1,column=1)
        #self.entrythingy2.pack(padx=5, pady=10)
        
        # here is the application variable
        self.contents = StringVar()
        self.contents2 = StringVar()
        
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy2["textvariable"] = self.contents2

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.submitButton = Button(master, command=self.buttonClick, text="Submit")
        #self.submitButton.bind('<Enter>',self.buttonClick)
        self.submitButton["command"]==self.buttonClick
        #self.submitButton.pack()
        self.submitButton.grid(row=2,column=1)
    def buttonClick(self):
        """ handle button click event and output text from entry area"""
        print ("Informacion del campo de texto")
        print (self.contents.get())
        


root = Tk()
app = App(master=root)

print (dir(app))
app.mainloop()
root.destroy()