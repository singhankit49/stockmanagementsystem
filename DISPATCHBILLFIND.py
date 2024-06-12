import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def dispatchbillfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('DISPATCH BILL')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid from dispatchorder"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def finddata():
        
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid,custid,custname,custemail,productid,pcatid,productname,dispatchdate,price,qty,bill from dispatchorder where dispatchid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        aa4.config(text='')
        bb.config(text='')
        bb5.config(text='')
        bb4.config(text='')
        cc.config(text='')
        dd.config(text='')
        dd1.config(text='')
        ee.config(text='')
        ee1.config(text='')
        ff.config(text='')
        ff1.config(text='')
        aa4.config(text=data[0])
        bb.config(text=data[1])
        bb5.config(text=data[2])
        bb4.config(text=data[3])
        cc.config(text=data[4])
        dd.config(text=data[5])
        dd1.config(text=data[6])
        ee.config(text=data[7])
        ee1.config(text=data[8])
        ff.config(text=data[9])
        ff1.config(text=data[10])
        db.commit()
        db.close()
        
       
    def close():
        t.destroy()  
    
    a1=Label(t,text='DISPATCH BILL- FIND SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)  
    a=Label(t,text='DISPATCH ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=250,y=100)
    filldata()
    aa['values']=xt
    a4=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a4.place(x=100,y=150)
    aa4=Label(t,width=30,font=('times new roman',12),anchor='w')
    aa4.place(x=250,y=150)
    b=Label(t,text='CUST ID',font=('times new roman bold',13))
    b.place(x=100,y=200)
    bb=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb.place(x=250,y=200)
    b5=Label(t,text='CUST NAME',font=('times new roman bold',13))
    b5.place(x=100,y=250)
    bb5=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb5.place(x=250,y=250)
    b4=Label(t,text='CUST EMAIL ID',font=('times new roman bold',13))
    b4.place(x=100,y=300)
    bb4=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb4.place(x=250,y=300)
    c=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    c.place(x=100,y=350)
    cc=Label(t,width=30,font=('times new roman',12),anchor='w')
    cc.place(x=250,y=350)
    d=Label(t,text='PCAT ID',font=('times new roman bold',13))
    d.place(x=100,y=400)
    dd=Label(t,width=30,font=('times new roman',12),anchor='w')
    dd.place(x=250,y=400)
    d1=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    d1.place(x=100,y=450)
    dd1=Label(t,width=30,font=('times new roman',12),anchor='w')
    dd1.place(x=250,y=450)
    e=Label(t,text='DISPATCH DATE',font=('times new roman bold',13))
    e.place(x=100,y=500)
    ee=Label(t,width=30,font=('times new roman',12),anchor='w')
    ee.place(x=250,y=500)
    e1=Label(t,text='PRICE',font=('times new roman bold',13))
    e1.place(x=100,y=550)
    ee1=Label(t,width=30,font=('times new roman',12),anchor='w')
    ee1.place(x=250,y=550)
    f=Label(t,text='QTY',font=('times new roman bold',13))
    f.place(x=100,y=600)
    ff=Label(t,width=30,font=('times new roman',12),anchor='w')
    ff.place(x=250,y=600)
    f1=Label(t,text='BILL',font=('times new roman bold',13))
    f1.place(x=100,y=650)
    ff1=Label(t,width=30,font=('times new roman',12),anchor='w')
    ff1.place(x=250,y=650)
    g=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    g.place(x=300,y=700)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=700)
    
    t.mainloop()    
    
