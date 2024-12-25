from tkinter import *
from tkinter import font
from tkinter import messagebox
import pymysql
from tkinter import ttk
w=Tk()
w.geometry('800x600')
w.resizable(False,False)
w.title("contacts")
f1=font.Font(w,family="Baskerville Old Face",size=14)
f2=font.Font(w,family="Baskerville Old Face",size=24)
fr=Frame(w,bg="white",height=600,width=800)
fr2=Frame(w,bg="white",height=600,width=800)
fr3=Frame(w,bg="white",height=600,width=800)
r=StringVar()
v=StringVar()
r.set("Male")
v.set("Male")
cn=pymysql.connect(host="localhost",user="username",password="",database="databases")
cr=cn.cursor()
cr.execute("show databases")
try:
    qry1="create table contact(First_Name Varchar(20),Last_Name Varchar(20),Gender Varchar(10),Phone Varchar(10))"
    cr.execute(qry1)
except:
    cr.execute("SELECT * FROM contact")
def create():
    fr.grid_forget()
    fr2.grid()
    e1.focus_set()

def cancel():
    fr2.grid_forget()
    fr.grid()
def save():
        qry="insert into contact values('{}','{}','{}','{}')".format(e1.get(),e2.get(),r.get(),e3.get())
        cr.execute(qry)
        cn.commit()
        fr2.grid_forget()
        fr.grid()
        tree.insert('',j,text="",values=(e1.get(),e2.get(),r.get(),e3.get()))    
        messagebox.showinfo("Info","The Contact is Saved Successfully")
        e1.delete(0,END)
        e3.delete(0,END)
        e2.delete(0,END)
        r.set("Male")


            
def edit():
    select=tree.focus()
    values=tree.item(select,'values')
    tree.bind("<ButtonRelease-1>",select)
    if (len(values)>0):
        fr.grid_forget()
        fr3.grid()
        e4.insert(0,values[0])
        e5.insert(0,values[1])
        e6.insert(0,values[3])
        v.set(values[2])
    else:
        messagebox.showinfo("info","Select the name to edit")
    e4.focus_set()

def cancel1():
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        fr3.grid_forget()
        fr.grid()

def save1():
    select=tree.focus()
    values=tree.item(select,'values')
    qry="delete from contact where phone='{}'".format(values[3])
    cr.execute(qry)
    cn.commit()
    tree.delete(select)
    cr.execute("SELECT * FROM contact")
    qry="insert into contact values('{}','{}','{}','{}')".format(e4.get(),e5.get(),v.get(),e6.get())
    cr.execute(qry)
    cn.commit()
    fr3.grid_forget()
    fr.grid()
    tree.insert('',j,text="",values=(e4.get(),e5.get(),v.get(),e6.get()))
    e4.delete(0,END)
    e5.delete(0,END)
    v.set("Male")
    e6.delete(0,END)


def delete():
    select=tree.focus()
    values=tree.item(select,'values')
    if(len(values)>0):
        qry="delete from contact where phone='{}'".format(values[3])
        cr.execute(qry)
        cn.commit()
        messagebox.showinfo("Info","The Contact is deleted Successfully")
        tree.delete(select)
        cr.execute("SELECT * FROM contact")
    else:
        messagebox.showinfo("info","select any contact to delete")
        fr.grid()



Button(fr,text="Create +",fg="white",bd=0,bg="Green",font=f1,width=10,command=create).place(x=25,y=25)
Button(fr,text="Delete",fg="White",bg="Red",bd=0,font=f1,width=10,command=delete).place(x=650,y=25)
frm=Frame(fr,height=4,width=800,bg="Black").place(x=0,y=80)
Label(fr,text="Contacts",font=f2,fg="black",bg="white").place(x=350,y=25)
Button(fr,text="Edit",font=f1,width=10,bg="Blue",fg="white",command=edit).place(x=350,y=500)

tree=ttk.Treeview(fr)
tree["columns"]=("First_Name","Last_Name","Gender","Phone")
tree.column("#0",width=0,stretch=NO)
tree.column("First_Name",width=150,minwidth=100,anchor=CENTER)
tree.column("Last_Name",width=150,minwidth=100,anchor=CENTER)
tree.column("Gender",width=100,minwidth=50,anchor=CENTER)
tree.column("Phone",width=200,minwidth=150,anchor=CENTER)

tree.heading("First_Name",text="First Name",anchor=CENTER)
tree.heading("Last_Name",text="Last Name",anchor=CENTER)
tree.heading("Gender",text="Gender",anchor=CENTER)
tree.heading("Phone",text="Phone No",anchor=CENTER)
j=0
for ro in cr:
    tree.insert('',j,text="",values=(ro[0],ro[1],ro[2],ro[3]))
    j=j+1

tree.place(x=100,y=125)
fr.grid()

#Frame 2
Label(fr2,text="Create New Contacts",font=f2,fg="black",bg="white").place(x=25,y=25)
Label(fr2,text="First Name",fg="black",bg="white",font=f1).place(x=50,y=125)
Label(fr2,text="Last Name",fg="black",bg="white",font=f1).place(x=50,y=175)
Label(fr2,text="Gender",fg="black",bg="white",font=f1).place(x=50,y=225)
Label(fr2,text="Phone NO",fg="black",bg="white",font=f1).place(x=50,y=275)
r1=Radiobutton(fr2,text="Male",fg="black",bg="white",font=f1,variable=r,value="Male").place(x=200,y=225)
r2=Radiobutton(fr2,text="Female",fg="black",bg="white",font=f1,variable=r,value="Female").place(x=300,y=225)
e1=Entry(fr2,width=40,font=f1)
e1.place(x=200,y=125)

e2=Entry(fr2,width=40,font=f1)
e2.place(x=200,y=175)
e3=Entry(fr2,width=40,font=f1)
e3.place(x=200,y=275)
Button(fr2,text="Cancel",fg="white",bg="red",font=f1,width=10,bd=0,command=cancel).place(x=75,y=375)
Button(fr2,text="Save",fg="white",bg="blue",font=f1,width=10,bd=0,command=save).place(x=300,y=375)


#Frame3

Label(fr3,text="Editing Contacts",font=f2,fg="black",bg="white").place(x=25,y=25)
Label(fr3,text="First Name",fg="black",bg="white",font=f1).place(x=50,y=125)
Label(fr3,text="Last Name",fg="black",bg="white",font=f1).place(x=50,y=175)
Label(fr3,text="Gender",fg="black",bg="white",font=f1).place(x=50,y=225)
Label(fr3,text="Phone NO",fg="black",bg="white",font=f1).place(x=50,y=275)
r1=Radiobutton(fr3,text="Male",fg="black",bg="white",font=f1,variable=v,value="Male").place(x=200,y=225)
r2=Radiobutton(fr3,text="Female",fg="black",bg="white",font=f1,variable=v,value="Female").place(x=300,y=225)
e4=Entry(fr3,width=40,font=f1)
e4.place(x=200,y=125)

e5=Entry(fr3,width=40,font=f1)
e5.place(x=200,y=175)
e6=Entry(fr3,width=40,font=f1)
e6.place(x=200,y=275)
Button(fr3,text="Cancel",fg="white",bg="red",font=f1,width=10,bd=0,command=cancel1).place(x=75,y=375)
Button(fr3,text="Save",fg="white",bg="blue",font=f1,width=10,bd=0,command=save1).place(x=300,y=375)


w.mainloop()
