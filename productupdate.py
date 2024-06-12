import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productupdatescreen():
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
    xp=[]
    def fillpdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xp.append(res[0])
        db.close()
    def checkdetail():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,pcatname,productname,priceperunit,openqty,currentqty from products where productid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        aa2.config(text='')
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        bb.insert(0,data[0])
        aa2.config(text=data[1])
        cc.insert(0,data[2])
        dd.insert(0,data[3])
        ee.insert(0,data[4])
        ff.insert(0,data[5])    
    def updatedata():
        xa=int(aa.get())
        xb=int(bb.get())
        xb1=aa2.cget("text")
        xc=cc.get()
        xd=int(dd.get())
        xe=int(ee.get())
        xf=int(ff.get())
        if xd<=0:
            messagebox.showerror('Hi','Price cannot be negative')
        elif xe<0:
            messagebox.showerror('Hi','Open qty cannot be negative')
        elif xf<0:
            messagebox.showerror('Hi','Current qty cannot be negative')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update products set pcatid=%d,pcatname='%s',productname='%s',priceperunit=%d,openqty=%d,currentqty=%d where productid=%d"%(xb,xb1,xc,xd,xe,xf,xa)  
            cur.execute(sql)
            data=cur.fetchone()
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Udated')
            bb.delete(0,100)
            aa2.config(text='')
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
    def close():
        t.destroy()
    def checkdata():
        xa=int(bb.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname from productcategory where pcatid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        aa2.config(text='')
        aa2.config(text=data[0])
        
    a1=Label(t,text='PRODUCT- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)   
    a=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=300,y=100)
    filldata()
    aa['values']=xt
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=550,y=100)
    b=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman',12))
    bb.place(x=300,y=150)
    fillpdata()
    bb['values']=xp
    bb1=Button(t,text='FILL DATA',font=('times new roman bold',11),fg='black',bg='orange',command=checkdata)
    bb1.place(x=550,y=150)
    a2=Label(t,text='PCAT NAME',font=('times new roman bold',13))
    a2.place(x=100,y=200)
    aa2=Label(t,width=26,font=('times new roman',12),anchor='w')
    aa2.place(x=300,y=200)
    c=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    c.place(x=100,y=250)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=300,y=250)
    d=Label(t,text='PRICE PER UNIT',font=('times new roman bold',13))
    d.place(x=100,y=300)
    dd=Entry(t,width=30,font=('times new roman',12))
    dd.place(x=300,y=300)
    e=Label(t,text='OPEN QTY',font=('times new roman bold',13))
    e.place(x=100,y=350)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=300,y=350)
    f=Label(t,text='CURRENT QTY',font=('times new roman bold',13))
    f.place(x=100,y=400)
    ff=Entry(t,width=30,font=('times new roman',12))
    ff.place(x=300,y=400)
    g=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    g.place(x=300,y=450)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=450)
    t.mainloop()
    
