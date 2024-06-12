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
def finalsmscanvasdashboarduser():
    t=tkinter.Tk()
    t.geometry('900x800')
    t.title('STOCK MANAGEMENT SYSTEM')
       
    def storefindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
        
        def finddata():
            xa=int(storeid_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select storeid,name,address,city,email,phone,regno from store where storeid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            name_elabel.config(text='')
            address_elabel.config(text='')
            city_elabel.config(text='')
            email_elabel.config(text='')
            phoneno_elabel.config(text='')
            regno_elabel.config(text='')
            name_elabel.config(text=data[0])
            address_elabel.config(text=data[1])
            city_elabel.config(text=data[2])
            email_elabel.config(text=data[3])
            phoneno_elabel.config(text=data[4])
            regno_elabel.config(text=data[5])
            db.close()
        def close():
            c2.destroy()
        
        storefindscreen_label=Label(c2,text='STORE- FIND SCREEN',font=('times new roman bold',18))
        storefindscreen_label.place(x=250,y=25)
        storeid_label=Label(c2,text='STORE ID',font=('times new roman bold',13))
        storeid_label.place(x=100,y=100)
        storeid_entry=ttk.Combobox(c2,font=('times new roman',12))
        storeid_entry.place(x=300,y=100)
        filldata()
        storeid_entry['values']=xt
        name_label=Label(c2,text='NAME',font=('times new roman bold',13))
        name_label.place(x=100,y=150)
        name_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        name_elabel.place(x=300,y=150)
        address_label=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        address_label.place(x=100,y=200)
        address_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        address_elabel.place(x=300,y=200)
        city_label=Label(c2,text='CITY',font=('times new roman bold',13))
        city_label.place(x=100,y=250)
        city_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        city_elabel.place(x=300,y=250)
        email_label=Label(c2,text='EMAIL',font=('times new roman bold',13))
        email_label.place(x=100,y=300)
        email_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        email_elabel.place(x=300,y=300)
        phoneno_label=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        phoneno_label.place(x=100,y=350)
        phoneno_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        phoneno_elabel.place(x=300,y=350)
        regno_label=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13))
        regno_label.place(x=100,y=400)
        regno_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        regno_elabel.place(x=300,y=400)
        
        
        find_button=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        find_button.place(x=300,y=500)
        close_button=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        close_button.place(x=400,y=500)
    
    def storeshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
            storeid_elabel.config(text='')
            name_elabel.config(text='')
            address_elabel.config(text='')
            city_elabel.config(text='')
            email_elabel.config(text='')
            phoneno_elabel.config(text='')
            regno_elabel.config(text='')
            storeid_elabel.config(text= xa[i])
            name_elabel.config(text= xb[i])
            address_elabel.config(text= xc[i])
            city_elabel.config(text= xd[i])
            email_elabel.config(text= xe[i])
            phoneno_elabel.config(text= xf[i])
            regno_elabel.config(text= xg[i])
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                storeid_elabel.config(text='')
                name_elabel.config(text='')
                address_elabel.config(text='')
                city_elabel.config(text='')
                email_elabel.config(text='')
                phoneno_elabel.config(text='')
                regno_elabel.config(text='')
                storeid_elabel.config(text= xa[i])
                name_elabel.config(text= xb[i])
                address_elabel.config(text= xc[i])
                city_elabel.config(text= xd[i])
                email_elabel.config(text= xe[i])
                phoneno_elabel.config(text= xf[i])
                regno_elabel.config(text= xg[i])
            else:
                messagebox.showinfo('Hi','End of records')
            
        def prevdata():
            global i
            i=i-1
            if i>=0:
                storeid_elabel.config(text='')
                name_elabel.config(text='')
                address_elabel.config(text='')
                city_elabel.config(text='')
                email_elabel.config(text='')
                phoneno_elabel.config(text='')
                regno_elabel.config(text='')
                storeid_elabel.config(text= xa[i])
                name_elabel.config(text= xb[i])
                address_elabel.config(text= xc[i])
                city_elabel.config(text= xd[i])
                email_elabel.config(text= xe[i])
                phoneno_elabel.config(text= xf[i])
                regno_elabel.config(text= xg[i])
            else:
                messagebox.showerror('Hi','End of previous records')
        def lastdata():
            global i
            i=len(xa)-1
            storeid_elabel.config(text='')
            name_elabel.config(text='')
            address_elabel.config(text='')
            city_elabel.config(text='')
            email_elabel.config(text='')
            phoneno_elabel.config(text='')
            regno_elabel.config(text='')
            storeid_elabel.config(text= xa[i])
            name_elabel.config(text= xb[i])
            address_elabel.config(text= xc[i])
            city_elabel.config(text= xd[i])
            email_elabel.config(text= xe[i])
            phoneno_elabel.config(text= xf[i])
            regno_elabel.config(text= xg[i])
        def close():
            c2.destroy()
           
        storeshowscreen_label=Label(c2,text='STORE- SHOW SCREEN',font=('times new roman bold',18))
        storeshowscreen_label.place(x=250,y=25)
        storeid_label=Label(c2,text='STORE ID',font=('times new roman bold',13))
        storeid_label.place(x=100,y=100)
        storeid_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        storeid_elabel.place(x=300,y=100)
        name_label=Label(c2,text='NAME',font=('times new roman bold',13))
        name_label.place(x=100,y=150)
        name_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        name_elabel.place(x=300,y=150)
        address_label=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        address_label.place(x=100,y=200)
        address_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        address_elabel.place(x=300,y=200)
        city_label=Label(c2,text='CITY',font=('times new roman bold',13))
        city_label.place(x=100,y=250)
        city_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        city_elabel.place(x=300,y=250)
        email_label=Label(c2,text='EMAIL',font=('times new roman bold',13))
        email_label.place(x=100,y=300)
        email_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        email_elabel.place(x=300,y=300)
        phoneno_label=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        phoneno_label.place(x=100,y=350)
        phoneno_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        phoneno_elabel.place(x=300,y=350)
        regno_label=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13))
        regno_label.place(x=100,y=400)
        regno_elabel=Label(c2,width=26,font=('times new roman',12),anchor='w')
        regno_elabel.place(x=300,y=400)
        ggg=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        ggg.place(x=200,y=450)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=450)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=450)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=450)
        filldata()
        i=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=450)
    
        
    
    
    def productcatfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
            c2.destroy()
        
        a1=Label(c2,text='PRODUCT CATEGORY- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=200,y=25)     
        a=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CATEGORY NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=200)
        h=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        h.place(x=300,y=300)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=400,y=300)
    
    def productcatshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
            c2.destroy()
        a1=Label(c2,text='PRODUCT CATEGORY- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=200,y=25)    
        a=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=300,y=100)
        b=Label(c2,text='CATEGORY NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=200)
        ggg=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        ggg.place(x=200,y=300)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=300)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=300)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=300)
        filldata()
        i=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=300)
        
    
    
    def productfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
            c2.destroy()
        a1=Label(c2,text='PRODUCT- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        a2=Label(c2,text='PCAT NAME',font=('times new roman bold',13))
        a2.place(x=100,y=200)
        aa2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa2.place(x=300,y=200)
        c=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        c.place(x=100,y=250)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=250)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        d.place(x=100,y=300)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=300,y=300)
        e=Label(c2,text='OPEN QTY',font=('times new roman bold',13))
        e.place(x=100,y=350)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=300,y=350)
        f=Label(c2,text='CURRENT QTY',font=('times new roman bold',13))
        f.place(x=100,y=400)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=300,y=400)
        
        h=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        h.place(x=300,y=450)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=400,y=450)
    
    def productshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xa=[]
        xb=[]
        xa2=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid,pcatid,pcatname,productname,priceperunit,openqty,currentqty from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xa2.append(res[2])
                xc.append(res[3])
                xd.append(res[4])
                xe.append(res[5])
                xf.append(res[6])
            db.close()
        def firstdata():
            global i
            i=0
            aa.config(text='')
            bb.config(text='')
            aa2.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            aa2.config(text=xa2[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
            ff.config(text= xf[i])
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                aa.config(text='')
                bb.config(text='')
                aa2.config(text='')
                cc.config(text='')
                dd.config(text='')
                ee.config(text='')
                ff.config(text='')
                aa.config(text= xa[i])
                bb.config(text= xb[i])
                aa2.config(text=xa2[i])
                cc.config(text= xc[i])
                dd.config(text= xd[i])
                ee.config(text= xe[i])
                ff.config(text= xf[i])
            else:
                messagebox.showinfo('Hi','End of records')
        def prevdata():
            global i
            i=i-1
            if i>=0:
                aa.config(text='')
                bb.config(text='')
                aa2.config(text='')
                cc.config(text='')
                dd.config(text='')
                ee.config(text='')
                ff.config(text='')
                aa.config(text= xa[i])
                bb.config(text= xb[i])
                aa2.config(text=xa2[i])
                cc.config(text= xc[i])
                dd.config(text= xd[i])
                ee.config(text= xe[i])
                ff.config(text= xf[i])
            else:
                messagebox.showerror('Hi','End of previous records')
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text='')
            bb.config(text='')
            aa2.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            aa2.config(text=xa2[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
            ff.config(text= xf[i])
        def close():
            c2.destroy()
        a1=Label(c2,text='PRODUCT- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)   
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=300,y=100)
        b=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        a2=Label(c2,text='PCAT NAME',font=('times new roman bold',13))
        a2.place(x=100,y=200)
        aa2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa2.place(x=300,y=200)
        c=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        c.place(x=100,y=250)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=250)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        d.place(x=100,y=300)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=300,y=300)
        e=Label(c2,text='OPEN QTY',font=('times new roman bold',13))
        e.place(x=100,y=350)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=300,y=350)
        f=Label(c2,text='CURRENT QTY',font=('times new roman bold',13))
        f.place(x=100,y=400)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=300,y=400)
        ggg=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        ggg.place(x=200,y=450)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=450)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=450)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=450)
        filldata()
        i=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=450)
    
    
    
    def supplierfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select supplierid from supplier"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xt.append(res[0])
            db.close()
        
        def finddata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select sname,address,phone,email from supplier where supplierid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            db.close()
        def close():
            c2.destroy()
        a1=Label(c2,text='SUPPLIER- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)
        a=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='SUPPLIER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=300,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=300,y=300)
        
        h=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        h.place(x=300,y=400)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=400,y=400)
    
    def suppliershowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select supplierid,sname,address,phone,email from supplier"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
            db.close()
        def firstdata():
            global i
            i=0
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                aa.config(text='')
                bb.config(text='')
                cc.config(text='')
                dd.config(text='')
                ee.config(text='')
                aa.config(text= xa[i])
                bb.config(text= xb[i])
                cc.config(text= xc[i])
                dd.config(text= xd[i])
                ee.config(text= xe[i])
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
                aa.config(text= xa[i])
                bb.config(text= xb[i])
                cc.config(text= xc[i])
                dd.config(text= xd[i])
                ee.config(text= xe[i])
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
            aa.config(text= xa[i])
            bb.config(text= xb[i])
            cc.config(text= xc[i])
            dd.config(text= xd[i])
            ee.config(text= xe[i])
        def close():
            c2.destroy()
        a1=Label(c2,text='SUPPLIER- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)   
        a=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=300,y=100)
        b=Label(c2,text='SUPPLIER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=300,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=300,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=300,y=250)
        e=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=300,y=300)
        ggg=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        ggg.place(x=200,y=400)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=400)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=400)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=400)
        filldata()
        i=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=400)
    
    
        
    def stockinfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select stockinid from stockin"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xt.append(res[0])
            db.close()
        
        def finddata():
            
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            ff.config(text=data[4])
            db.commit()
            db.close()
            
           
        def close():
            c2.destroy()    
        a1=Label(c2,text='STOCK IN- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='STOCK ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=150)
        c=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=200)
        d=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=250)
        e=Label(c2,text='DATE IN',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=300)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=350)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=350)
        g=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        g.place(x=300,y=400)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=400)
    
    def stockinshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select stockinid,supplierid,pcatid,productid,datein,qty from stockin"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
                xf.append(res[5])
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
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
           
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
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                ee.config(text=xe[i])
                ff.config(text=xf[i])
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
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                ee.config(text=xe[i])
                ff.config(text=xf[i])
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
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            ff.config(text=xf[i])
            
        def close():
            c2.destroy()    
        a1=Label(c2,text='STOCK IN- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='STOCK ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=250,y=100)
        b=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=150)
        c=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=200)
        d=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=250)
        e=Label(c2,text='DATE IN',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=300)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=350)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=350)
        g=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        g.place(x=200,y=450)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=450)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=450)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=450)
        filldata()
        i=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=450)
    
    
    
    def customersfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
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
        
        def finddata():
            
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select cname,address,phone,email from customers where custid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            bb.config(text=data[0])
            cc.config(text=data[1])
            dd.config(text=data[2])
            ee.config(text=data[3])
            db.commit()
            db.close()
            
           
        def close():
            c2.destroy()    
        a1=Label(c2,text='CUSTOMER- FIND SCREEN',font=('times new roman bold',20))
        a1.place(x=250,y=25)    
        a=Label(c2,text='CUSTOMER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=275,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUSTOMER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=275,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL ID',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=275,y=300)
        g=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        g.place(x=300,y=400)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=400)
    
    def customersshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid,cname,address,phone,email from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xb.append(res[1])
                xc.append(res[2])
                xd.append(res[3])
                xe.append(res[4])
            db.close()
        def firstdata():
            global i
            i=0
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd.config(text='')
            ee.config(text='')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
               
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                aa.config(text='')
                bb.config(text='')
                cc.config(text='')
                dd.config(text='')
                ee.config(text='')
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                ee.config(text=xe[i])
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
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                ee.config(text=xe[i])
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
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            ee.config(text=xe[i])
            
        def close():
            c2.destroy()    
        a1=Label(c2,text='CUSTOMER- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)    
        a=Label(c2,text='CUSTOMER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=275,y=100)
        b=Label(c2,text='CUSTOMER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=275,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL ID',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=275,y=300)
        g=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        g.place(x=200,y=400)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=400)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=400)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=400)
        filldata()
        i=Button(c2,text="CLOSE",font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=400)
    
    
    
    def ordersfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        xt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select orderid from orders"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xt.append(res[0])
            db.close()
        
        def finddata():
            
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders where orderid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            cc.config(text='')
            dd1.config(text='')
            bb4.config(text='')
            bb5.config(text='')
            bb6.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            dd2.config(text='')
            bb.config(text=data[0])
            bb5.config(text=data[1])
            bb4.config(text=data[2])
            cc.config(text=data[3])
            dd.config(text=data[4])
            bb6.config(text=data[5])
            ee.config(text=data[6])
            ff.config(text=data[7])
            dd1.config(text=data[8])
            dd2.config(text=data[9])
            db.commit()
            db.close()
            
           
        def close():
            c2.destroy()    
        a1=Label(c2,text='ORDER- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)      
        a=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=150)
        b5=Label(c2,text='CUST NAME',font=('times new roman bold',13))
        b5.place(x=100,y=200)
        bb5=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb5.place(x=250,y=200)
        b4=Label(c2,text='CUST EMAIL ID',font=('times new roman bold',13))
        b4.place(x=100,y=250)
        bb4=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb4.place(x=250,y=250)
        c=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        c.place(x=100,y=300)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=300)
        d=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        d.place(x=100,y=350)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=350)
        b6=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        b6.place(x=100,y=400)
        bb6=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb6.place(x=250,y=400)
        e=Label(c2,text='DATE OF ORDER',font=('times new roman bold',13))
        e.place(x=100,y=450)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=450)
        f=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        f.place(x=100,y=500)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=500)
        d1=Label(c2,text='QTY',font=('times new roman bold',13))
        d1.place(x=100,y=550)
        dd1=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd1.place(x=250,y=550)
        d2=Label(c2,text='BILL',font=('times new roman bold',13))
        d2.place(x=100,y=600)
        dd2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd2.place(x=250,y=600)
        g=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        g.place(x=300,y=700)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=700)
        
    def ordersshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0) 
        xa=[]
        xb=[]
        xc=[]
        xd=[]
        xe=[]
        xf=[]
        xg=[]
        xh=[]
        xi=[]
        xj=[]
        xk=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select orderid,custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders"
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
                xh.append(res[7])
                xi.append(res[8])
                xj.append(res[9])
                xk.append(res[10])
                
            db.close()
        def firstdata():
            global i
            i=0
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd1.config(text='')
            bb4.config(text='')
            bb5.config(text='')
            bb6.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            dd2.config(text='')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            bb5.config(text=xc[i])
            bb4.config(text=xd[i])
            cc.config(text=xe[i])
            dd.config(text=xf[i])
            bb6.config(text=xg[i])
            ee.config(text=xh[i])
            ff.config(text=xi[i])
            dd1.config(text=xj[i])
            dd2.config(text=xk[i])
           
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                aa.config(text='')
                bb.config(text='')
                cc.config(text='')
                dd1.config(text='')
                bb4.config(text='')
                bb5.config(text='')
                bb6.config(text='')
                dd.config(text='')
                ee.config(text='')
                ff.config(text='')
                dd2.config(text='')
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                bb5.config(text=xc[i])
                bb4.config(text=xd[i])
                cc.config(text=xe[i])
                dd.config(text=xf[i])
                bb6.config(text=xg[i])
                ee.config(text=xh[i])
                ff.config(text=xi[i])
                dd1.config(text=xj[i])
                dd2.config(text=xk[i])
            else:
                messagebox.showinfo('Hi','End of records')
            
        def prevdata():
            global i
            i=i-1
            if i>=0:
                aa.config(text='')
                bb.config(text='')
                cc.config(text='')
                dd1.config(text='')
                bb4.config(text='')
                bb5.config(text='')
                bb6.config(text='')
                dd.config(text='')
                ee.config(text='')
                ff.config(text='')
                dd2.config(text='')
                aa.config(text=xa[i])
                bb.config(text=xb[i])
                bb5.config(text=xc[i])
                bb4.config(text=xd[i])
                cc.config(text=xe[i])
                dd.config(text=xf[i])
                bb6.config(text=xg[i])
                ee.config(text=xh[i])
                ff.config(text=xi[i])
                dd1.config(text=xj[i])
                dd2.config(text=xk[i])
            else:
                messagebox.showerror('Hi','End of previous records')
           
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text='')
            bb.config(text='')
            cc.config(text='')
            dd1.config(text='')
            bb4.config(text='')
            bb5.config(text='')
            bb6.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            dd2.config(text='')
            aa.config(text=xa[i])
            bb.config(text=xb[i])
            bb5.config(text=xc[i])
            bb4.config(text=xd[i])
            cc.config(text=xe[i])
            dd.config(text=xf[i])
            bb6.config(text=xg[i])
            ee.config(text=xh[i])
            ff.config(text=xi[i])
            dd1.config(text=xj[i])
            dd2.config(text=xk[i])
            
        def close():
            c2.destroy()    
        a1=Label(c2,text='ORDER- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)      
        a=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa.place(x=250,y=100)
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=150)
        b5=Label(c2,text='CUST NAME',font=('times new roman bold',13))
        b5.place(x=100,y=200)
        bb5=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb5.place(x=250,y=200)
        b4=Label(c2,text='CUST EMAIL ID',font=('times new roman bold',13))
        b4.place(x=100,y=250)
        bb4=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb4.place(x=250,y=250)
        c=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        c.place(x=100,y=300)
        cc=Label(c2,width=26,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=300)
        d=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        d.place(x=100,y=350)
        dd=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=350)
        b6=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        b6.place(x=100,y=400)
        bb6=Label(c2,width=26,font=('times new roman',12),anchor='w')
        bb6.place(x=250,y=400)
        e=Label(c2,text='DATE OF ORDER',font=('times new roman bold',13))
        e.place(x=100,y=450)
        ee=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=450)
        f=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        f.place(x=100,y=500)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=500)
        d1=Label(c2,text='QTY',font=('times new roman bold',13))
        d1.place(x=100,y=550)
        dd1=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd1.place(x=250,y=550)
        d2=Label(c2,text='BILL',font=('times new roman bold',13))
        d2.place(x=100,y=600)
        dd2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd2.place(x=250,y=600)
        g=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        g.place(x=200,y=650)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=650)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=650)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=650)
        filldata()
        i=Button(c2,text="CLOSE",font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=650)
    
    
    
    def dispatchbillfindscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0) 
        xt=[]
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select dispatchid from dispatchorder"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xt.append(res[0])
            db.close()
        
        def finddata():
            
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select orderid,custid,custname,custemail,productid,pcatid,productname,dispatchdate,price,qty,bill from dispatchorder where dispatchid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            aa4.config(text='')
            bb.config(text='')
            bb5.config(text='')
            bb4.config(text='')
            cc.config(text='')
            dd.config(text='')
            dd1.config(text='')
            ee.config(text='')
            ee1.config(text='')
            ff.config(text='')
            ff1.config(text='')
            aa4.config(text=data[0])
            bb.config(text=data[1])
            bb5.config(text=data[2])
            bb4.config(text=data[3])
            cc.config(text=data[4])
            dd.config(text=data[5])
            dd1.config(text=data[6])
            ee.config(text=data[7])
            ee1.config(text=data[8])
            ff.config(text=data[9])
            ff1.config(text=data[10])
            db.commit()
            db.close()
            
           
        def close():
            c2.destroy()  
        
        a1=Label(c2,text='DISPATCH BILL- FIND SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)  
        a=Label(c2,text='DISPATCH ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        a4=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a4.place(x=100,y=150)
        aa4=Label(c2,width=30,font=('times new roman',12),anchor='w')
        aa4.place(x=250,y=150)
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=200)
        bb=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=200)
        b5=Label(c2,text='CUST NAME',font=('times new roman bold',13))
        b5.place(x=100,y=250)
        bb5=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb5.place(x=250,y=250)
        b4=Label(c2,text='CUST EMAIL ID',font=('times new roman bold',13))
        b4.place(x=100,y=300)
        bb4=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb4.place(x=250,y=300)
        c=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        c.place(x=100,y=350)
        cc=Label(c2,width=30,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=350)
        d=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        d.place(x=100,y=400)
        dd=Label(c2,width=30,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=400)
        d1=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        d1.place(x=100,y=450)
        dd1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        dd1.place(x=250,y=450)
        e=Label(c2,text='DISPATCH DATE',font=('times new roman bold',13))
        e.place(x=100,y=500)
        ee=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=500)
        e1=Label(c2,text='PRICE',font=('times new roman bold',13))
        e1.place(x=100,y=550)
        ee1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ee1.place(x=250,y=550)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=600)
        ff=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=600)
        f1=Label(c2,text='BILL',font=('times new roman bold',13))
        f1.place(x=100,y=650)
        ff1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ff1.place(x=250,y=650)
        g=Button(c2,text='FIND',font=('times new roman bold',11),bg='yellow',command=finddata)
        g.place(x=300,y=700)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=700)
    
    def dispatchbillshowscreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0) 
        xa=[]
        xa1=[]
        xb=[]
        xb1=[]
        xb2=[]
        xc=[]
        xd=[]
        xd1=[]
        xe=[]
        xe1=[]
        xf=[]
        xf1=[]
        i=0
        def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select dispatchid,orderid,custid,custname,custemail,productid,pcatid,productname,dispatchdate,price,qty,bill from dispatchorder"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xa.append(res[0])
                xa1.append(res[1])
                xb.append(res[2])
                xb1.append(res[3])
                xb2.append(res[4])
                xc.append(res[5])
                xd.append(res[6])
                xd1.append(res[7])
                xe.append(res[8])
                xe1.append(res[9])
                xf.append(res[10])
                xf1.append(res[11])
            db.close()
        def firstdata():
            global i
            i=0
            aa.config(text='')
            aa4.config(text='')
            bb.config(text='')
            bb5.config(text='')
            bb4.config(text='')
            cc.config(text='')
            dd.config(text='')
            dd1.config(text='')
            ee.config(text='')
            ee1.config(text='')
            ff.config(text='')
            ff1.config(text='')
            aa.config(text=xa[i])
            aa4.config(text=xa1[i])
            bb.config(text=xb[i])
            bb5.config(text=xb1[i])
            bb4.config(text=xb2[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            dd1.config(text=xd1[i])
            ee.config(text=xe[i])
            ee1.config(text=xe1[i])
            ff.config(text=xf[i])
            ff1.config(text=xf1[i])
           
        def nextdata():
            global i
            i=i+1
            if i<=(len(xa)-1):
                aa.config(text='')
                aa4.config(text='')
                bb.config(text='')
                bb5.config(text='')
                bb4.config(text='')
                cc.config(text='')
                dd.config(text='')
                dd1.config(text='')
                ee.config(text='')
                ee1.config(text='')
                ff.config(text='')
                ff1.config(text='')
                aa.config(text=xa[i])
                aa4.config(text=xa1[i])
                bb.config(text=xb[i])
                bb5.config(text=xb1[i])
                bb4.config(text=xb2[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                dd1.config(text=xd1[i])
                ee.config(text=xe[i])
                ee1.config(text=xe1[i])
                ff.config(text=xf[i])
                ff1.config(text=xf1[i])
            else:
                messagebox.showinfo('Hi','End of records')
            
        def prevdata():
            global i
            i=i-1
            if i>=0:
                aa.config(text='')
                aa4.config(text='')
                bb.config(text='')
                bb5.config(text='')
                bb4.config(text='')
                cc.config(text='')
                dd.config(text='')
                dd1.config(text='')
                ee.config(text='')
                ee1.config(text='')
                ff.config(text='')
                ff1.config(text='')
                aa.config(text=xa[i])
                aa4.config(text=xa1[i])
                bb.config(text=xb[i])
                bb5.config(text=xb1[i])
                bb4.config(text=xb2[i])
                cc.config(text=xc[i])
                dd.config(text=xd[i])
                dd1.config(text=xd1[i])
                ee.config(text=xe[i])
                ee1.config(text=xe1[i])
                ff.config(text=xf[i])
                ff1.config(text=xf1[i])
            else:
                messagebox.showerror('Hi','End of previous records')
           
        def lastdata():
            global i
            i=len(xa)-1
            aa.config(text='')
            aa4.config(text='')
            bb.config(text='')
            bb5.config(text='')
            bb4.config(text='')
            cc.config(text='')
            dd.config(text='')
            dd1.config(text='')
            ee.config(text='')
            ee1.config(text='')
            ff.config(text='')
            ff1.config(text='')
            aa.config(text=xa[i])
            aa4.config(text=xa1[i])
            bb.config(text=xb[i])
            bb5.config(text=xb1[i])
            bb4.config(text=xb2[i])
            cc.config(text=xc[i])
            dd.config(text=xd[i])
            dd1.config(text=xd1[i])
            ee.config(text=xe[i])
            ee1.config(text=xe1[i])
            ff.config(text=xf[i])
            ff1.config(text=xf1[i])
            
        def close():
            c2.destroy()    
        a1=Label(c2,text='DISPATCH BILL- SHOW SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)   
        a=Label(c2,text='DISPATCH ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Label(c2,width=30,font=('times new roman',12),anchor='w')
        aa.place(x=250,y=100)
        a4=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a4.place(x=100,y=150)
        aa4=Label(c2,width=30,font=('times new roman',12),anchor='w')
        aa4.place(x=250,y=150)
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=200)
        bb=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb.place(x=250,y=200)
        b5=Label(c2,text='CUST NAME',font=('times new roman bold',13))
        b5.place(x=100,y=250)
        bb5=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb5.place(x=250,y=250)
        b4=Label(c2,text='CUST EMAIL ID',font=('times new roman bold',13))
        b4.place(x=100,y=300)
        bb4=Label(c2,width=30,font=('times new roman',12),anchor='w')
        bb4.place(x=250,y=300)
        c=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        c.place(x=100,y=350)
        cc=Label(c2,width=30,font=('times new roman',12),anchor='w')
        cc.place(x=250,y=350)
        d=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        d.place(x=100,y=400)
        dd=Label(c2,width=30,font=('times new roman',12),anchor='w')
        dd.place(x=250,y=400)
        d1=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        d1.place(x=100,y=450)
        dd1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        dd1.place(x=250,y=450)
        e=Label(c2,text='DISPATCH DATE',font=('times new roman bold',13))
        e.place(x=100,y=500)
        ee=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ee.place(x=250,y=500)
        e1=Label(c2,text='PRICE',font=('times new roman bold',13))
        e1.place(x=100,y=550)
        ee1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ee1.place(x=250,y=550)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=600)
        ff=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=600)
        f1=Label(c2,text='BILL',font=('times new roman bold',13))
        f1.place(x=100,y=650)
        ff1=Label(c2,width=30,font=('times new roman',12),anchor='w')
        ff1.place(x=250,y=650)
        g=Button(c2,text='FIRST',font=('times new roman bold',11),bg='dark blue',fg='white',command=firstdata)
        g.place(x=200,y=700)
        h=Button(c2,text='NEXT',font=('times new roman bold',11),bg='dark blue',fg='white',command=nextdata)
        h.place(x=280,y=700)
        i=Button(c2,text='LAST',font=('times new roman bold',11),bg='dark blue',fg='white',command=lastdata)
        i.place(x=360,y=700)
        j=Button(c2,text='PREVIOUS',font=('times new roman bold',11),bg='dark blue',fg='white',command=prevdata)
        j.place(x=440,y=700)
        filldata()
        i=Button(c2,text="CLOSE",font=('times new roman bold',11),fg='white',bg='purple',command=close)
        i.place(x=560,y=700)
        
    def storebuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - STORE',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=100,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=storefindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=storeshowscreen)
        b1.place(x=300,y=300)
    
    def productcatbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - PRODUCTS CATEGORY',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=15,y=25) 
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=productcatfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=productcatshowscreen)
        b1.place(x=300,y=300)
    
    def productbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - PRODUCTS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=70,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=productfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=productshowscreen)
        b1.place(x=300,y=300)
    
    def supplierbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - SUPPLIERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=90,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=supplierfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=suppliershowscreen)
        b1.place(x=300,y=300)
    
    def stockinbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - STOCKIN',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=100,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=stockinfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=stockinshowscreen)
        b1.place(x=300,y=300)
    
    def customersbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - CUSTOMERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=70,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=customersfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=customersshowscreen)
        b1.place(x=300,y=300)
    
    def ordersbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - ORDERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=100,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=ordersfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=ordersshowscreen)
        b1.place(x=300,y=300)
    
    def dispatchbillbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - CUSTOMERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=70,y=25)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=dispatchbillfindscreen)
        b1.place(x=300,y=150)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=dispatchbillshowscreen)
        b1.place(x=300,y=300)
    
    def close():
        t.destroy()
    c1=Canvas(t,height=900,width=200,bg='teal')
    c1.place(x=0,y=0)
    c2=Canvas(t,height=900,width=725,bg='light blue')
    c2.place(x=200,y=0)
    a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - USER',font=('times new roman bold',20),fg='white',bg='midnight blue')
    a1.place(x=100,y=25)
    b1=Button(c1,text='STORE',fg='black',bg='white',font=('times new roman bold',15),command=storebuttons)
    b1.place(x=20,y=90)
    b2=Button(c1,text='PRODUCTS CAT',fg='black',bg='white',font=('times new roman bold',15),command=productcatbuttons)
    b2.place(x=20,y=170)
    b3=Button(c1,text='PRODUCTS',fg='black',bg='white',font=('times new roman bold',15),command=productbuttons)
    b3.place(x=20,y=250)
    b4=Button(c1,text='SUPPLIERS',fg='black',bg='white',font=('times new roman bold',15),command=supplierbuttons)
    b4.place(x=20,y=330)
    b5=Button(c1,text='STOCKIN',fg='black',bg='white',font=('times new roman bold',15),command=stockinbuttons)
    b5.place(x=20,y=410)
    b6=Button(c1,text='CUSTOMERS',fg='black',bg='white',font=('times new roman bold',15),command=customersbuttons)
    b6.place(x=20,y=490)
    b7=Button(c1,text='ORDERS',fg='black',bg='white',font=('times new roman bold',15),command=ordersbuttons)
    b7.place(x=20,y=570)
    b8=Button(c1,text='DISPATCH BILL',fg='black',bg='white',font=('times new roman bold',15),command=dispatchbillbuttons)
    b8.place(x=20,y=650)
    b8=Button(c1,text='CLOSE',fg='white',bg='purple',font=('times new roman bold',15),command=close)
    b8.place(x=20,y=725)
    t.mainloop()