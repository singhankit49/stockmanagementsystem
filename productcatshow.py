import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productcatshowscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product category')
    xa=[]
    xb=[]
    xc=[]
    
    i=0
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select pcatid,catname,description from productcategory"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xc.append(res[2])
        db.close()
    def firstdata():
        global i
        i=0
        aa.config(text='')
        bb.config(text='')
        cc.config(text='')
        aa.config(text= xa[i])
        bb.config(text= xb[i])
        cc.config(text= xc[i])
    def nextdata():
        global i
        i=i+1
        if i<=(len(xa)-1):
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
        else:
            messagebox.showinfo('Hi','End of records')
    def prevdata():
        global i
        i=i-1
        if i>=0:
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
        else:
            messagebox.showerror('Hi','End of previous records')
    def lastdata():
        global i
        i=len(xa)-1
        aa.config(text='')
        bb.config(text='')
        cc.config(text='')
        aa.config(text= xa[i])
        bb.config(text= xb[i])
        cc.config(text= xc[i])
    def close():
        t.destroy()
    a1=Label(t,text='PRODUCT CATEGORY- SHOW SCREEN',font=('times new roman bold',18))
    a1.place(x=200,y=25)    
    a=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Label(t,width=26,font=('times new roman',12),anchor='w')
    aa.place(x=300,y=100)
    b=Label(t,text='CATEGORY NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=300,y=150)
    c=Label(t,text='DESCRIPTION',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=300,y=200)
    ggg=Button(t,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
    ggg.place(x=200,y=300)
    h=Button(t,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
    h.place(x=280,y=300)
    i=Button(t,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
    i.place(x=360,y=300)
    j=Button(t,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
    j.place(x=440,y=300)
    filldata()
    i=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    i.place(x=560,y=300)
    
    t.mainloop()