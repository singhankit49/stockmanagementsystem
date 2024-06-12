import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def customersfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('CUSTOMER')
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
    
    def finddata():
        
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,address,phone,email from customers where custid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        bb.config(text='')
        cc.config(text='')
        dd.config(text='')
        ee.config(text='')
        bb.config(text=data[0])
        cc.config(text=data[1])
        dd.config(text=data[2])
        ee.config(text=data[3])
        db.commit()
        db.close()
        
       
    def close():
        t.destroy()    
    a1=Label(t,text='CUSTOMER- FIND SCREEN',font=('times new roman bold',20))
    a1.place(x=250,y=25)    
    a=Label(t,text='CUSTOMER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=275,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='CUSTOMER NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=275,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=275,y=200)
    d=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=275,y=250)
    e=Label(t,text='EMAIL ID',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    ee.place(x=275,y=300)
    g=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    g.place(x=300,y=400)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=400)
    
    t.mainloop()
    
    
