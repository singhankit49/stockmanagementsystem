import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def storesavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Store SMS')
    def checkdata():
        xa=int(aa.get())
        if xa>0:
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*) from store where storeid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','OK pls go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')
            db.close()
        else:
            messagebox.showerror('Hi','Store id cannot be negative')
        
    def savedata():
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
                sql="insert into store values(%d,'%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg) 
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('Hi','Data Saved')
                aa.delete(0,100)
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
                ff.delete(0,100)
                gg.delete(0,100)
            
    def close():
        t.destroy()
           
    a1=Label(t,text='STORE- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)    
    a=Label(t,text='STORE ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=275,y=100)
    btf=Button(t,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
    btf.place(x=540,y=100)
    b=Label(t,text='NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=275,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=275,y=200)
    d=Label(t,text='CITY',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Entry(t,width=30,font=('times new roman',12))
    dd.place(x=275,y=250)
    e=Label(t,text='EMAIL',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=275,y=300)
    f=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    f.place(x=100,y=350)
    ff=Entry(t,width=30,font=('times new roman',12))
    ff.place(x=275,y=350)
    g=Label(t,text='REGISTRATION NO.',font=('times new roman bold',13))
    g.place(x=100,y=400)
    gg=Entry(t,width=30,font=('times new roman',12))
    gg.place(x=275,y=400)
    
    
    h=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    h.place(x=305,y=450)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=385,y=450)
    t.mainloop()
