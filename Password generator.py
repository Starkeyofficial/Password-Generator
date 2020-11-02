from password_generator import PasswordGenerator
password=PasswordGenerator()
password.minlen=5
password.maxlen=8
password.minuchars=1
def create():
    result=password.generate()
    pw.insert(0,result)
def delete1():
    pw.delete(0,END)
from tkinter import *
master=Tk()
master.title("Password Generator")
label1=Label(master,text="Password Generator",font=("Helvetica",15,"bold"))
pw=Entry(master)
Generate=Button(master,text="Generate",command=create)
Clear=Button(master,text="Clear",command=delete1)
label1.grid(row=0,column=0)
pw.grid(row=1,column=0)
Generate.grid(row=2,column=0)
Clear.grid(row=3,column=0)
master.mainloop()