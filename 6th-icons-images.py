from tkinter import *
from PIL import ImageTK,Image

root=Tk()

root.title("Learn to code at codemy.com ")
#root.iconbitmap('C:\Users\mbarh\Downloads\python.png')

my_img= ImageTK.photoImage(Image.open("E:\pycharm\pics"))
my_label=Label(image=my_img)
my_label.pack()

root.mainloop()



button_quit=Button(root,text="Exit program",command=root.quit)
button_quit.pack()
root.mainloop()
