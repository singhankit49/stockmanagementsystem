import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def customersupdatescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('CUSTOMERS')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def checkdetail():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,address,phone,email from customers where custid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        db.close()
    
    def updatedata():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        xd=dd.get()
        xe=ee.get()
        if len(xd)!=10:
            messagebox.showerror('Hi','Enter valid Phone no.')
        elif not xd.isdigit():
            messagebox.showerror('Hi','Enter valid Phone no.')
        elif xe.count('@')!=1:
            messagebox.showerror('Hi','Enter valid Email id')
        elif xe.count('.')!=1:
            messagebox.showerror('Hi','Enter valid Email id')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update customers set cname='%s',address='%s',phone='%s',email='%s' where custid=%d"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            data=cur.fetchone()
            db.commit()
            db.close()
            messagebox.showinfo('Hi',"Data Updated")
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
           
    def close():
        t.destroy()
    a1=Label(t,text='CUSTOMER- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)    
    a=Label(t,text='CUSTOMER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=275,y=100)
    filldata()
    aa['values']=xt
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=550,y=100)
    b=Label(t,text='CUSTOMER NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=275,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=275,y=200)
    d=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Entry(t,width=30,font=('times new roman',12))
    dd.place(x=275,y=250)
    e=Label(t,text='EMAIL ID',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=275,y=300)
    
    g=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    g.place(x=300,y=400)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=400)
    
    
    t.mainloop()
    
    
