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
 
def orderssavescreen():
    t=tkinter.Tk()
    t.geometry('800x8600')
    t.title ('ORDERS')
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
                from_address = "nikkie081297@gmail.com"
                to_address = bb4.cget("text")

                # Create message container - the correct MIME type is multipart/alternative.
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "THANKS FOR SHOPPING WITH NIKITA'S STORE"
                msg['From'] = from_address
                msg['To'] = to_address

                # Create the message (HTML).
                html ="Hi "+str(bb5.cget("text"))+",<br><br>Thanks for shopping with Nikita's Store.<br>Your Total bill is of Rs."+str(dd2.cget("text"))+" for purchase of "+str(dd1.get())+" "+str(bb6.cget("text"))+".<br><br>Will notify you once your order is dispatched.<br><br>Keep Shoping with us.<br><br>Thanks & Regards,<br>Team Nikita's Store"

                # Record the MIME type - text/html.
                part1 = MIMEText(html, 'html')

                # Attach parts into message container
                msg.attach(part1)

                # Credentials
                username = 'nikkie081297@gmail.com'  
                password = 'nbiqexxsciicwuig'

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
        t.destroy()
        
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
    a1=Label(t,text='ORDER- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=230,y=25)      
    a=Label(t,text='ORDER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=250,y=100)
    aaa=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata)
    aaa.place(x=550,y=100)
    b=Label(t,text='CUST ID',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=ttk.Combobox(t,font=('times new roman',12))
    bb.place(x=250,y=150)
    filldata()
    bb['values']=xt
    a1=Button(t,text='CHECK DATA',font=('times new roman bold',11),bg='orange',command=checkdata2)
    a1.place(x=550,y=150)
    b5=Label(t,text='CUST NAME',font=('times new roman bold',13))
    b5.place(x=100,y=200)
    bb5=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb5.place(x=250,y=200)
    b4=Label(t,text='CUST EMAIL ID',font=('times new roman bold',13))
    b4.place(x=100,y=250)
    bb4=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb4.place(x=250,y=250)
    c=Label(t,text='PRODUCT ID',font=('times new roman bold',13))
    c.place(x=100,y=300)
    cc=ttk.Combobox(t,font=('times new roman',12))
    cc.place(x=250,y=300)
    fildata()
    cc['values']=xw
    a1=Button(t,text='FILL DATA',font=('times new roman bold',11),bg='orange',command=productfill)
    a1.place(x=550,y=300)
    d=Label(t,text='PCAT ID',font=('times new roman bold',13))
    d.place(x=100,y=350)
    dd=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd.place(x=250,y=350)
    b6=Label(t,text='PRODUCT NAME',font=('times new roman bold',13))
    b6.place(x=100,y=400)
    bb6=Label(t,width=26,font=('times new roman',12),anchor='w')
    bb6.place(x=250,y=400)
    e=Label(t,text='DATE OF ORDER',font=('times new roman bold',13))
    e.place(x=100,y=450)
    ee=Label(t,width=26,font=('times new roman',12),anchor='w')
    date()
    ee.place(x=250,y=450)
    f=Label(t,text='PRICE PER UNIT',font=('times new roman bold',13))
    f.place(x=100,y=500)
    ff=Label(t,width=26,font=('times new roman',12),anchor='w')
    ff.place(x=250,y=500)
    ff.config(text='0')
    d1=Label(t,text='QTY',font=('times new roman bold',13))
    d1.place(x=100,y=550)
    dd1=Spinbox(t,from_=0,to=100,font=('times new roman',12),command=calc)
    dd1.insert(0,'0')
    dd1.place(x=250,y=550)
    d2=Label(t,text='BILL',font=('times new roman bold',13))
    d2.place(x=100,y=600)
    dd2=Label(t,width=26,font=('times new roman',12),anchor='w')
    dd2.config(text='0')
    dd2.place(x=250,y=600)
    g=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    g.place(x=305,y=650)
    h=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    h.place(x=385,y=650)
    
    t.mainloop()
    
    
