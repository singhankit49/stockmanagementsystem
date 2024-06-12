import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def dispatchbillshowscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('DISPATCH BILL')
    xa=[]
    xa1=[]
    xb=[]
    xb1=[]
    xb2=[]
    xc=[]
    xd=[]
    xd1=[]
    xe=[]
    xe1=[]
    xf=[]
    xf1=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select dispatchid,orderid,custid,custname,custemail,productid,pcatid,productname,dispatchdate,price,qty,bill from dispatchorder"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xa1.append(res[1])
            xb.append(res[2])
            xb1.append(res[3])
            xb2.append(res[4])
            xc.append(res[5])
            xd.append(res[6])
            xd1.append(res[7])
            xe.append(res[8])
            xe1.append(res[9])
            xf.append(res[10])
            xf1.append(res[11])
        db.close()
    def firstdata():
        global i
        i=0
        aa.config(text='')
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
        aa.config(text=xa[i])
        aa4.config(text=xa1[i])
        bb.config(text=xb[i])
        bb5.config(text=xb1[i])
        bb4.config(text=xb2[i])
        cc.config(text=xc[i])
        dd.config(text=xd[i])
        dd1.config(text=xd1[i])
        ee.config(text=xe[i])
        ee1.config(text=xe1[i])
        ff.config(text=xf[i])
        ff1.config(text=xf1[i])
       
    def nextdata():
        global i
        i=i+1
        if i<=(len(xa)-1):
            aa.config(text='')
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
            aa.config(text=xa[i])
            aa4.config(text=xa1[i])
            bb.config(text=xb[i])
            bb5.config(text=xb1[i])
            bb4.config(text=xb2[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            dd1.config(text=xd1[i])
            ee.config(text=xe[i])
            ee1.config(text=xe1[i])
            ff.config(text=xf[i])
            ff1.config(text=xf1[i])
        else:
            messagebox.showinfo('Hi','End of records')
        
    def prevdata():
        global i
        i=i-1
        if i>=0:
            aa.config(text='')
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
            aa.config(text=xa[i])
            aa4.config(text=xa1[i])
            bb.config(text=xb[i])
            bb5.config(text=xb1[i])
            bb4.config(text=xb2[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            dd1.config(text=xd1[i])
            ee.config(text=xe[i])
            ee1.config(text=xe1[i])
            ff.config(text=xf[i])
            ff1.config(text=xf1[i])
        else:
            messagebox.showerror('Hi','End of previous records')
       
    def lastdata():
        global i
        i=len(xa)-1
        aa.config(text='')
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
        aa.config(text=xa[i])
        aa4.config(text=xa1[i])
        bb.config(text=xb[i])
        bb5.config(text=xb1[i])
        bb4.config(text=xb2[i])
        cc.config(text=xc[i])
        dd.config(text=xd[i])
        dd1.config(text=xd1[i])
        ee.config(text=xe[i])
        ee1.config(text=xe1[i])
        ff.config(text=xf[i])
        ff1.config(text=xf1[i])
        
    def close():
        t.destroy()    
    a1=Label(t,text='DISPATCH BILL- SHOW SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)   
    a=Label(t,text='DISPATCH ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Label(t,width=30,font=('times new roman',12),anchor='w')
    aa.place(x=250,y=100)
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
    g=Button(t,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
    g.place(x=200,y=700)
    h=Button(t,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
    h.place(x=280,y=700)
    i=Button(t,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
    i.place(x=360,y=700)
    j=Button(t,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
    j.place(x=440,y=700)
    filldata()
    i=Button(t,text="CLOSE",font=('times new roman bold',11),fg='white',bg='purple',command=close)
    i.place(x=560,y=700)
    t.mainloop()
    
    
