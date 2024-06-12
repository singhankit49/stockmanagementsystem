import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def storeshowscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Store SMS')
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select storeid,name,address,city,email,phone,regno from store"
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
        db.close()
    def firstdata():
        global i
        i=0
        aa.config(text='')
        bb.config(text='')
        cc.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        gg.config(text='')
        aa.config(text= xa[i])
        bb.config(text= xb[i])
        cc.config(text= xc[i])
        dd.config(text= xd[i])
        ee.config(text= xe[i])
        ff.config(text= xf[i])
        gg.config(text= xg[i])
    def nextdata():
        global i
        i=i+1
        if i<=(len(xa)-1):
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            gg.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
            ff.config(text= xf[i])
            gg.config(text= xg[i])
        else:
            messagebox.showinfo('Hi','End of records')
        
    def prevdata():
        global i
        i=i-1
        if i>=0:
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            gg.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
            ff.config(text= xf[i])
            gg.config(text= xg[i])
        else:
            messagebox.showerror('Hi','End of previous records')
    def lastdata():
        global i
        i=len(xa)-1
        aa.config(text='')
        bb.config(text='')
        cc.config(text='')
        dd.config(text='')
        ee.config(text='')
        ff.config(text='')
        gg.config(text='')
        aa.config(text= xa[i])
        bb.config(text= xb[i])
        cc.config(text= xc[i])
        dd.config(text= xd[i])
        ee.config(text= xe[i])
        ff.config(text= xf[i])
        gg.config(text= xg[i])
    def close():
        t.destroy()
       
    a1=Label(t,text='STORE- SHOW SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)
    a=Label(t,text='STORE ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Label(t,width=26,font=('times new roman',12),anchor='w')
    aa.place(x=300,y=100)
    b=Label(t,text='NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=300,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=300,y=200)
    d=Label(t,text='CITY',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=300,y=250)
    e=Label(t,text='EMAIL',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    ee.place(x=300,y=300)
    f=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Label(t,width=26,font=('times new roman',12),anchor='w')
    ff.place(x=300,y=350)
    g=Label(t,text='REGISTRATION NO.',font=('times new roman bold',13))
    g.place(x=100,y=400)
    gg=Label(t,width=26,font=('times new roman',12),anchor='w')
    gg.place(x=300,y=400)
    ggg=Button(t,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
    ggg.place(x=200,y=450)
    h=Button(t,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
    h.place(x=280,y=450)
    i=Button(t,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
    i.place(x=360,y=450)
    j=Button(t,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
    j.place(x=440,y=450)
    filldata()
    i=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    i.place(x=560,y=450)
    
    t.mainloop()
