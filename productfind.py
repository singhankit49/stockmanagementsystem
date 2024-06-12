import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select productid from products"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,pcatname,productname,priceperunit,openqty,currentqty from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.config(text='')
        aa2.config(text='')
        cc.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        bb.config(text=data[0])
        aa2.config(text=data[1])
        cc.config(text=data[2])
        dd.config(text=data[3])
        ee.config(text=data[4])
        ff.config(text=data[5])
        db.close()
    def close():
        t.destroy()
    a1=Label(t,text='PRODUCT- FIND SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)
    a=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=300,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=300,y=150)
    a2=Label(t,text='PCAT NAME',font=('times new roman bold',13))
    a2.place(x=100,y=200)
    aa2=Label(t,width=26,font=('times new roman',12),anchor='w')
    aa2.place(x=300,y=200)
    c=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    c.place(x=100,y=250)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=300,y=250)
    d=Label(t,text='PRICE PER UNIT',font=('times new roman bold',13))
    d.place(x=100,y=300)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=300,y=300)
    e=Label(t,text='OPEN QTY',font=('times new roman bold',13))
    e.place(x=100,y=350)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    ee.place(x=300,y=350)
    f=Label(t,text='CURRENT QTY',font=('times new roman bold',13))
    f.place(x=100,y=400)
    ff=Label(t,width=26,font=('times new roman',12),anchor='w')
    ff.place(x=300,y=400)
    
    h=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    h.place(x=300,y=450)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=400,y=450)
    
    t.mainloop()
