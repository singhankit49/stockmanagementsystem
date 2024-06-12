import pymysql
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def suppliersavescreen():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Supplier')
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
                
                from_address = "nikkie081297@gmail.com"
                to_address = ee.get()
    
                # Create message container - the correct MIME type is multipart/alternative.
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "WELCOME TO NIKITA'S STORE"
                msg['From'] = from_address
                msg['To'] = to_address
    
                # Create the message (HTML).
                html ="Hi "+str(bb.get())+",<br><br>Thanks for joining our venture and becoming a part of Nikita's Store<br><br>Thanks & Regards,<br>Team Nikita's Store"
    
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
                
                messagebox.showinfo('Hi','Data Saved & Mail Send')
                
                aa.delete(0,100)
                bb.delete(0,100)
                cc.delete(0,100)
                dd.delete(0,100)
                ee.delete(0,100)
    def close():
        t.destroy()
    
    a1=Label(t,text='SUPPLIER- SAVE SCREEN',font=('times new roman bold',18))
    a1.place(x=250,y=25)    
    a=Label(t,text='SUPPLIER ID',font=('times new roman bold',13))
    a.place(x=100,y=100)
    aa=Entry(t,width=30,font=('times new roman',12))
    aa.place(x=275,y=100)
    btf=Button(t,text='CHECK',font=('times new roman bold',11),bg='orange',command=checkdata)
    btf.place(x=540,y=100)
    b=Label(t,text='SUPPLIER NAME',font=('times new roman bold',13))
    b.place(x=100,y=150)
    bb=Entry(t,width=30,font=('times new roman',12))
    bb.place(x=275,y=150)
    c=Label(t,text='ADDRESS',font=('times new roman bold',13))
    c.place(x=100,y=200)
    cc=Entry(t,width=30,font=('times new roman',12))
    cc.place(x=275,y=200)
    d=Label(t,text='PHONE NO.',font=('times new roman bold',13))
    d.place(x=100,y=250)
    dd=Entry(t,width=30,font=('times new roman',12))
    dd.place(x=275,y=250)
    e=Label(t,text='EMAIL',font=('times new roman bold',13))
    e.place(x=100,y=300)
    ee=Entry(t,width=30,font=('times new roman',12))
    ee.place(x=275,y=300)
    
    
    h=Button(t,text='SAVE',font=('times new roman bold',11),fg='white',bg='green',command=savedata)
    h.place(x=305,y=400)
    j=Button(t,text='CLOSE',font=('times new roman bold',11),fg='white',bg='purple',command=close)
    j.place(x=385,y=400)
    t.mainloop()