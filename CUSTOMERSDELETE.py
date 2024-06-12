import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import datetime 
def customersdeletescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('CUSTOMERS')
    xt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select custid from customers"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def delete():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="delete from customers where custid=%d"%xa
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Data Deleted')
        aa.delete(0,100)
    def close():
        t.destroy()
    
    a1=Label(t,text='CUSTOMER- DELETE SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)
    a=Label(t,text='CUSTOMER ID',font=('times new roman bold',13))
    a.place(x=250,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=400,y=100)
    filldata()
    aa['values']=xt
    
    h=Button(t,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
    h.place(x=250,y=200)
    refresh=Button(t,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
    refresh.place(x=350,y=200)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=500,y=200)
    
    t.mainloop()
    
