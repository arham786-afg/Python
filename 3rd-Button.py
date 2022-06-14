from tkinter import *

root = Tk()


def myclick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myclick, fg="black", bg="blue")
myButton.pack()

root.mainloop()
