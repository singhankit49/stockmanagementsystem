import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def ordersshowscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('ORDERS')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    xh=[]
    xi=[]
    xj=[]
    xk=[]
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select orderid,custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
            xe.append(res[4])
            xf.append(res[5])
            xg.append(res[6])
            xh.append(res[7])
            xi.append(res[8])
            xj.append(res[9])
            xk.append(res[10])
            
        db.close()
    def firstdata():
        global i
        i=0
        aa.config(text='')
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
        aa.config(text=xa[i])
        bb.config(text=xb[i])
        bb5.config(text=xc[i])
        bb4.config(text=xd[i])
        cc.config(text=xe[i])
        dd.config(text=xf[i])
        bb6.config(text=xg[i])
        ee.config(text=xh[i])
        ff.config(text=xi[i])
        dd1.config(text=xj[i])
        dd2.config(text=xk[i])
       
    def nextdata():
        global i
        i=i+1
        if i<=(len(xa)-1):
            aa.config(text='')
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
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            bb5.config(text=xc[i])
            bb4.config(text=xd[i])
            cc.config(text=xe[i])
            dd.config(text=xf[i])
            bb6.config(text=xg[i])
            ee.config(text=xh[i])
            ff.config(text=xi[i])
            dd1.config(text=xj[i])
            dd2.config(text=xk[i])
        else:
            messagebox.showinfo('Hi','End of records')
        
    def prevdata():
        global i
        i=i-1
        if i>=0:
            aa.config(text='')
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
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            bb5.config(text=xc[i])
            bb4.config(text=xd[i])
            cc.config(text=xe[i])
            dd.config(text=xf[i])
            bb6.config(text=xg[i])
            ee.config(text=xh[i])
            ff.config(text=xi[i])
            dd1.config(text=xj[i])
            dd2.config(text=xk[i])
        else:
            messagebox.showerror('Hi','End of previous records')
       
    def lastdata():
        global i
        i=len(xa)-1
        aa.config(text='')
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
        aa.config(text=xa[i])
        bb.config(text=xb[i])
        bb5.config(text=xc[i])
        bb4.config(text=xd[i])
        cc.config(text=xe[i])
        dd.config(text=xf[i])
        bb6.config(text=xg[i])
        ee.config(text=xh[i])
        ff.config(text=xi[i])
        dd1.config(text=xj[i])
        dd2.config(text=xk[i])
        
    def close():
        t.destroy()    
    a1=Label(t,text='ORDER- SHOW SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)      
    a=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Label(t,width=26,font=('times new roman',12),anchor='w')
    aa.place(x=250,y=100)
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
    g=Button(t,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
    g.place(x=200,y=650)
    h=Button(t,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
    h.place(x=280,y=650)
    i=Button(t,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
    i.place(x=360,y=650)
    j=Button(t,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
    j.place(x=440,y=650)
    filldata()
    i=Button(t,text="CLOSE",font=('times new roman bold',11),fg='white',bg='purple',command=close)
    i.place(x=560,y=650)
    t.mainloop()


