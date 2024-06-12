import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def productcatupdatescreen():
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
    
    def checkdetail():
        xa=int(aa.get())
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="select catname,description from productcategory where pcatid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        bb.delete(0,100)
        cc.delete(0,100)
        bb.insert(0,data[0])
        cc.insert(0,data[1])
                
    def updatedata():
        xa=int(aa.get())
        xb=bb.get()
        xc=cc.get()
        db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
        cur=db.cursor()
        sql="update productcategory set catname='%s',description='%s' where pcatid=%d"%(xb,xc,xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Data Updated')
        bb.delete(0,100)
        cc.delete(0,100)
                        
    def close():
        t.destroy()
        
    a1=Label(t,text='PRODUCT CATEGORY- UPDATE SCREEN',font=('times new roman bold',18))
    a1.place(x=200,y=25)      
    a=Label(t,text='PRODUCT CAT ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=ttk.Combobox(t,font=('times new roman',12))
    aa.place(x=300,y=100)
    filldata()
    aa['values']=xt
    i=Button(t,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
    i.place(x=550,y=100)
    b=Label(t,text='CATEGORY NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=300,y=150)
    c=Label(t,text='DESCRIPTION',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=300,y=200)

    g=Button(t,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
    g.place(x=300,y=275)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=400,y=275)
    t.mainloop()
    
