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
def finalsmscanvasdashboardadmin():
    t=tkinter.Tk()
    t.geometry('900x800')
    t.title('STOCK MANAGEMENT SYSTEM')
    def close():
        t.destroy()
    def storesavescreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        
        def checkdata():
            xa=int(storeid_entry.get())
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
            if len(storeid_entry.get())==0 or len(name_entry.get())==0 or len(address_entry.get())==0 or len(city_entry.get())==0 or len(email_entry.get())==0 or len(phoneno_entry.get())==0 or len(regno_entry.get())==0:
                messagebox.showerror('hi','Please fill all data') 
            else:
                xa=int(storeid_entry.get())
                xb=name_entry.get()
                xc=address_entry.get()
                xd=city_entry.get()
                xe=email_entry.get()
                xf=phoneno_entry.get()
                xg=regno_entry.get()
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
                    storeid_entry.delete(0,100)
                    name_entry.delete(0,100)
                    address_entry.delete(0,100)
                    city_entry.delete(0,100)
                    email_entry.delete(0,100)
                    phoneno_entry.delete(0,100)
                    regno_entry.delete(0,100)
                
        def close():
            c2.destroy()
               
        storesavescreen_label=Label(c2,text='STORE- SAVE SCREEN',font=('times new roman bold',18))
        storesavescreen_label.place(x=250,y=25)    
        storeid_label=Label(c2,text='STORE ID',font=('times new roman bold',13))
        storeid_label.place(x=100,y=100)
        storeid_entry=Entry(c2,width=30,font=('times new roman',12))
        storeid_entry.place(x=275,y=100)
        checkstoreid_button=Button(c2,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
        checkstoreid_button.place(x=540,y=100)
        name_label=Label(c2,text='NAME',font=('times new roman bold',13))
        name_label.place(x=100,y=150)
        name_entry=Entry(c2,width=30,font=('times new roman',12))
        name_entry.place(x=275,y=150)
        address_label=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        address_label.place(x=100,y=200)
        address_entry=Entry(c2,width=30,font=('times new roman',12))
        address_entry.place(x=275,y=200)
        city_label=Label(c2,text='CITY',font=('times new roman bold',13))
        city_label.place(x=100,y=250)
        city_entry=Entry(c2,width=30,font=('times new roman',12))
        city_entry.place(x=275,y=250)
        email_label=Label(c2,text='EMAIL',font=('times new roman bold',13))
        email_label.place(x=100,y=300)
        email_entry=Entry(c2,width=30,font=('times new roman',12))
        email_entry.place(x=275,y=300)
        phoneno_label=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        phoneno_label.place(x=100,y=350)
        phoneno_entry=Entry(c2,width=30,font=('times new roman',12))
        phoneno_entry.place(x=275,y=350)
        regno_label=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13))
        regno_label.place(x=100,y=400)
        regno_entry=Entry(c2,width=30,font=('times new roman',12))
        regno_entry.place(x=275,y=400)
        
        
        save_button=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        save_button.place(x=305,y=450)
        close_button=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        close_button.place(x=385,y=450)
    def storeupdatescreen():
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
        
        def checkdetail():
            xa=int(storeid_entry.get())
        
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select name,address,city,email,phone,regno from store where storeid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            
            name_entry.delete(0,100)
            address_entry.delete(0,100)
            city_entry.delete(0,100)
            email_entry.delete(0,100)
            phoneno_entry.delete(0,100)
            regno_entry.delete(0,100)
            name_entry.insert(0,data[0])
            address_entry.insert(0,data[1])
            city_entry.insert(0,data[2])
            email_entry.insert(0,data[3])
            phoneno_entry.insert(0,data[4])
            regno_entry.insert(0,data[5])
            
            
        def updatedata():
            if len(storeid_entry.get())==0 or len(name_entry.get())==0 or len(address_entry.get())==0 or len(city_entry.get())==0 or len(email_entry.get())==0 or len(phoneno_entry.get())==0 or len(regno_entry.get())==0:
                messagebox.showerror('hi','Please fill all data')
            else:
                xa=int(storeid_entry.get())
                xb=name_entry.get()
                xc=address_entry.get()
                xd=city_entry.get()
                xe=email_entry.get()
                xf=phoneno_entry.get()
                xg=regno_entry.get()
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
                    name_entry.delete(0,100)
                    address_entry.delete(0,100)
                    city_entry.delete(0,100)
                    email_entry.delete(0,100)
                    ee.delete(0,100)
                    phoneno_entry.delete(0,100)
                    regno_entry.delete(0,100)
                    storeid_entry.delete(0,100)
               
        def close():
            c2.destroy()
             
        storeupdatescreen_label=Label(c2,text='STORE- UPDATE SCREEN',font=('times new roman bold',18))
        storeupdatescreen_label.place(x=250,y=25)
        storeid_label=Label(c2,text='STORE ID',font=('times new roman bold',13))
        storeid_label.place(x=100,y=100)
        storeid_entry=ttk.Combobox(c2,font=('times new roman',12))
        storeid_entry.place(x=300,y=100)
        filldata()
        storeid_entry['values']=xt
        checkdetails_button=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        checkdetails_button.place(x=550,y=100)
        name_label=Label(c2,text='NAME',font=('times new roman bold',13))
        name_label.place(x=100,y=150)
        name_entry=Entry(c2,width=30,font=('times new roman',12))
        name_entry.place(x=300,y=150)
        address_label=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        address_label.place(x=100,y=200)
        address_entry=Entry(c2,width=30,font=('times new roman',12))
        address_entry.place(x=300,y=200)
        city_label=Label(c2,text='CITY',font=('times new roman bold',13))
        city_label.place(x=100,y=250)
        city_entry=Entry(c2,width=30,font=('times new roman',12))
        city_entry.place(x=300,y=250)
        email_label=Label(c2,text='EMAIL',font=('times new roman bold',13))
        email_label.place(x=100,y=300)
        email_entry=Entry(c2,width=30,font=('times new roman',12))
        email_entry.place(x=300,y=300)
        phoneno_label=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        phoneno_label.place(x=100,y=350)
        phoneno_entry=Entry(c2,width=30,font=('times new roman',12))
        phoneno_entry.place(x=300,y=350)
        regno_label=Label(c2,text='REGISTRATION NO.',font=('times new roman bold',13))
        regno_label.place(x=100,y=400)
        regno_entry=Entry(c2,width=30,font=('times new roman',12))
        regno_entry.place(x=300,y=400)
        
        save_button=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        save_button.place(x=300,y=450)
        close_button=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        close_button.place(x=400,y=450)
    
    def storedeletescreen():
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
        
        def delete():
            xa=int(storeid_entry.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from store where storeid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hi','Data Deleted')    
            storeid_entry.delete(0,100)
            db.close()
        
        def close():
            c2.destroy()
        storedeletescreen_label=Label(c2,text='STORE- DELETE SCREEN',font=('times new roman bold',18))
        storedeletescreen_label.place(x=200,y=25)
        storeid_label=Label(c2,text='STORE ID',font=('times new roman bold',13))
        storeid_label.place(x=200,y=100)
        storeid_entry=ttk.Combobox(c2,font=('times new roman',12))
        storeid_entry.place(x=350,y=100)
        filldata()
        storeid_entry['values']=xt
             
        delete_button=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        delete_button.place(x=250,y=200)
        close_button=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        close_button.place(x=500,y=200)
        
    
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
    
        
    def productcatsavescreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        def checkdata():
            xa=int(aa.get())
            if xa>0:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="select count(*) from productcategory where pcatid=%d"%(xa)
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
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0:
                messagebox.showerror('Hi','Please fill all data')
            else:
                xa=int(aa.get())
                xb=bb.get()
                xc=cc.get()
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="insert into productcategory values(%d,'%s','%s')"%(xa,xb,xc) 
                cur.execute(sql)
                db.commit()
                db.close()
                messagebox.showinfo('Hi','Data Saved')
                aa.delete(0,100)
                bb.delete(0,100)
                cc.delete(0,100)
                
        def close():
            c2.destroy()
            
        a1=Label(c2,text='PRODUCT CATEGORY- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=200,y=25) 
        a=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=300,y=100)
        aab=Button(c2,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
        aab.place(x=575,y=100)
        b=Label(c2,text='CATEGORY NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=300,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=300,y=200)
        e=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        e.place(x=305,y=250)
        f=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        f.place(x=385,y=250)
    
    def productcatupdatescreen():
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
            c2.destroy()
            
        a1=Label(c2,text='PRODUCT CATEGORY- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=200,y=25)      
        a=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        b=Label(c2,text='CATEGORY NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=300,y=150)
        c=Label(c2,text='DESCRIPTION',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=300,y=200)
    
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=300,y=275)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=275)
    
    def productcatdeletescreen():
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
            
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from productcategory where pcatid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')    
            aa.delete(0,100)
        def close():
            c2.destroy()
        a1=Label(c2,text='PRODUCT CATEGORY- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=150,y=25)  
        a=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        a.place(x=150,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=350,y=100)
        filldata()
        aa['values']=xt
            
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
        
    def productsavescreen():
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
            c2.destroy()
        def filldata2():
            xa=int(bb.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select catname from productcategory where pcatid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            aa2.config(text='')
            aa2.config(text=data[0])
           
        a1=Label(c2,text='PRODUCT- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=300,y=100)
        btf=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
        btf.place(x=560,y=100)
        b=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman',12))
        bb.place(x=300,y=150)
        filldata()
        bb['values']=xt
        b1=Button(c2,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=filldata2)
        b1.place(x=560,y=150)
        a2=Label(c2,text='PCAT NAME',font=('times new roman bold',13))
        a2.place(x=100,y=200)
        aa2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa2.place(x=300,y=200)
        c=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        c.place(x=100,y=250)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=300,y=250)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        d.place(x=100,y=300)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=300,y=300)
        e=Label(c2,text='OPEN QTY',font=('times new roman bold',13))
        e.place(x=100,y=350)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=300,y=350)
        f=Label(c2,text='CURRENT QTY',font=('times new roman bold',13))
        f.place(x=100,y=400)
        ff=Entry(c2,width=30,font=('times new roman',12))
        ff.place(x=300,y=400)
        
        
        h=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        h.place(x=305,y=500)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=385,y=500)
    
    def productupdatescreen():
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
            c2.destroy()
        def checkdata():
            xa=int(bb.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select catname from productcategory where pcatid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            aa2.config(text='')
            aa2.config(text=data[0])
            
        a1=Label(c2,text='PRODUCT- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)   
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        b=Label(c2,text='PRODUCT CAT ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman',12))
        bb.place(x=300,y=150)
        fillpdata()
        bb['values']=xp
        bb1=Button(c2,text='FILL DATA',font=('times new roman bold',11),fg='black',bg='orange',command=checkdata)
        bb1.place(x=550,y=150)
        a2=Label(c2,text='PCAT NAME',font=('times new roman bold',13))
        a2.place(x=100,y=200)
        aa2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        aa2.place(x=300,y=200)
        c=Label(c2,text='PRODUCT NAME',font=('times new roman bold',13))
        c.place(x=100,y=250)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=300,y=250)
        d=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        d.place(x=100,y=300)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=300,y=300)
        e=Label(c2,text='OPEN QTY',font=('times new roman bold',13))
        e.place(x=100,y=350)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=300,y=350)
        f=Label(c2,text='CURRENT QTY',font=('times new roman bold',13))
        f.place(x=100,y=400)
        ff=Entry(c2,width=30,font=('times new roman',12))
        ff.place(x=300,y=400)
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=300,y=450)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=450)
    
    def productdeletescreen():
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
            
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from products where productid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')    
            aa.delete(0,100)
            
        def close():
            c2.destroy()
        a1=Label(c2,text='PRODUCT- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)
        a=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman bold',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
         
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
    
    def suppliersavescreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        
        def checkdata():
            xa=int(aa.get())
            if xa>0:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="select count(*) from supplier where supplierid=%d"%(xa)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    messagebox.showinfo('Hi','OK pls go ahead')
                else:
                    messagebox.showerror('Hi','You cannot enter')        
                db.close()
            else:
                messagebox.showerror('Hi','Supplier id cannot be negative')
        def savedata():
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0:
                messagebox.showerror('hi','Please fill all data')
            else:
                xa=int(aa.get())
                xb=bb.get()
                xc=cc.get()
                xd=dd.get()
                xe=ee.get()
                if len(xd)!=10:
                    messagebox.showerror('Hi','Enter valid Phone no.')
                elif not xd.isdigit():
                    messagebox.showerror('Hi','Enter valid Phone no.')
                elif xe.count('@')!=1:
                    messagebox.showerror('Hi','Enter valid Email id')
                elif xe.count('.')!=1:
                    messagebox.showerror('Hi','Enter valid Email id')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into supplier values(%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe) 
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    
                    from_address = "ankit.bizcrum@gmail.com"
                    to_address = ee.get()
        
                    # Create message container - the correct MIME type is multipart/alternative.
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "WELCOME TO NIKITA'S STORE"
                    msg['From'] = from_address
                    msg['To'] = to_address
        
                    # Create the message (HTML).
                    html ="Hi "+str(bb.get())+",<br><br>Thanks for joining our venture and becoming a part of Ankit's Store<br><br>Thanks & Regards,<br>Team Ankit's Store"
        
                    # Record the MIME type - text/html.
                    part1 = MIMEText(html, 'html')
        
                    # Attach parts into message container
                    msg.attach(part1)
        
                    # Credentials
                    username = 'ankit.bizcrum@gmail.com'  
                    password = 'jlfzpwxwamccqvvr'
        
                    # Sending the email
                    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
                    server = smtplib.SMTP('smtp.gmail.com', 587) 
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)  
                    server.sendmail(from_address, to_address, msg.as_string())  
                    server.quit()
                    
                    messagebox.showinfo('Hi','Data Saved & Mail Send')
                    
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd.delete(0,100)
                    ee.delete(0,100)
        def close():
            c2.destroy()
        
        a1=Label(c2,text='SUPPLIER- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)    
        a=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=275,y=100)
        btf=Button(c2,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
        btf.place(x=540,y=100)
        b=Label(c2,text='SUPPLIER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=275,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=275,y=300)
        
        
        h=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        h.place(x=305,y=400)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=385,y=400)
        
    def supplierupdatescreen():
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
        
        def checkdetail():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select sname,address,phone,email from supplier where supplierid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            bb.insert(0,data[0])
            cc.insert(0,data[1])
            dd.insert(0,data[2])
            ee.insert(0,data[3])   
        def updatedata():
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()
            if len(xd)!=10:
                messagebox.showerror('Hi','Enter valid Phone no.')
            elif not xd.isdigit():
                messagebox.showerror('Hi','Enter valid Phone no.')
            elif xe.count('@')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            elif xe.count('.')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="update supplier set sname='%s',address='%s',phone='%s',email='%s' where supplierid=%d"%(xb,xc,xd,xe,xa)  
                cur.execute(sql)
                data=cur.fetchone()
                db.commit()
                db.close()
                messagebox.showinfo('Hi','Data Updated')
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
        def close():
            c2.destroy()
        a1=Label(c2,text='SUPPLIER- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)   
        a=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        b=Label(c2,text='SUPPLIER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=300,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=300,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=300,y=250)
        e=Label(c2,text='EMAIL',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=300,y=300)
        
        
        i=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        i.place(x=300,y=375)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=400,y=375)
    
    def supplierdeletescreen():
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
            
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from supplier where supplierid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')    
            aa.delete(0,100)
            
        def close():
            c2.destroy()
        a1=Label(c2,text='SUPPLIER- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)
        a=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman bold',12))
        aa.place(x=300,y=100)
        filldata()
        aa['values']=xt
         
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
    
    def stockinsavescreen():
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
        xv=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from productcategory"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xv.append(res[0])
            db.close()
        xw=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()
        
        def checkdata():
            xa=int(aa.get())
            if xa>0:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="select count(*)from stockin where stockinid=%d"%xa
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    messagebox.showinfo('Hi','Please go ahead')
                else:
                    messagebox.showerror('Hi','You cannot enter')
                db.close()
            else:
                messagebox.showerror('Hi','Stockin id cannot be negative')
        
        def savedata():
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ff.get())==0:
                messagebox.showerror('Hi','Please fill all data')
            else:
                xa=int(aa.get())
                xb=int(bb.get())
                xc=int(cc.get())
                xd=int(dd.get())
                xe=ee.cget("text")
                xf=int(ff.get())
                if xf<0:
                    messagebox.showerror('Hi','Stockin id cannot be negative')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into stockin values (%d,%d,%d,%d,'%s',%d)"%(xa,xb,xc,xd,xe,xf)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    updatestockdata()
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd.delete(0,100)
                    ff.delete(0,100) 
                    dd.delete(0,100) 
                    messagebox.showinfo(' ','Data Added')
            
        def close():
            c2.destroy()
        def date():
            xa=datetime.datetime.now().date()
            ee.config(text=str(xa))    
        def updatestockdata():
            xd=int(dd.get())
            xf=int(ff.get()) #qty
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update products set currentqty=currentqty+%d where productid=%d"%(xf,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi ','Stock updated...')
        a1=Label(c2,text='STOCK IN- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='STOCK ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=250,y=100)
        aaa=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
        aaa.place(x=500,y=100)
        b=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman bold',12))
        bb.place(x=250,y=150)
        filldata()
        bb['values']=xt
        c=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=ttk.Combobox(c2,font=('times new roman bold',12))
        cc.place(x=250,y=200)
        filleddata()
        cc['values']=xv
        d=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=ttk.Combobox(c2,font=('times new roman bold',12))
        dd.place(x=250,y=250)
        fildata()
        dd['values']=xw
        e=Label(c2,text='DATE IN',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Label(c2,width=30,font=('times new roman',12),anchor='w')
        date()
        ee.place(x=250,y=300)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=350)
        ff=Entry(c2,width=30,font=('times new roman',12))
        ff.place(x=250,y=350)
        h=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        h.place(x=305,y=450)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=385,y=450)
    
    def stockinupdatescreen():
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
        xs=[]
        def fillsdata():
             db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
             cur=db.cursor()
             sql="select supplierid from supplier"
             cur.execute(sql)
             data=cur.fetchall()
             for res in data:
                 xs.append(res[0])
             db.close()
        xv=[]
        def filleddata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid from productcategory"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xv.append(res[0])
            db.close()
        xw=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()
        def checkdetail():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select supplierid,pcatid,productid,datein,qty from stockin where stockinid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
            bb.insert(0,data[0])
            cc.insert(0,data[1])
            dd.insert(0,data[2])
            ee.insert(0,data[3])
            ff.insert(0,data[4])
            db.close()
        
        def updatedata():
            xa=int(aa.get())
            xb=int(bb.get())
            xc=int(cc.get())
            xd=int(dd.get())
            xe=ee.get()
            xf=int(ff.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update stockin set supplierid=%d,pcatid=%d,productid=%d,datein='%s',qty=%d where stockinid=%d"%(xb,xc,xd,xe,xf,xa)
            cur.execute(sql)
            data=cur.fetchone()
            db.commit()
            db.close()
            messagebox.showinfo('Hi'," Data Updated")
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            ff.delete(0,100)
           
        def close():
            c2.destroy()
        a1=Label(c2,text='STOCK IN- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='STOCK ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        b=Label(c2,text='SUPPLIER ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman bold',12))
        bb.place(x=250,y=150)
        fillsdata()
        bb['values']=xs
        c=Label(c2,text='PCAT ID',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=ttk.Combobox(c2,font=('times new roman bold',12))
        cc.place(x=250,y=200)
        filleddata()
        cc['values']=xv
        d=Label(c2,text='PRODUCT ID',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=ttk.Combobox(c2,font=('times new roman bold',12))
        dd.place(x=250,y=250)
        fildata()
        dd['values']=xw
        e=Label(c2,text='DATE IN',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=250,y=300)
        f=Label(c2,text='QTY',font=('times new roman bold',13))
        f.place(x=100,y=350)
        ff=Entry(c2,width=30,font=('times new roman',12))
        ff.place(x=250,y=350)
        
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=250,y=400)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=400)
    
    def stockindeletescreen():
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
        
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from stockin where stockinid=%d"%xa
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')
            aa.delete(0,100)
        def close():
            c2.destroy()
        a1=Label(c2,text='STOCK IN- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)
        a=Label(c2,text='STOCK ID',font=('times new roman bold',13))
        a.place(x=230,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=350,y=100)
        filldata()
        aa['values']=xt
        
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
        
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
    
    def customerssavescreen():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        def checkdata():
            xa=int(aa.get())
            if xa>0:
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="select count(*)from customers where custid=%d"%xa
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    messagebox.showinfo('Hi','Please go ahead')
                else:
                    messagebox.showerror('Hi','You cannot enter')
                db.close()
            else:
                messagebox.showerror('Hi','Customer id cannot be negative')
        
        def savedata():
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd.get())==0 or len(ee.get())==0:
                messagebox.showerror('Hi','Please fill all data')
            else:
                xa=int(aa.get())
                xb=bb.get()
                xc=cc.get()
                xd=dd.get()
                xe=ee.get()
                if len(xd)!=10:
                    messagebox.showerror('Hi','Enter valid Phone no.')
                elif not xd.isdigit():
                    messagebox.showerror('Hi','Enter valid Phone no.')
                elif xe.count('@gmail.com')!=1:
                    messagebox.showerror('Hi','Enter valid Email id')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into customers values (%d,'%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                                
                    from_address = "ankit.bizcrum@gmail.com"
                    to_address = ee.get()
        
                    # Create message container - the correct MIME type is multipart/alternative.
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "WELCOME TO ANKIT'S STORE"
                    msg['From'] = from_address
                    msg['To'] = to_address
        
                    # Create the message (HTML).
                    html ="Hi "+str(bb.get())+",<br><br>Thanks for becoming a part of Ankit's Store<br>We look forward to serve you better and better everyday<br><br>Happy Shoping,<br>Team Ankit's Store"
        
                    # Record the MIME type - text/html.
                    part1 = MIMEText(html, 'html')
        
                    # Attach parts into message container
                    msg.attach(part1)
        
                    # Credentials
                    username = 'ankit.bizcrum@gmail.com'  
                    password = 'jlfzpwxwamccqvvr'
        
                    # Sending the email
                    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
                    server = smtplib.SMTP('smtp.gmail.com', 587) 
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)  
                    server.sendmail(from_address, to_address, msg.as_string())  
                    server.quit()
                    
                    messagebox.showinfo('Hi','Data Saved & Mail Send')
                
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd.delete(0,100)
                    ee.delete(0,100) 
        def close():
            c2.destroy()
        a1=Label(c2,text='CUSTOMER- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)    
        a=Label(c2,text='CUSTOMER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=275,y=100)
        aaa=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
        aaa.place(x=550,y=100)
        b=Label(c2,text='CUSTOMER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=275,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL ID',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=275,y=300)
        g=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        g.place(x=305,y=400)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=385,y=400)
    
    def customersupdatescreen():
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
        def checkdetail():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select cname,address,phone,email from customers where custid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.delete(0,100)
            cc.delete(0,100)
            dd.delete(0,100)
            ee.delete(0,100)
            bb.insert(0,data[0])
            cc.insert(0,data[1])
            dd.insert(0,data[2])
            ee.insert(0,data[3])
            db.close()
        
        def updatedata():
            xa=int(aa.get())
            xb=bb.get()
            xc=cc.get()
            xd=dd.get()
            xe=ee.get()
            if len(xd)!=10:
                messagebox.showerror('Hi','Enter valid Phone no.')
            elif not xd.isdigit():
                messagebox.showerror('Hi','Enter valid Phone no.')
            elif xe.count('@')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            elif xe.count('.')!=1:
                messagebox.showerror('Hi','Enter valid Email id')
            else:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="update customers set cname='%s',address='%s',phone='%s',email='%s' where custid=%d"%(xb,xc,xd,xe,xa)
                cur.execute(sql)
                data=cur.fetchone()
                db.commit()
                db.close()
                messagebox.showinfo('Hi',"Data Updated")
                aa.delete(0,100)
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
               
        def close():
            c2.destroy()
        a1=Label(c2,text='CUSTOMER- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)    
        a=Label(c2,text='CUSTOMER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=275,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        b=Label(c2,text='CUSTOMER NAME',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=Entry(c2,width=30,font=('times new roman',12))
        bb.place(x=275,y=150)
        c=Label(c2,text='ADDRESS',font=('times new roman bold',13))
        c.place(x=100,y=200)
        cc=Entry(c2,width=30,font=('times new roman',12))
        cc.place(x=275,y=200)
        d=Label(c2,text='PHONE NO.',font=('times new roman bold',13))
        d.place(x=100,y=250)
        dd=Entry(c2,width=30,font=('times new roman',12))
        dd.place(x=275,y=250)
        e=Label(c2,text='EMAIL ID',font=('times new roman bold',13))
        e.place(x=100,y=300)
        ee=Entry(c2,width=30,font=('times new roman',12))
        ee.place(x=275,y=300)
        
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=300,y=400)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=400)
    
    def customersdeletescreen():
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
            c2.destroy()
        
        a1=Label(c2,text='CUSTOMER- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=250,y=25)
        a=Label(c2,text='CUSTOMER ID',font=('times new roman bold',13))
        a.place(x=250,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=400,y=100)
        filldata()
        aa['values']=xt
        
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
    
    def orderssavescreen():
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
        xw=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()
        def checkdata():
            xa=int(aa.get())
            if xa>0:
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="select count(*)from orders where orderid=%d"%xa
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    messagebox.showinfo('Hi','Please go ahead')
                else:
                    messagebox.showerror('Hi','You cannot enter')
                db.close()
            else:
                messagebox.showerror('Hi','Order id cannot be negative')
        
        def savedata():
            if len(aa.get())==0 or len(bb.get())==0 or len(cc.get())==0 or len(dd1.get())==0 :
                messagebox.showerror('Hi','Please fill all data')
            else:
                xa=int(aa.get())
                xb=int(bb.get())
                xc=bb5.cget("text")
                xd=bb4.cget("text")
                xe=int(cc.get())
                xf=int(dd.cget("text"))
                xg=bb6.cget("text")
                xh=ee.cget("text")
                xi=int(ff.cget("text"))
                xj=int(dd1.get())
                xk=int(dd2.cget("text"))
                if xj<=0:
                    messagebox.showerror('Hi','Invalid qty')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                    cur=db.cursor()
                    sql="insert into orders values (%d,%d,'%s','%s',%d,%d,'%s','%s',%d,%d,%d)"%(xa,xb,xc,xd,xe,xf,xg,xh,xi,xj,xk)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    updatestockdata()
                    from_address = "ankit.bizcrum@gmail.com"
                    to_address = bb4.cget("text")
    
                    # Create message container - the correct MIME type is multipart/alternative.
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = "THANKS FOR SHOPPING WITH ANKIT'S STORE"
                    msg['From'] = from_address
                    msg['To'] = to_address
    
                    # Create the message (HTML).
                    html ="Hi "+str(bb5.cget("text"))+",<br><br>Thanks for shopping with Ankit's Store.<br>Your Total bill is of Rs."+str(dd2.cget("text"))+" for purchase of "+str(dd1.get())+" "+str(bb6.cget("text"))+".<br><br>Will notify you once your order is dispatched.<br><br>Keep Shoping with us.<br><br>Thanks & Regards,<br>Team Ankit's Store"
    
                    # Record the MIME type - text/html.
                    part1 = MIMEText(html, 'html')
    
                    # Attach parts into message container
                    msg.attach(part1)
    
                    # Credentials
                    username = 'ankit.bizcrum@gmail.com'  
                    password = 'jlfzpwxwamccqvvr'
    
                    # Sending the email
                    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
                    server = smtplib.SMTP('smtp.gmail.com', 587) 
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)  
                    server.sendmail(from_address, to_address, msg.as_string())  
                    server.quit()
                    
                    messagebox.showinfo('Hi','Order received & Mail Send')
                    
                    aa.delete(0,100)
                    bb.delete(0,100)
                    cc.delete(0,100)
                    dd1.delete(0,100)
                    bb4.config(text='')
                    bb5.config(text='')
                    bb6.config(text='')
                    dd.config(text='')
                    ee.config(text='')
                    ff.config(text='')
                    dd2.config(text='')
                    
        def close():
            c2.destroy()
            
        def date():
            xa=datetime.datetime.now().date()
            ee.config(text=str(xa)) 
            
        def checkdata2():
            xa=int(bb.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select cname,email from customers where custid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb5.config(text=data[0])
            bb4.config(text=data[1])
            db.close()
        def calc():
            xa=int(ff.cget("text"))
            xb=int(dd1.get())
            xc=xa*xb
            dd2.config(text=str(xc))
        def productfill():
            xa=int(cc.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid,productname,priceperunit from products where productid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            dd.config(text=data[0])
            bb6.config(text=data[1])
            ff.config(text=data[2])
            db.close()
        def updatestockdata():
            xd=int(cc.get())
            xf=int(dd1.get()) #qty
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update products set currentqty=currentqty-%d where productid=%d"%(xf,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi ','Stock updated...')
        a1=Label(c2,text='ORDER- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)      
        a=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=250,y=100)
        aaa=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
        aaa.place(x=550,y=100)
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman',12))
        bb.place(x=250,y=150)
        filldata()
        bb['values']=xt
        a1=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
        a1.place(x=550,y=150)
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
        cc=ttk.Combobox(c2,font=('times new roman',12))
        cc.place(x=250,y=300)
        fildata()
        cc['values']=xw
        a1=Button(c2,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=productfill)
        a1.place(x=550,y=300)
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
        date()
        ee.place(x=250,y=450)
        f=Label(c2,text='PRICE PER UNIT',font=('times new roman bold',13))
        f.place(x=100,y=500)
        ff=Label(c2,width=26,font=('times new roman',12),anchor='w')
        ff.place(x=250,y=500)
        ff.config(text='0')
        d1=Label(c2,text='QTY',font=('times new roman bold',13))
        d1.place(x=100,y=550)
        dd1=Spinbox(c2,from_=0,to=100,font=('times new roman',12),command=calc)
        dd1.insert(0,'0')
        dd1.place(x=250,y=550)
        d2=Label(c2,text='BILL',font=('times new roman bold',13))
        d2.place(x=100,y=600)
        dd2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd2.config(text='0')
        dd2.place(x=250,y=600)
        g=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        g.place(x=305,y=650)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=385,y=650)
    
    def ordersupdatescreen():
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
        def checkdetail():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid,cname,cemail,productid,pcatid,pname,dateoforder,priceperunit,qty,bill from orders where orderid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.delete(0,100)
            cc.delete(0,100)
            dd1.delete(0,100)
            bb4.config(text='')
            bb5.config(text='')
            bb6.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            dd2.config(text='')
            bb.insert(0,data[0])
            bb5.config(text=data[1])
            bb4.config(text=data[2])
            cc.insert(0,data[3])
            dd.config(text=data[4])
            bb6.config(text=data[5])
            ee.config(text=data[6])
            ff.config(text=data[7])
            dd1.insert(0,data[8])
            dd2.config(text=data[9])
            
            db.close()
        
        def updatedata():
            xa=int(aa.get())
            xb=int(bb.get())
            xc=bb5.cget("text")
            xd=bb4.cget("text")
            xe=int(cc.get())
            xf=int(dd.cget("text"))
            xg=bb6.cget("text")
            xh=ee.cget("text")
            xi=int(ff.cget("text"))
            xj=int(dd1.get())
            xk=int(dd2.cget("text"))
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update orders set custid=%d,cname='%s',cemail='%s',productid=%d,pcatid=%d,pname='%s',dateoforder='%s',priceperunit=%d,qty=%d,bill=%d where orderid=%d"%(xb,xc,xd,xe,xf,xg,xh,xi,xj,xk,xa)
            cur.execute(sql)
            data=cur.fetchone()
            db.commit()
            db.close()
            messagebox.showinfo('Hi',"Data Updated")
            aa.delete(0,100)
            bb.delete(0,100)
            cc.delete(0,100)
            dd1.delete(0,100)
            bb4.config(text='')
            bb5.config(text='')
            bb6.config(text='')
            dd.config(text='')
            ee.config(text='')
            ff.config(text='')
            dd2.config(text='')
            
           
        def close():
            c2.destroy()
    
        xc=[]
        def fillcdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid from customers"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xc.append(res[0])
            db.close()
        xw=[]
        def fildata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select productid from products"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xw.append(res[0])
            db.close()    
    
        def checkdata2():
            xa=int(bb.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select cname,email from customers where custid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb5.config(text=data[0])
            bb4.config(text=data[1])
            db.close()
            
        def calc():
            xa=int(ff.cget("text"))
            xb=int(dd1.get())
            xc=xa*xb
            dd2.config(text=str(xc))
        def productfill():
            xa=int(cc.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select pcatid,productname,priceperunit from products where productid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            dd.config(text=data[0])
            bb6.config(text=data[1])
            ff.config(text=data[2])
            db.close()    
            
        a1=Label(c2,text='ORDER- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)      
        a=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        b=Label(c2,text='CUST ID',font=('times new roman bold',13))
        b.place(x=100,y=150)
        bb=ttk.Combobox(c2,font=('times new roman',12))
        bb.place(x=250,y=150)
        fillcdata()
        bb['values']=xc
        a1=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
        a1.place(x=550,y=150)
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
        cc=ttk.Combobox(c2,font=('times new roman',12))
        cc.place(x=250,y=300)
        fildata()
        cc['values']=xw
        a1=Button(c2,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=productfill)
        a1.place(x=550,y=300)
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
        ff.config(text='0')
        d1=Label(c2,text='QTY',font=('times new roman bold',13))
        d1.place(x=100,y=550)
        dd1=Spinbox(c2,from_=0,to=100,font=('times new roman',12),command=calc)
        dd1.insert(0,'0')
        dd1.place(x=250,y=550)
        d2=Label(c2,text='BILL',font=('times new roman bold',13))
        d2.place(x=100,y=600)
        dd2=Label(c2,width=26,font=('times new roman',12),anchor='w')
        dd2.config(text='0')
        dd2.place(x=250,y=600)
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=225,y=700)
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=400,y=700)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=500,y=700)
    
    def ordersdeletescreen():
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
        
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from orders where orderid=%d"%xa
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')
        def close():
            c2.destroy()
         
        a1=Label(c2,text='ORDER- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)    
        a=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a.place(x=230,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=380,y=100)
        filldata()
        aa['values']=xt
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
    
    def dispatchbillsavescreen():
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
        def checkdata():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select count(*)from dispatchorder where dispatchid=%d"%xa
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('Hi','Please go ahead')
            else:
                messagebox.showerror('Hi','You cannot enter')
            db.close()
        
        def savedata():
            if len(aa.get())==0 or len(aa4.get())==0 :
                messagebox.showerror('Hi','Please fill all data')
            else:
                xa=int(aa.get())
                xa1=int(aa4.get())
                xb=int(bb.cget("text"))
                xb1=bb5.cget("text")
                xb2=bb4.cget("text")
                xc=int(cc.cget("text"))
                xd=int(dd.cget("text"))
                xd1=dd1.cget("text")
                xe=ee.cget("text")
                xe1=int(ee1.cget("text"))
                xf=int(ff.cget("text"))
                xf1=int(ff1.cget("text"))
                
                db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
                cur=db.cursor()
                sql="insert into dispatchorder values (%d,%d,%d,'%s','%s',%d,%d,'%s','%s',%d,%d,%d)"%(xa,xa1,xb,xb1,xb2,xc,xd,xd1,xe,xe1,xf,xf1)
                cur.execute(sql)
                db.commit()
                db.close()
                
                from_address = "ankit.bizcrum@gmail.com"
                to_address = bb4.cget("text")
    
                # Create message container - the correct MIME type is multipart/alternative.
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "ORDER DISPATCHED"
                msg['From'] = from_address
                msg['To'] = to_address
    
                # Create the message (HTML).
                html ="Hi "+str(bb5.cget("text"))+",<br><br>Your total bill is Rs."+str(ff1.get())+"against Order No."+str(aa4.get())+". Your product- "+str((dd1.get))+" has dispatched and will reach you within 4-5 working days.<br><br>Keep Shoping with us.<br><br>Thanks & Regards,<br>Team Ankit's Store"
    
                # Record the MIME type - text/html.
                part1 = MIMEText(html, 'html')
    
                # Attach parts into message container
                msg.attach(part1)
    
                # Credentials
                username = 'ankit.bizcrum@gmail.com'  
                password = 'jlfzpwxwamccqvvr'
    
                # Sending the email
                ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
                server = smtplib.SMTP('smtp.gmail.com', 587) 
                server.ehlo()
                server.starttls()
                server.login(username,password)  
                server.sendmail(from_address, to_address, msg.as_string())  
                server.quit()
                
                messagebox.showinfo('Hi','Order dispatched & Mail Send')
            
                aa.delete(0,100)
                aa4.delete(0,100)
                bb.config(text='')
                bb5.config(text='')
                bb4.config(text='')
                cc.config(text='')
                dd.config(text='')
                dd1.config(text='')
                ee1.config(text='')
                ff.config(text='') 
                ff1.config(text='')
                
            
        def close():
            c2.destroy()
        def date():
            xa=datetime.datetime.now().date()
            ee.config(text=str(xa))    
           
        def checkdata2():
            xa=int(aa4.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid,cname,cemail,productid,pcatid,pname,priceperunit,qty,bill from orders where orderid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            bb5.config(text='')
            bb4.config(text='')
            cc.config(text='')
            dd.config(text='')
            dd1.config(text='')
            ee1.config(text='')
            ff.config(text='')
            ff1.config(text='')
            bb.config(text=data[0])
            bb5.config(text=data[1])
            bb4.config(text=data[2])
            cc.config(text=data[3])
            dd.config(text=data[4])
            dd1.config(text=data[5])
            ee1.config(text=data[6])
            ff.config(text=data[7])
            ff1.config(text=data[8])
            db.close()
            
        a1=Label(c2,text='DISPATCH BILL- SAVE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)
        a=Label(c2,text='DISPATCH ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=Entry(c2,width=30,font=('times new roman',12))
        aa.place(x=250,y=100)
        aaa=Button(c2,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
        aaa.place(x=550,y=100)
        a4=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a4.place(x=100,y=150)
        aa4=ttk.Combobox(c2,font=('times new roman',12))
        aa4.place(x=250,y=150)
        filldata()
        aa4['values']=xt
        a5=Button(c2,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
        a5.place(x=550,y=150)
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
        date()
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
        g=Button(c2,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
        g.place(x=305,y=700)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=385,y=700)
    
    def dispatchbillupdatescreen():
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
        xo=[]
        def fillodata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select orderid from orders"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                xo.append(res[0])
            db.close()
        def checkdetail():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select orderid,custid,custname,custemail,productid,pcatid,productname,dispatchdate,price,qty,bill from dispatchorder where dispatchid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            aa4.delete(0,100)
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
            aa4.insert(0,data[0])
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
            db.close()
        
        def updatedata():
            xa=int(aa.get())
            xa1=int(aa4.get())
            xb=int(bb.cget("text"))
            xb1=bb5.cget("text")
            xb2=bb4.cget("text")
            xc=int(cc.cget("text"))
            xd=int(dd.cget("text"))
            xd1=dd1.cget("text")
            xe=ee.cget("text")
            xe1=int(ee1.cget("text"))
            xf=int(ff.cget("text"))
            xf1=int(ff1.cget("text"))
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="update dispatchorder set orderid=%d,custid=%d,custname='%s',custemail='%s',productid=%d,pcatid=%d,productname='%s',dispatchdate='%s',price='%s',qty=%d,bill=%d where dispatchid=%d"%(xa1,xb,xb1,xb2,xc,xd,xd1,xe,xe1,xf,xf1,xa)
            cur.execute(sql)
            data=cur.fetchone()
            db.commit()
            db.close()
            messagebox.showinfo('Hi',"Data Updated")
            aa.delete(0,100)
            aa4.delete(0,100)
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
           
        def close():
            c2.destroy()
        def checkdata2():
            xa=int(aa4.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="select custid,cname,cemail,productid,pcatid,pname,priceperunit,qty,bill from orders where orderid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            bb.config(text='')
            bb5.config(text='')
            bb4.config(text='')
            cc.config(text='')
            dd.config(text='')
            dd1.config(text='')
            ee1.config(text='')
            ff.config(text='')
            ff1.config(text='')
            bb.config(text=data[0])
            bb5.config(text=data[1])
            bb4.config(text=data[2])
            cc.config(text=data[3])
            dd.config(text=data[4])
            dd1.config(text=data[5])
            ee1.config(text=data[6])
            ff.config(text=data[7])
            ff1.config(text=data[8])
            db.close()
            
        a1=Label(c2,text='DISPATCH BILL- UPDATE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)   
        a=Label(c2,text='DISPATCH ID',font=('times new roman bold',13))
        a.place(x=100,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=250,y=100)
        filldata()
        aa['values']=xt
        i=Button(c2,text='CHECK DETAILS',font=('times new roman bold',11),fg='white',bg='green',command=checkdetail)
        i.place(x=550,y=100)
        a4=Label(c2,text='ORDER ID',font=('times new roman bold',13))
        a4.place(x=100,y=150)
        aa4=ttk.Combobox(c2,font=('times new roman',12))
        aa4.place(x=250,y=150)
        fillodata()
        aa4['values']=xo
        a5=Button(c2,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
        a5.place(x=550,y=150)
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
        
        g=Button(c2,text='UPDATE',font=('times new roman bold',11),bg='orange',command=updatedata)
        g.place(x=300,y=700)
        h=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        h.place(x=400,y=700)
    
    def dispatchbilldeletescreen():
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
        
        def delete():
            xa=int(aa.get())
            db=pymysql.connect(host='localhost',user='root',password='root',database='sms')
            cur=db.cursor()
            sql="delete from dispatchorder where dispatchid=%d"%xa
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Data Deleted')
        def close():
            c2.destroy()
        a1=Label(c2,text='DISPATCH BILL- DELETE SCREEN',font=('times new roman bold',18))
        a1.place(x=230,y=25)
        a=Label(c2,text='DISPATCH ID',font=('times new roman bold',13))
        a.place(x=230,y=100)
        aa=ttk.Combobox(c2,font=('times new roman',12))
        aa.place(x=380,y=100)
        filldata()
        aa['values']=xt
        h=Button(c2,text='DELETE',font=('times new roman bold',11),bg='red',command=delete)
        h.place(x=250,y=200)
        refresh=Button(c2,text='REFRESH DATA',font=('times new roman bold',11),bg='orange')
        refresh.place(x=350,y=200)
        j=Button(c2,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
        j.place(x=500,y=200)
    
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
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=storesavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=storeupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=storedeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=storefindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=storeshowscreen)
        b1.place(x=300,y=500)
    
    def productcatbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - PRODUCTS CATEGORY',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=15,y=25) 
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=productcatsavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=productcatupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=productcatdeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=productcatfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=productcatshowscreen)
        b1.place(x=300,y=500)
    
    def productbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - PRODUCTS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=70,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=productsavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=productupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=productdeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=productfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=productshowscreen)
        b1.place(x=300,y=500)
    
    def supplierbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - SUPPLIERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=90,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=suppliersavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=supplierupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=supplierdeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=supplierfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=suppliershowscreen)
        b1.place(x=300,y=500)
    
    def stockinbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - STOCKIN',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=100,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=stockinsavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=stockinupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=stockindeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=stockinfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=stockinshowscreen)
        b1.place(x=300,y=500)
    
    def customersbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - CUSTOMERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=70,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=customerssavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=customersupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=customersdeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=customersfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=customersshowscreen)
        b1.place(x=300,y=500)
    
    def ordersbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - ORDERS',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=100,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=orderssavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=ordersupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=ordersdeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=ordersfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=ordersshowscreen)
        b1.place(x=300,y=500)
    
    def dispatchbillbuttons():
        c2=Canvas(t,height=900,width=725,bg='light blue')
        c2.place(x=200,y=0)
        a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - DISPATCH BILL',font=('times new roman bold',18),fg='white',bg='midnight blue')
        a1.place(x=50,y=25)
        b1=Button(c2,text='INSERT',font=('times new roman bold',14),bg='green',fg='WHITE',command=dispatchbillsavescreen)
        b1.place(x=300,y=100)
        b1=Button(c2,text='UPDATE',font=('times new roman bold',14),bg='orange',fg='black',command=dispatchbillupdatescreen)
        b1.place(x=300,y=200)
        b1=Button(c2,text='DELETE',font=('times new roman bold',14),bg='red',fg='black',command=dispatchbilldeletescreen)
        b1.place(x=300,y=300)
        b1=Button(c2,text='FIND',font=('times new roman bold',14),bg='yellow',fg='black',command=dispatchbillfindscreen)
        b1.place(x=300,y=400)
        b1=Button(c2,text='SHOW',font=('times new roman bold',14),bg='blue',fg='WHITE',command=dispatchbillshowscreen)
        b1.place(x=300,y=500)
    
    
    c1=Canvas(t,height=900,width=200,bg='teal')
    c1.place(x=0,y=0)
    c2=Canvas(t,height=900,width=725,bg='light blue')
    c2.place(x=200,y=0)
    a1=Label(c2,text='STOCK MANAGEMENT SYSTEM - ADMIN',font=('times new roman bold',20),fg='white',bg='midnight blue')
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