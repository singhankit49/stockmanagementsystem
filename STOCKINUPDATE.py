import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def stockinupdatescreen():
    t=tkinter.Tk()
    t.geometry('6800x800')
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
    xs=[]
    def fillsdata():
         db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
         cur=db.cursor()
         sql="select supplierid from supplier"
         cur.execute(sql)
         data=cur.fetchall()
         for res in data:
             xs.append(res[0])
         db.close()
    xv=[]
    def filleddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xv.append(res[0])
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
    def checkdetail():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        db.close()
    
    def updatedata():
        xa=int(aa.get())
        xb=int(bb.get())
        xc=int(cc.get())
        xd=int(dd.get())
        xe=ee.get()
        xf=int(ff.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update stockin set supplierid=%d,pcatid=%d,productid=%d,datein='%s',qty=%d where stockinid=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        db.close()
        messagebox.showinfo('Hi'," Data Updated")
        aa.delete(0,100)
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
       
    def close():
        t.destroy()
    a1=Label(t,text='STOCK IN- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)    
    a=Label(t,text='STOCK ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=250,y=100)
    filldata()
    aa['values']=xt
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=550,y=100)
    b=Label(t,text='SUPPLIER ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman bold',12))
    bb.place(x=250,y=150)
    fillsdata()
    bb['values']=xs
    c=Label(t,text='PCAT ID',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=ttk.Combobox(t,font=('times new roman bold',12))
    cc.place(x=250,y=200)
    filleddata()
    cc['values']=xv
    d=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=ttk.Combobox(t,font=('times new roman bold',12))
    dd.place(x=250,y=250)
    fildata()
    dd['values']=xw
    e=Label(t,text='DATE IN',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=250,y=300)
    f=Label(t,text='QTY',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Entry(t,width=30,font=('times new roman',12))
    ff.place(x=250,y=350)
    
    g=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    g.place(x=250,y=400)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=400)
    
    t.mainloop()
    
    
