from tkinter import *
def Mysel():
    dic = {0:'money',1:'right',2:'apperance'}
    s = "your choice is "+dic.get(var.get())
    lb.config(text = s)

root = Tk()
root.title('choice game')
root.geometry("460x240")
lb = Label(root)
lb.pack()
var = IntVar()
rd1 = Radiobutton(root,text='money',variable=var,value=0,command=Mysel)
rd1.pack()
rd2 = Radiobutton(root,text='right',variable=var,value=1,command=Mysel)
rd2.pack()
rd3 = Radiobutton(root,text='appearence',variable=var,value=2,command=Mysel)
rd3.pack()
root.mainloop()