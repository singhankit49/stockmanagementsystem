import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def stockinfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('STOCK IN')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select stockinid from stockin"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def finddata():
        
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        bb.config(text='')
        cc.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        bb.config(text=data[0])
        cc.config(text=data[1])
        dd.config(text=data[2])
        ee.config(text=data[3])
        ff.config(text=data[4])
        db.commit()
        db.close()
        
       
    def close():
        t.destroy()    
    a1=Label(t,text='STOCK IN- FIND SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)    
    a=Label(t,text='STOCK ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=250,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='SUPPLIER ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=250,y=150)
    c=Label(t,text='PCAT ID',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=250,y=200)
    d=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=250,y=250)
    e=Label(t,text='DATE IN',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    ee.place(x=250,y=300)
    f=Label(t,text='QTY',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Label(t,width=26,font=('times new roman',12),anchor='w')
    ff.place(x=250,y=350)
    g=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    g.place(x=300,y=400)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=400)
    
    t.mainloop()
    
    
