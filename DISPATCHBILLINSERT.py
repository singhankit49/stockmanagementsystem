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
def dispatchbillsavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title ('DISPATCH BILL')
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
            
            from_address = "nikkie081297@gmail.com"
            to_address = bb4.cget("text")

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "ORDER DISPATCHED"
            msg['From'] = from_address
            msg['To'] = to_address

            # Create the message (HTML).
            html ="Hi "+str(bb5.cget("text"))+",<br><br>Your Order No."+str(aa4.get())+" is dispatched and will reach you within 4-5 working days.<br><br>Keep Shoping with us.<br><br>Thanks & Regards,<br>Team Nikita's Store"

            # Record the MIME type - text/html.
            part1 = MIMEText(html, 'html')

            # Attach parts into message container
            msg.attach(part1)

            # Credentials
            username = 'nikkie081297@gmail.com'  
            password = ''

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
        t.destroy()
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
        
    a1=Label(t,text='DISPATCH BILL- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)
    a=Label(t,text='DISPATCH ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=250,y=100)
    aaa=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
    aaa.place(x=550,y=100)
    a4=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a4.place(x=100,y=150)
    aa4=ttk.Combobox(t,font=('times new roman',12))
    aa4.place(x=250,y=150)
    filldata()
    aa4['values']=xt
    a5=Button(t,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
    a5.place(x=550,y=150)
    b=Label(t,text='CUST ID',font=('times new roman bold',13))
    b.place(x=100,y=200)
    bb=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb.place(x=250,y=200)
    b5=Label(t,text='CUST NAME',font=('times new roman bold',13))
    b5.place(x=100,y=250)
    bb5=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb5.place(x=250,y=250)
    b4=Label(t,text='CUST EMAIL ID',font=('times new roman bold',13))
    b4.place(x=100,y=300)
    bb4=Label(t,width=30,font=('times new roman',12),anchor='w')
    bb4.place(x=250,y=300)
    c=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    c.place(x=100,y=350)
    cc=Label(t,width=30,font=('times new roman',12),anchor='w')
    cc.place(x=250,y=350)
    d=Label(t,text='PCAT ID',font=('times new roman bold',13))
    d.place(x=100,y=400)
    dd=Label(t,width=30,font=('times new roman',12),anchor='w')
    dd.place(x=250,y=400)
    d1=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    d1.place(x=100,y=450)
    dd1=Label(t,width=30,font=('times new roman',12),anchor='w')
    dd1.place(x=250,y=450)
    e=Label(t,text='DISPATCH DATE',font=('times new roman bold',13))
    e.place(x=100,y=500)
    ee=Label(t,width=30,font=('times new roman',12),anchor='w')
    date()
    ee.place(x=250,y=500)
    e1=Label(t,text='PRICE',font=('times new roman bold',13))
    e1.place(x=100,y=550)
    ee1=Label(t,width=30,font=('times new roman',12),anchor='w')
    ee1.place(x=250,y=550)
    f=Label(t,text='QTY',font=('times new roman bold',13))
    f.place(x=100,y=600)
    ff=Label(t,width=30,font=('times new roman',12),anchor='w')
    ff.place(x=250,y=600)
    f1=Label(t,text='BILL',font=('times new roman bold',13))
    f1.place(x=100,y=650)
    ff1=Label(t,width=30,font=('times new roman',12),anchor='w')
    ff1.place(x=250,y=650)
    g=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    g.place(x=305,y=700)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=385,y=700)
    
    t.mainloop()
