import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productcatfindscreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Product category')
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
    
    def finddata():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname,description from productcategory where pcatid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.config(text='')
        cc.config(text='')
        bb.config(text=data[0])
        cc.config(text=data[1])
        db.close()
    def close():
        t.destroy()
    
    a1=Label(t,text='PRODUCT CATEGORY- FIND SCREEN',font=('times new roman bold',18))
    a1.place(x=200,y=25)     
    a=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=300,y=100)
    filldata()
    aa['values']=xt
    b=Label(t,text='CATEGORY NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb.place(x=300,y=150)
    c=Label(t,text='DESCRIPTION',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Label(t,width=26,font=('times new roman',12),anchor='w')
    cc.place(x=300,y=200)
    h=Button(t,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
    h.place(x=300,y=300)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=400,y=300)
    
    t.mainloop()
