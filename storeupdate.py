import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def storeupdatescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Store SMS')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid from store"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def checkdetail():
        xa=int(aa.get())
    
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select name,address,city,email,phone,regno from store where storeid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        
        bb.delete(0,100)
        cc.delete(0,100)
        dd.delete(0,100)
        ee.delete(0,100)
        ff.delete(0,100)
        gg.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
        dd.insert(0,data[2])
        ee.insert(0,data[3])
        ff.insert(0,data[4])
        gg.insert(0,data[5])
        
        
    def updatedata():
        if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0 or len(ff.get())==0 or len(gg.get())==0:
            messagebox.showerror('hi','Please fill all data')
        else:
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()
            xf=ff.get()
            xg=gg.get()
            if xe.count('@')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            elif xe.count('.')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            elif len(xf)!=10:
                messagebox.showerror('Hi','Enter valid Phone no.')
            elif not xf.isdigit():
                messagebox.showerror('Hi','Enter valid Phone no.')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="update store set name='%s',address='%s',city='%s',email='%s',phone='%s',regno='%s' where storeid=%d"%(xb,xc,xd,xe,xf,xg,xa)
                cur.execute(sql)
                data=cur.fetchone()
                db.commit()
                db.close()
                messagebox.showinfo('Hi',' Data Updated')
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
                ee.delete(0,100)
                ff.delete(0,100)
                gg.delete(0,100)
                aa.delete(0,100)
           
    def close():
        t.destroy()
         
    a1=Label(t,text='STORE- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)
    a=Label(t,text='STORE ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=300,y=100)
    filldata()
    aa['values']=xt
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=550,y=100)
    b=Label(t,text='NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=300,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=300,y=200)
    d=Label(t,text='CITY',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Entry(t,width=30,font=('times new roman',12))
    dd.place(x=300,y=250)
    e=Label(t,text='EMAIL',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=300,y=300)
    f=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Entry(t,width=30,font=('times new roman',12))
    ff.place(x=300,y=350)
    g=Label(t,text='REGISTRATION NO.',font=('times new roman bold',13))
    g.place(x=100,y=400)
    gg=Entry(t,width=30,font=('times new roman',12))
    gg.place(x=300,y=400)
    
    h=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    h.place(x=300,y=450)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=400,y=450)
    t.mainloop()
    
