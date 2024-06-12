import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def ordersupdatescreen():
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
    def checkdetail():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders where orderid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd1.delete(0,100)
        bb4.config(text='')
        bb5.config(text='')
        bb6.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        dd2.config(text='')
        bb.insert(0,data[0])
        bb5.config(text=data[1])
        bb4.config(text=data[2])
        cc.insert(0,data[3])
        dd.config(text=data[4])
        bb6.config(text=data[5])
        ee.config(text=data[6])
        ff.config(text=data[7])
        dd1.insert(0,data[8])
        dd2.config(text=data[9])
        
        db.close()
    
    def updatedata():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=bb5.cget("text")
        xd=bb4.cget("text")
        xe=int(cc.get())
        xf=int(dd.cget("text"))
        xg=bb6.cget("text")
        xh=ee.cget("text")
        xi=int(ff.cget("text"))
        xj=int(dd1.get())
        xk=int(dd2.cget("text"))
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update orders set custid=%d,cname='%s',cemail='%s',productid=%d,pcatid=%d,pname='%s',dateoforder='%s',priceperunit=%d,qty=%d,bill=%d where orderid=%d"%(xb,xc,xd,xe,xf,xg,xh,xi,xj,xk,xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        db.close()
        messagebox.showinfo('Hi',"Data Updated")
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd1.delete(0,100)
        bb4.config(text='')
        bb5.config(text='')
        bb6.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        dd2.config(text='')
        
       
    def close():
        t.destroy()

    xc=[]
    def fillcdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xc.append(res[0])
        db.close()
    xw=[]
    def fildata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select productid from products"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xw.append(res[0])
        db.close()    

    def checkdata2():
        xa=int(bb.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select cname,email from customers where custid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb5.config(text=data[0])
        bb4.config(text=data[1])
        db.close()
        
    def calc():
        xa=int(ff.cget("text"))
        xb=int(dd1.get())
        xc=xa*xb
        dd2.config(text=str(xc))
    def productfill():
        xa=int(cc.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,productname,priceperunit from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        dd.config(text=data[0])
        bb6.config(text=data[1])
        ff.config(text=data[2])
        db.close()    
        
    a1=Label(t,text='ORDER- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)      
    a=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=250,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='CUST ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman',12))
    bb.place(x=250,y=150)
    fillcdata()
    bb['values']=xc
    a1=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
    a1.place(x=550,y=150)
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
    cc=ttk.Combobox(t,font=('times new roman',12))
    cc.place(x=250,y=300)
    fildata()
    cc['values']=xw
    a1=Button(t,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=productfill)
    a1.place(x=550,y=300)
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
    ff.config(text='0')
    d1=Label(t,text='QTY',font=('times new roman bold',13))
    d1.place(x=100,y=550)
    dd1=Spinbox(t,from_=0,to=100,font=('times new roman',12),command=calc)
    dd1.insert(0,'0')
    dd1.place(x=250,y=550)
    d2=Label(t,text='BILL',font=('times new roman bold',13))
    d2.place(x=100,y=600)
    dd2=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd2.config(text='0')
    dd2.place(x=250,y=600)
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=225,y=700)
    g=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    g.place(x=400,y=700)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=500,y=700)
    
    t.mainloop()
    
    
