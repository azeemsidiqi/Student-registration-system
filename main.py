from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("Registration Form")
win.geometry("400x400")
win.resizable(False,False)

def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    
    if name=="":
        messagebox.showerror("Enter","Pleae enter the name")
    elif age=="":
        messagebox.showerror("Enter","Pleae enter the age")
    elif phone=="":
        messagebox.showerror("Enter","Pleae enter the phone number")
    elif email=="":
        messagebox.showerror("Enter","Pleae enter the email")
    else:
        Label(win,text="Registration Successful",font="20",fg="green").place(x=135,y=285)

    with open(name+".txt","w") as f:
        f.write(name+"\n")
        f.write(age+"\n")
        f.write(phone+"\n")
        f.write(email+"\n")

def clear():
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    email_entry.delete(0,END)

Label(win,text="Registration Form",font="ariel 20 bold",bg="red",fg="white").pack(fill="both")

Label(win,text="Name",font="20").place(x=40,y=75)
Label(win,text="age",font="20").place(x=40,y=115)
Label(win,text="Phone No.",font="20").place(x=40,y=155)
Label(win,text="email Id",font="20").place(x=40,y=195)

name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()

name_entry=Entry(win,font="10",bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)
age_entry=Entry(win,font="10",bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)
phone_entry=Entry(win,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)
email_entry=Entry(win,font="10",bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)

Button(win,text="Register",font="20",command=register).place(x=185,y=255)
Button(win,text="Clear",font="20",command=clear).place(x=330,y=355)

mainloop()



