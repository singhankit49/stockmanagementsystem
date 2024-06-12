import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productsavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def checkdata():
        xa=int(aa.get())
        if xa>0:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from products where productid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')        
            db.close()
        else:
            messagebox.showerror('Hi','Product id cannot be negative')
    def savedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0:
            messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
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
                sql="insert into products values(%d,'%s','%s','%s',%d,%d,%d)"%(xa,xb,xb1,xc,xd,xe,xf) 
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('Hi','Data Saved')
                aa.delete(0,100)
                bb.delete(0,100)
                aa2.config(text='')
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
                ff.delete(0,100)
    def close():
        t.destroy()
    def filldata2():
        xa=int(bb.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname from productcategory where pcatid=%d"%xa
        cur.execute(sql)
        data=cur.fetchone()
        aa2.config(text='')
        aa2.config(text=data[0])
       
    a1=Label(t,text='PRODUCT- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)    
    a=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=300,y=100)
    btf=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
    btf.place(x=560,y=100)
    b=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman',12))
    bb.place(x=300,y=150)
    filldata()
    bb['values']=xt
    b1=Button(t,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=filldata2)
    b1.place(x=560,y=150)
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
    
    
    h=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    h.place(x=305,y=500)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=385,y=500)
    t.mainloop()
