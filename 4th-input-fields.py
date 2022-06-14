from tkinter import *

root=Tk()

e = Entry(root,width=20,fg="black",bg="grey",borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def myclick():
    hello="Hello "+e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myclick)
myButton.pack()

root.mainloop()
