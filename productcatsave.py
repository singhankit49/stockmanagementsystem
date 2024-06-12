import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productcatsavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product category')
    def checkdata():
        xa=int(aa.get())
        if xa>0:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from productcategory where pcatid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
        else:
            messagebox.showerror('Hi','Product id cannot be negative')
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0:
            messagebox.showerror('Hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="insert into productcategory values(%d,'%s','%s')"%(xa,xb,xc) 
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Saved')
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            
    def close():
        t.destroy()
        
    a1=Label(t,text='PRODUCT CATEGORY- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=200,y=25) 
    a=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=300,y=100)
    aab=Button(t,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
    aab.place(x=575,y=100)
    b=Label(t,text='CATEGORY NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=300,y=150)
    c=Label(t,text='DESCRIPTION',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=300,y=200)
    e=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    e.place(x=305,y=250)
    f=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    f.place(x=385,y=250)
    t.mainloop()
