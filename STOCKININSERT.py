import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def stockinsavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('STOCK IN')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select supplierid from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
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
    
    def checkdata():
        xa=int(aa.get())
        if xa>0:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*)from stockin where stockinid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','Please go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')
            db.close()
        else:
            messagebox.showerror('Hi','Stockin id cannot be negative')
    
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ff.get())==0:
            messagebox.showerror('Hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=int(bb.get())
            xc=int(cc.get())
            xd=int(dd.get())
            xe=ee.cget("text")
            xf=int(ff.get())
            if xf<0:
                messagebox.showerror('Hi','Stockin id cannot be negative')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="insert into stockin values (%d,%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe,xf)
                cur.execute(sql)
                db.commit()
                db.close()
                updatestockdata()
                aa.delete(0,100)
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ff.delete(0,100) 
                dd.delete(0,100) 
                messagebox.showinfo(' ','Data Added')
        
    def close():
        t.destroy()
    def date():
        xa=datetime.datetime.now().date()
        ee.config(text=str(xa))    
    def updatestockdata():
        xd=int(dd.get())
        xf=int(ff.get()) #qty
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update products set currentqty=currentqty+%d where productid=%d"%(xf,xd)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi ','Stock updated...')
    a1=Label(t,text='STOCK IN- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)    
    a=Label(t,text='STOCK ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=250,y=100)
    aaa=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
    aaa.place(x=500,y=100)
    b=Label(t,text='SUPPLIER ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman bold',12))
    bb.place(x=250,y=150)
    filldata()
    bb['values']=xt
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
    ee=Label(t,width=30,font=('times new roman',12),anchor='w')
    date()
    ee.place(x=250,y=300)
    f=Label(t,text='QTY',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Entry(t,width=30,font=('times new roman',12))
    ff.place(x=250,y=350)
    h=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    h.place(x=305,y=450)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=385,y=450)
    
    t.mainloop()
    
    
