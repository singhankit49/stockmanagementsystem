import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def ordersfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('ORDERS')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def finddata():
        
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders where orderid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.config(text='')
        cc.config(text='')
        dd1.config(text='')
        bb4.config(text='')
        bb5.config(text='')
        bb6.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        dd2.config(text='')
        bb.config(text=data[0])
        bb5.config(text=data[1])
        bb4.config(text=data[2])
        cc.config(text=data[3])
        dd.config(text=data[4])
        bb6.config(text=data[5])
        ee.config(text=data[6])
        ff.config(text=data[7])
        dd1.config(text=data[8])
        dd2.config(text=data[9])
        db.commit()
        db.close()
        
       
    def close():
        t.destroy()    
    a1=Label(t,text='ORDER- FIND SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)      
    a=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=250,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='CUST ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=250,y=150)
    b5=Label(t,text='CUST NAME',font=('times new roman bold',13))
    b5.place(x=100,y=200)
    bb5=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb5.place(x=250,y=200)
    b4=Label(t,text='CUST EMAIL ID',font=('times new roman bold',13))
    b4.place(x=100,y=250)
    bb4=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb4.place(x=250,y=250)
    c=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    c.place(x=100,y=300)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=250,y=300)
    d=Label(t,text='PCAT ID',font=('times new roman bold',13))
    d.place(x=100,y=350)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=250,y=350)
    b6=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    b6.place(x=100,y=400)
    bb6=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb6.place(x=250,y=400)
    e=Label(t,text='DATE OF ORDER',font=('times new roman bold',13))
    e.place(x=100,y=450)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    ee.place(x=250,y=450)
    f=Label(t,text='PRICE PER UNIT',font=('times new roman bold',13))
    f.place(x=100,y=500)
    ff=Label(t,width=26,font=('times new roman',12),anchor='w')
    ff.place(x=250,y=500)
    d1=Label(t,text='QTY',font=('times new roman bold',13))
    d1.place(x=100,y=550)
    dd1=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd1.place(x=250,y=550)
    d2=Label(t,text='BILL',font=('times new roman bold',13))
    d2.place(x=100,y=600)
    dd2=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd2.place(x=250,y=600)
    g=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    g.place(x=300,y=700)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=700)
    
    t.mainloop()
    
    
