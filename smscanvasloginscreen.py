import tkinter
from tkinter import *
from tkinter import ttk
from finalsmscanvasdashboardadmin import *
from finalsmscanvasdashboarduser import *
from tkinter import messagebox

t=tkinter.Tk()
t.geometry('800x800')
def login():
    r=aa.get()
    s=bb.get()
    if r=='admin' and s=='123':                 
        t.destroy()
        command=finalsmscanvasdashboardadmin()
        
    elif r=='user' and s=='456':
        t.destroy()
        command=finalsmscanvasdashboarduser()
        
    else:
        messagebox.showinfo('hi','Failed')
    
def close():
    t.destroy()

t.title('SMS LOGIN')

a1=Label(t,text='LOGIN SCREEN',font=('times new roman bold',20))
a1.place(x=300,y=10)
a=Label(t,text='USERNAME',font=('times new roman bold',13))
a.place(x=100,y=100)
aa=Entry(t,width=20)
aa.place(x=300,y=100)
b=Label(t,text='PASSWORD',font=('times new roman bold',13))
b.place(x=100,y=150)
bb=Entry(t,width=20,show='*')
bb.place(x=300,y=150)

g=Button(t,text='LOGIN',font=('times new roman bold',11),fg='black',bg='skyblue',command=login)
g.place(x=100,y=300)
i=Button(t,text='CANCEL',font=('times new roman bold',11),fg='black',bg='red',command=close)
i.place(x=200,y=300)

t.mainloop()