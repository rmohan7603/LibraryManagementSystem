#importing libraries
import tkinter as tk
import mysql.connector as sql
import imageio
from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import pyttsx3 as py
import vlc
import datetime 
engine=py.init()
hi = sql.connect(host="localhost", user="root", passwd="101817",database="Library_Management")
a=1
q=0
q1=0
q12=0
q127=0
ak=0
ga=0
er=0
es=0
se=0
se1=0
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#Page to choose Admin or user
ty=0
def acsspage():
    if ty==0:
        root.destroy()
    elif ty==1:
        sl001.destroy()
    elif ty==2:
        rmb1.destroy()
    elif ty==3:
        abo143.destroy()
    elif ty==4:
        swin8.destroy()
    elif ty==5:
        swin9.destroy()
    elif ty==6:
        abo2413.destroy()
    global mainwin5
    mainwin5=Tk()
    mainwin5.iconbitmap(r'D:\CS\Media\library.ico')
    mainwin5.title("Library Management")
    image1=Image.open(r'D:\CS\Media\library5.jpg')
    photo1=ImageTk.PhotoImage(image1)
    background_label=Label(mainwin5,image=photo1)
    engine.setProperty('rate',155)
    engine.setProperty('voice',voices[1].id)
    engine.say('Select your choice')
    engine.runAndWait()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    image=Image.open(r'D:\CS\Media\admin12345.png')
    photo=ImageTk.PhotoImage(image)
    image3=Image.open(r'D:\CS\Media\user12345.png')
    photo3=ImageTk.PhotoImage(image3)
    Label(mainwin5, text=" ADMIN ", fg='blue',font=("Times New Roman", 25, 'bold')).place(x=1065,y=735)
    l1 = Button(mainwin5, text="Admin", bg='light blue',image=photo, fg='white', font=("Times New Roman", 25, 'bold'),command=adlo).place(x=1065, y=585, relwidth=0.08, relheight=0.15)
    Label(mainwin5, text=" USER ", fg='blue',font=("Times New Roman", 25, 'bold')).place(x=475,y=735)
    b1 = Button(mainwin5, text="User", bg='light blue',image=photo3, fg='white', font=("Times New Roman", 19, 'bold'),command=abo43)
    b1.place(x=465, y=585, relwidth=0.08, relheight=0.15)
    mainwin5.geometry('1730x920+100+50')
    mainwin5.mainloop()
#user page
s2=0
def abo43():
    if s2==0:
        mainwin5.destroy()
    elif s2==1:
        abo2413a.destroy()
    elif s2==2:
        sl00.destroy()
    elif s2==3:
        abo13.destroy()
    global abo143
    abo143=Tk()
    abo143.iconbitmap(r'D:\CS\Media\library.ico')
    abo143.title("Library Management")
    image=Image.open(r'D:\CS\Media\studentteacher12345.png')
    photo=ImageTk.PhotoImage(image)
    image3=Image.open(r'D:\CS\Media\guest12345.png')
    photo3=ImageTk.PhotoImage(image3)
    Label(abo143, text=" GUEST ", fg='red',font=("Times New Roman", 15, 'bold')).place(x=395,y=285)
    p1 = Button(abo143,bg='light blue',image=photo, fg='white', font=("Times New Roman", 25, 'bold'),command=first).place(x=55, y=125, relwidth=0.25, relheight=0.30)
    Label(abo143, text=" STUDENT\TEACHER ", fg='Red',font=("Times New Roman", 15, 'bold')).place(x=20,y=285)
    p1 = Button(abo143,bg='light blue',image=photo3, fg='white', font=("Times New Roman", 19, 'bold'),command=guest)
    p1.place(x=365, y=125, relwidth=0.25, relheight=0.30)
    Button(abo143, text="Main Page", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=qw1w331).place(x=220, y=400)
    abo143.geometry('550x500+600+250')
    abo143.mainloop()
def qw1w331():
    global ty
    ty=3
    acsspage()
def first():
    global user
    global abo13
    global kr 
    global ks
    abo143.destroy()
    abo13=Tk()
    kr=StringVar()
    ks=StringVar()
    user=StringVar()
    abo13.iconbitmap(r'D:\CS\Media\library.ico')
    abo13.title("Library Management")
    engine.say("Login to continue")
    engine.runAndWait()
    l1 = Label(abo13, text="User Login", bg='black', fg='white', font=("Times New Roman", 25, 'bold'))
    l1.place(x=0, y=0,relwidth=1,relheight=0.1)
    Label(abo13, text="Enter your designation", fg='blue', font=("Times New Roman", 25, 'bold')).pack(pady=80)
    tcat2 = ttk.Combobox(abo13,width=45,textvariable=user,font=("Times New Roman",15,'bold'))
    tcat2['values']=("Student","Teacher")
    tcat2.pack(padx=10)
    Label(abo13, text="Enter your id", fg='blue', font=("Times New Roman", 25, 'bold')).pack()
    tname23 = Entry(abo13, textvariable=kr,font=("Times New Roman", 15, 'bold'))
    tname23.pack(pady=15)
    Label(abo13, text="Enter your Name", fg='blue', font=("Times New Roman", 25, 'bold')).pack()
    tname24 = Entry(abo13, textvariable=ks,font=("Times New Roman", 15, 'bold'))
    tname24.pack(pady=15)
    Button(abo13,text="Continue", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=stubo
                ).pack(padx=55,pady=10)
    Button(abo13, text="Leave page", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
                command=qw1w231).pack(padx=20, pady=30)
    global q23
    q23=0
    global name1
    name1='a'
    abo13.geometry('550x650')
    abo13.mainloop()
zx=0
w2=0
def qw1w231():
    global s2
    s2=3
    abo43()
def stubo():#library menu
    global az
    global az1
    az=0
    az1=0 
    global abo2413
    
    if user.get()=="Teacher":
        cursor = hi.cursor("create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
        cursor.execute("select Tid,Name from teacher")
    elif user.get()=="Student":  
        cursor = hi.cursor("create table student(studid integer(4) primary key, Name varchar(20),class varchar(4),sec varchar(1)) if not exists")
        cursor.execute("select studid,Name from student")  
    else:
        engine.say('Please choose valid designation')
        engine.runAndWait()
    z=[]
    zx=0
    if user.get()=="Teacher" or user.get()=="Student":
        for i in cursor.fetchall():
            z.append(i)
        for i in z:
            if kr.get().isalpha():
                az1=0
                az=1
                break
            if str(i[0])==kr.get() and i[1].lower()==ks.get().lower():
                zx=1
                if w2==0:
                    abo13.destroy()
                elif w2==1:
                    abo2413a.destroy()
                elif w2==2:
                    rmb.destroy()
                elif w2==3:
                    bd.destroy()
                elif w2==4:
                    sl003.destroy()                
                abo2413=Tk()
                abo2413.iconbitmap(r'D:\CS\Media\library.ico')
                abo2413.title("Library Management")
                if user.get()=="Teacher":
                    Button(abo2413,text="Lend Book", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=instru).pack(pady=10)
                    Button(abo2413,text="Return Book", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=lambda:view_bk1(1)).pack(pady=15)
                    Button(abo2413,  text="Extend Return Date", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=lambda:view_bk1(2)).pack(pady=15)
                elif user.get()=='Student':
                    Button(abo2413,text="Return Book", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=ret_book).pack(pady=15)
                    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
                    cursor.execute("select sname from lend")
                    lu=[]
                    for i in cursor.fetchall():
                        lu.append(i)
                    print(lu,ks.get())
                    if ks.get() in lu[0]:
                        cursor.execute("select return_date,curdate() from lend where sname='{}'".format(ks.get()))
                        for i  in cursor.fetchall():
                            daty=str(i[0])
                            daty1=str(i[1])
                        if daty<daty1:
                            engine.say('Due date exceeded Please contact the admin')
                            engine.runAndWait()
                        else:
                            Button(abo2413,text="Lend Book", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=instru).pack(pady=10)
                            Button(abo2413,  text="Extend Return Date", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=ext_ret).pack(pady=15)
                    else:
                        Button(abo2413,text="Lend Book", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=instru).pack(pady=10)
                        Button(abo2413,  text="Extend Return Date", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=ext_ret).pack(pady=15)
                Button(abo2413, text="Logout", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=lkjout).pack(padx=20, pady=30)
                abo2413.geometry('400x350')
                abo2413.mainloop()
                break
        else:
            az=0
            az1=1
        if zx==0:
            if az==0:
                engine.say("User does not exist ")
                engine.runAndWait()
                user.set('Select')
                kr.set(0000)
                ks.set('abcd')       
            if az1==0:
                engine.say("Please enter only numeric value in id field")
                engine.runAndWait()
                kr.set(0000)
def lkjout():
    global ty
    ty=6
    global s2
    s2=0
    global w2
    w2=0
    acsspage()
def ext_ret():
    global bd
    global h1
    h1=0
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    ins = "select * from lend"
    cursor.execute(ins)
    if mk==0:
        abo2413.destroy()
    elif mk==1:
        sl003.destroy()
    bd = Tk()
    bd.iconbitmap(r'D:\CS\Media\library.ico')
    bd.title("Library Management")
    if user.get()=='Student':
        for i in cursor.fetchall():
            if i[0]==int(kr.get()):         
                l1 = Label(bd, text="Are you willing to use the book for few more days ", fg='blue',
                        font=("Times New Roman", 20, 'bold'))
                l1.pack(pady=5)
                l3=Label(bd, text=str(i[2])+' '+str(i[3]), fg='blue',
                        font=("Times New Roman", 20, 'bold')).pack(pady=5)
                l2 = Label(bd, text='If yes , confirm by pressing the button', fg='blue',
                        font=("Times New Roman", 14, 'bold'))
                l2.pack(padx=20,pady=5)
                bd.geometry('300x250')
                b0 = Button(bd, text="Extend ", width=10, height=1, bg="blue", fg="white", command=extreturn).pack()
                quitbut = Button(bd, text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'),
                                command=bd.quit).pack(padx=46, pady=20)
                h1+=1
    elif user.get()=='Teacher':
        for i in cursor.fetchall():
            if i[0]==int(kr.get()) and i[2]==state1:
                        
                l1 = Label(bd, text="Are you willing to use the book for few more days ", fg='blue',
                        font=("Times New Roman", 20, 'bold'))
                l1.pack(pady=5)
                l3=Label(bd, text=str(i[2])+' '+str(i[3]), fg='blue',
                        font=("Times New Roman", 20, 'bold')).pack(pady=5)
                l2 = Label(bd, text='If yes , confirm by pressing the button', fg='blue',
                        font=("Times New Roman", 14, 'bold'))
                l2.pack(padx=20,pady=5)
                bd.geometry('300x250')
                b0 = Button(bd, text="Extend ", width=10, height=1, bg="blue", fg="white", command=extreturn).pack()
                quitbut = Button(bd, text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'),
                                command=bd.quit).pack(padx=46, pady=20)
                h1+=1
    if h1==0:
        Label(bd, text="You have not borrowed any book ", bg='brown', fg='white',
              font=("Times New Roman", 20, 'bold')).pack()
        Label(bd, text="Press here to Lend a book", bg='orange', fg='white',
              font=("Times New Roman", 20, 'bold')).pack()
        Button(bd, text="Lend book ", width=10, height=1, bg="pink", fg="white", command=golen).pack()
    Button(bd, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
           command=qw311).pack(padx=20, pady=30)
    global m11
    m11=1
    bd.geometry('650x400')
    bd.mainloop()   
def golen():
    global ak
    ak = 1
    instru()
def extreturn():
    global m11
    if m11==1:
        m11=2
        cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
        if user.get()=='Student':
            ins = "update lend set return_date=date_add(return_date,interval 7 day) where sid='{}'".format(int(kr.get()))
        elif user.get()=='Teacher':
            ins = "update lend set return_date=date_add(return_date,interval 7 day) where sid='{}' and bname='{}'".format(int(kr.get()),state1)
        cursor.execute(ins)
        hi.commit()
        if user.get()=='Student':
            cursor.execute("select return_date from lend where sid='{}'".format(kr.get()))
        elif user.get()=='Teacher':
            cursor.execute("select return_date from lend where sid='{}' and bname='{}'".format(kr.get(),state1))
        z4 = cursor.fetchone()
        z5 = str(z4[0])[8:] + '-' + str(z4[0])[5:7] + '-' + str(z4[0])[0:4]
        Label(bd, text="Return within {} ".format(z5), bg='orange', fg='white',
            font=("Times New Roman", 19, 'bold')).pack(pady=20)   
qa=0          
def instru():
    global abo2413a1
    global sq
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    global sq
    cursor.execute("select sname,count(sname) from lend where sid={}".format(int(kr.get())))
    sq=cursor.fetchone()
    if sq==None:
        sq='aqwedsss'
    if ak==1:
        bd.destroy()
    elif ak==2:
        rmb.destroy() 
    global qa
    qa=sq[1]   
    if sq[0]==ks.get() and user.get()=='Student':
        engine.say('You have already borrowed a book. If you wish to lend another book, please return the book you have borrowed to the library.')
        engine.runAndWait()
    elif  sq[1]>=5 and user.get()=='Teacher':
        engine.say('You have already borrowed the maximum number of books. If you wish to lend another book, please return the book you have borrowed to the library.')
        engine.runAndWait()
    else:
        if ak==0:
            abo2413.destroy()
        if sq[0]==ks.get() and user.get()=='Teacher':
            engine.say('You have already borrowed one/more books. You can choose upto five books.')
            engine.runAndWait()
        abo2413a1=Tk()
        l1 = Label(abo2413a1, text="Instructions", bg='Green', fg='white', font=("Times New Roman", 25, 'bold'))
        l1.place(x=0, y=0,relwidth=1,relheight=0.1)
        if user.get()=="Teacher":
            Label(abo2413a1, text="###> As a teacher, You will have the privilege to select upto 5 books.", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=60)
        elif user.get()=="Student":
            Label(abo2413a1, text="###> As a student, You will have the privilege to select only one book from the available catagories.", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=60)
        Label(abo2413a1, text="###>You can use the drop-down menu to filter the books according to their category", fg='blue', font=("Times New Roman", 16, 'bold')).pack()
        Label(abo2413a1, text="###>If you choose a book to lend, click the radio-button next to it and press continue", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=6)
        Label(abo2413a1, text="###>Please handle the book with care.", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=6)
        Label(abo2413a1, text="###> Any damage to the book woud not be appreciated and would invite a penalty", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=6)
        Label(abo2413a1, text="###>Please return the book on or before the specified date", fg='blue', font=("Times New Roman", 16, 'bold')).pack(pady=6)
        abo2413a1.iconbitmap(r'D:\CS\Media\library.ico')
        Button(abo2413a1,text="Proceed", bg='orange', fg='white', font=("Times New Roman", 19, 'bold'),command=cat).pack(padx=55,pady=15)
        abo2413a1.title("Library Management")
        abo2413a1.geometry('900x450')
        abo2413a1.mainloop()
mk=0   
def ret_book():
    if mk==0:
        abo2413.destroy()
    elif mk==1:
        sl003.destroy()
    global rmb
    global p1
    p1 = 0
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    ins = "select * from lend"
    cursor.execute(ins)
    rmb=Tk()
    rmb.iconbitmap(r'D:\CS\Media\library.ico')
    rmb.title("Library Management")
    if user.get()=='Student':
        for i in cursor.fetchall():
            if i[0]==int(kr.get()):
                m=str(i[2]+i[3])
                l1 = Label(rmb, text="Are you sure you want to return your book", bg="black", fg="white")
                l1.pack()
                Label(rmb, text=m, bg="black", fg="white").pack()
                b0 = Button(rmb, text="Yes, Return ", width=10, height=1, bg="blue", fg="white", command=ret_suc)
                b0.pack()
                p1=1
    elif user.get()=='Teacher':
        for i in cursor.fetchall():
            if i[0]==int(kr.get()) and i[2]==state1:
                m=str(i[2]+i[3])
                l1 = Label(rmb, text="Are you sure you want to return your book", bg="black", fg="white")
                l1.pack()
                Label(rmb, text=m, bg="black", fg="white").pack()
                b0 = Button(rmb, text="Yes, Return ", width=10, height=1, bg="blue", fg="white", command=ret_suc)
                b0.pack()
                p1=1
    if p1==0:
        Label(rmb, text="You have not borrowed any book ", bg='brown', fg='white',
              font=("Times New Roman", 20, 'bold')).pack()
        Label(rmb, text="Press here to Lend a book", bg='orange', fg='white',
              font=("Times New Roman", 20, 'bold')).pack()
        Button(rmb, text="Lend book ", width=10, height=1, bg="pink", fg="white", command=golen1).pack()
    Button(rmb, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
           command=qw121).pack(padx=20, pady=30)
    rmb.geometry("300x250")
    rmb.mainloop()
def golen1():
    global ak
    ak = 2
    instru()
def ret_suc():
    global rmb1
    jka= hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    if user.get()=='Student':
        ins = "delete from lend where sid='{}'".format(int(kr.get()))
    elif user.get()=='Teacher':
        ins = "delete from lend where sid='{}' and bname='{}'".format(int(kr.get()),state1)  
    jka.execute(ins)
    hi.commit()
    rmb.destroy()
    rmb1=Tk()
    Label(rmb1, text="Please return the book to the library", bg="black", fg="white").pack()
    quitbut = Button(rmb1, text="Logout", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'),command=u31).pack(padx=46, pady=20)
    rmb1.geometry('300x250')
    rmb1.mainloop()
len3=0
len2=0
pageno=0
pd={}
name1=''
def u31():
    global ty
    ty=2
    global w2
    w2=0
    global s2
    s2=0
    global ak
    ak=0
    acsspage()
def cat():
    if name1=='guest':
        if q23==0:
            abo143.destroy()
        if q23==1:
            sl00.destroy()
        
    if name1!='guest':
        if q23==0:
            abo2413a1.destroy()
        if q23==1:
            sl00.destroy()
        if q23==2:
            sl001.destroy()
    global abo2413a
    global wsa 
    abo2413a=Tk()
    wsa=StringVar()
    abo2413a.iconbitmap(r'D:\CS\Media\library.ico')
    abo2413a.title("Library Management")
    l1 = Label(abo2413a, text="Select Book Category", bg='Green', fg='white', font=("Times New Roman", 25, 'bold'))
    l1.place(x=0, y=0,relwidth=1,relheight=0.1)
    tcat2 = ttk.Combobox(abo2413a,width=45,textvariable=wsa,font=("Times New Roman",15,'bold'))
    tcat2['values']=("fantasy","adventure","horror","fiction","scientific","reference")
    tcat2.pack(padx=60,pady=85)
    q=['Select','View']
    if name1=='guest':
        u=q[1]
        Button(abo2413a, text="Leave page", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=qw1w1).pack(padx=20, pady=30)
    else:
        u=q[0]
        Button(abo2413a, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=qw11).pack(padx=20, pady=30)
    Button(abo2413a,text="{} books".format(u), bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=view_bk).pack(padx=55,pady=25)
    abo2413a.geometry('600x650')
    abo2413a.mainloop()
def qw1w1():
    global s2
    s2=1
    if name1=='guest':
        global q23
        q23=0
        global e3
        e3=0
    abo43()
def qw11():
    global w2
    w2=1
    if name1!='guest':
        global q23
        q23=0
        global ak
        ak=0
        global e3
        e3=0
    stubo()
def qw121():
    global w2
    w2=2
    if name1!='guest':
        global ak
        ak=0
        global e3
        e3=0
    stubo()
def qw311():
    global w2
    w2=3
    stubo()
def guest():
    engine.say("As a guest you are allowed to see the various books in the library")
    engine.runAndWait()
    global name1
    name1='guest'
    cat()
e3=0
def view_bk():
    global sl00
    global var1
    global var2
    global var3
    global var4
    global var5
    #if name1!='guest':
    if e3==0:
        abo2413a.destroy()
    elif e3==1:
        sl001.destroy()
    sl00=Tk()
    sl00.iconbitmap(r'D:\CS\Media\library.ico')
    sl00.title("Library Management")
    cursor = hi.cursor("create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
    cursor.execute("select bid,bname,author,pub from books where category='{}'".format(wsa.get()))
    global z11
    z11=cursor.fetchall()
    global len3
    global len2
    global pageno
    len3=len(z11)
    if len3%7==0:
        print('hi')
    else:
        if len3>7:
            len2=int(len3%7)
    if len3>7:
        pageno=2
        if len3>14:
            pageno=int((len3-len2)/7)
    else:
        pageno=1
    global pd
    a9=0;b9=7
    for i in range(1,pageno+1):
        pd[i]=[a9,b9]
        a9=b9
        b9+=7
    if len3>14:
        if pageno>1:
            pd[pageno+1]=[len3-len2,len3+1]
    global bn
    global bi
    bn=[]
    bi=[]
    global dk
    dk={}
    global cj
    cj=1
    z=1
    global buttons
    buttons=[]
    global l
    h=0
    global h1
    global g1
    if q2==0:
        h1=0
        g1=7
    hello()
    #Button(sl00,text="Reset selection",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=reset1).place(x=350, y=515)
    #Button(sl00,text="Return to Main menu",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret_tea1).place(x=430, y=515)
    sl00.geometry('640x600')
    sl00.mainloop()
h=0
zy=0
buttons=[]
text=''
q2=0
h1=0
g1=0
pgno=0
f12=0
def hello():
    global z13
    global oz
    l11 = Label(sl00,text=" Books", bg='brown', fg='white', font=("Times New Roman", 25, 'bold')).place(x=0, y=0,relwidth=1,relheight=0.08)
    l1 = Label(sl00, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=45,relwidth=1,relheight=0.004)
    l2 = Label(sl00, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=105, relwidth=1, relheight=0.004)
    l3 = Label(sl00, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=170, y=1, relwidth=0.004, relheight=1)
    l4 = Label(sl00, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=0, y=1,relwidth=0.004, relheight=1)
    l5 = Label(sl00, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=390, y=1, relwidth=0.004, relheight=1)
    Label(sl00,text="Book Name", fg='green',bg ="white", font=("Times New Roman",19, 'bold')).place(x=15, y=55)
    Label(sl00,text="Book author", fg='green',bg ="white", font=("Times New Roman", 25, 'bold')).place(x=200, y=55)
    if name1=='guest':
        Label(sl00,text="Publication", fg='green',bg ="white", font=("Times New Roman", 25, 'bold')).place(x=450, y=55)
    if name1!='guest':
        Label(sl00,text="Select", fg='green',bg ="white", font=("Times New Roman", 25, 'bold')).place(x=450, y=55)
        Button(sl00,text="Continue",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=cont).place(x=350, y=415)
    a=55;b=125
    a=55;b=125
    oz=0
    global pgno
    if h==0:
        pgno=1
    try:
        h1=pd[pgno][0]
        g1=pd[pgno][1]
    except:
        engine.say('No more books available')
        engine.runAndWait()
    if len3>14:
        if pgno==pageno+1 :
            Button(sl00,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back1).place(x=250, y=470)
        elif pgno==1 and pd.get(2)!=None:
            Button(sl00,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next1).place(x=450, y=470)
        elif pgno>1:
            Button(sl00,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next1).place(x=450, y=470)
            Button(sl00,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back1).place(x=250, y=470)
    else:
        if pgno==2:
            Button(sl00,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back1).place(x=250, y=470)
        elif pgno==1 and pd.get(2)!=None:
            Button(sl00,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next1).place(x=450, y=470)
        elif pgno>1:
            Button(sl00,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next1).place(x=450, y=470)
            Button(sl00,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back1).place(x=250, y=470)
    global jh
    global buttons
    jh=StringVar()   
    for i in z11[h1:g1]:
        Label(sl00,text=i[1],bg ="white",font=("Times New Roman", 20, 'bold')).place(x=a,y=b)
        Label(sl00,text=i[2],bg ="white",font=("Times New Roman", 20, 'bold')).place(x=a+165,y=b)
        if name1=='guest':
            Label(sl00,text=i[3],bg ="white",font=("Times New Roman", 20, 'bold')).place(x=a+365,y=b)
        bn.append(i[1])
        bi.append(i[0])
        #dk[i[0]]=IntVar()
        #rd=Radiobutton(sl00,bg ="white",value=i,command=lambda i=i:onpress(i)).place(x=a+450,y=b)
        #buttons.append(rd)            
        oz+=1        
        b+=50
    az=[]
    for i in z11[h1:g1]:
        az.append(i[0])
    b=125
    Button(sl00, text="Other categories", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=q11).place(x=450,y=450)
    if name1=='guest':
        if f12==0:
            Button(sl00, text="Leave page", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
                        command=qw1w23).pack(padx=20, pady=30)
    else:
        if f12==0:
            Button(sl00, text="Leave page", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
                        command=qw1w23).pack(padx=20, pady=30)
    if name1!='guest':
        for i in az:
            rd=Radiobutton(sl00,bg ="white",value=i,command=(lambda i=i:onpress(i))).place(x=a+450,y=b)
            buttons.append(rd)
            b+=50
        b+=50
state=0
q23=0
#now doing teacher return and ext return 
#again use lambda in login to check if teacher or student
def view_bk1(args):
    global sl003
    abo2413.destroy()
    sl003=Tk()
    global mk
    if args==1:
        mk=1
        Button(sl003,text="Return",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret_book).place(x=350, y=415)
    elif args==2:
        mk=1
        Button(sl003,text="Extend",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ext_ret).place(x=350, y=415)
    sl003.iconbitmap(r'D:\CS\Media\library.ico')
    sl003.title("Library Management")
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    cursor.execute("select sid,bname,author from lend where sid='{}'".format(kr.get()))
    global z11
    z11=cursor.fetchall()
    l11 = Label(sl003,text=" Books Borrowed", bg='brown', fg='white', font=("Times New Roman", 25, 'bold')).place(x=0, y=0,relwidth=1,relheight=0.08)
    l1 = Label(sl003, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=45,relwidth=1,relheight=0.004)
    l2 = Label(sl003, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=105, relwidth=1, relheight=0.004)
    l3 = Label(sl003, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=170, y=1, relwidth=0.004, relheight=1)
    l4 = Label(sl003, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=0, y=1,relwidth=0.004, relheight=1)
    l5 = Label(sl003, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=390, y=1, relwidth=0.004, relheight=1)
    Label(sl003,text="Book Name", fg='green',bg ="white", font=("Times New Roman",19, 'bold')).place(x=15, y=55)
    Label(sl003,text="Book author", fg='green',bg ="white", font=("Times New Roman", 25, 'bold')).place(x=200, y=55)
    Label(sl003,text="Select", fg='green',bg ="white", font=("Times New Roman", 25, 'bold')).place(x=450, y=55)
    Button(sl003,text="Back ",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=bck).place(x=250, y=415)
    a=55;b=125
    for i in z11:
        Label(sl003,text=i[1],bg ="white",font=("Times New Roman", 20, 'bold')).place(x=a,y=b)
        Label(sl003,text=i[2],bg ="white",font=("Times New Roman", 20, 'bold')).place(x=a+165,y=b)
        b+=50
    b=125
    global op
    for i in z11:
        op.append(i[1])
    for i in op:
        Radiobutton(sl003,bg ="white",value=i,command=(lambda i=i:onpress1(i))).place(x=a+450,y=b)
        b+=50
    op=[]
    sl003.geometry('640x600')
    sl003.mainloop()
op=[]
state1=0
def bck():
    global w2
    w2=4
    stubo()
def onpress1(i):#to get book name
    global state1
    state1 = i
def qw1w23():
    global s2
    s2=2
    global q23
    q23=0
    global w2
    w2=0
    abo43()
def q11():
    global q23
    q23=1
    global e3
    e3=0
    cat()
dw=0
def onpress(i):
    global dw
    global state
    state = i
    if user.get()=="Teacher" and (dw in lp):
        engine.say('You have already borrowed the same book')
        engine.runAndWait()
    else:
        hud()
    state = i
    print(state)
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    cursor.execute("select bname from books where bid='{}'".format(state))
    lop=cursor.fetchone()
    dw=lop[0]
def cont():
    cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
    cursor.execute("select bname from lend where sid='{}'".format(int(kr.get())))
    lko=cursor.fetchall()
    lp=[]
    for k in lko:
        lp.append(k[0])
def hud():
    global sl001
    sl00.destroy()
    sl001=Tk()
    sl001.iconbitmap(r'D:\CS\Media\library.ico')
    sl001.title("Library Management")
    Label(sl001,text="Are you sure to borrow this book", bg='brown', fg='white', font=("Times New Roman", 25, 'bold')).place(x=0, y=0,relwidth=1,relheight=0.08)
    print(state)
    cursor = hi.cursor("create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
    cursor.execute("select bid,bname,author from books where bid='{}'".format(int(state)))
    for i in cursor.fetchall():
        print(i)
        z=i
    Label(sl001,text=str(z),font=("Times New Roman", 20, 'bold')).pack(padx=20,pady=70)
    Button(sl001,text="Lend",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=brw).pack(pady=20)
    global df
    if user.get()=='Student':
        df=Button(sl001, text="Select a different book", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
                command=w11)
        df.pack(padx=20, pady=30)
    elif user.get()=='Teacher' and qa<5:
        dr=Button(sl001, text="If you want lend another", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
                command=et11)
        dr.pack(padx=20, pady=30)  
    global m
    m=1
    sl001.geometry('300x350')
    sl001.mainloop()
def w11():
    global e3
    e3=1
    view_bk()
def et11():
    if qa>=5:
        engine.say("You have borrowed the maximum number of books please return the books to borrow more")
        engine.runAndWait()
    else:
        global q23
        q23=2
        global e3
        e3=0
        cat()
def brw():
    if user.get()=='Student':
        df.pack_forget()
    global m
    global qa
    if m==1:
        m=2
        cursor = hi.cursor(
            "create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
        cursor.execute("select bname,author from books where bid='{}'".format(int(state)))
        sq=cursor.fetchone()
        bn=sq[0]
        ab=sq[1]
        if user.get()=="Teacher":
            ins1="select Name from teacher where Tid='{}'".format(int(kr.get()))
            qa+=1
        elif user.get()=="Student":
            
            ins1="select name from student where studid='{}'".format(int(kr.get()))
        cursor.execute(ins1)
        z=cursor.fetchone()
        z1=z[0]
        ins = "insert into lend values({},'{}','{}','{}',curdate(),date_add(curdate(),interval 7 day))".format(int(kr.get()),z1,bn,ab)
        cursor.execute(ins)
        hi.commit()
        ins = "update books set qty=qty-1 where bname='{}'".format(bn)
        cursor.execute(ins)
        hi.commit()
        if user.get()=="Teacher":
            cursor.execute("select return_date,count(sname) from lend where sid='{}'".format(int(kr.get())))
        elif user.get()=="Student":
            cursor.execute("select return_date from lend where sid='{}'".format(int(kr.get())))
        z4=cursor.fetchone()
        z5=str(z4[0])[8:]+'-'+str(z4[0])[5:7]+'-'+str(z4[0])[0:4]
        Label(sl001,text="Return within {} ".format(z5), bg='pink', fg='white',
          font=("Times New Roman", 19, 'bold')).pack(pady=20)
        Button(sl001, text="Logout", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=pkl).pack(padx=20, pady=30)
def pkl():
    global ty 
    ty=1
    global w2
    w2=0
    global s2
    s2=0
    global ak
    ak=0
    acsspage()
def next1():
    global f12
    f12=1
    global h
    h=1
    global pgno
    pgno=pgno+1  
    global q2
    q2=1
    lst=sl00.place_slaves()
    for i in lst:
        i.destroy() 
    hello()
def back1():
    global f12
    f12=1
    global h
    h=1
    global pgno
    pgno=pgno-1  
    global q2
    q2=1
    lst=sl00.place_slaves()
    for i in lst:
        i.destroy()
    hello()
#admin login
def adlo():
    global swin8
    global usy
    global psy
    mainwin5.destroy()
    swin8=Tk()
    usy = StringVar()
    psy = StringVar()
    swin8.iconbitmap(r'D:\CS\Media\library.ico')
    swin8.title("Library Management")
    engine.say('Please enter your id and password to continue')
    engine.runAndWait()
    l1 = Label(swin8, text="Admin login", bg='black', fg='white', font=("Times New Roman", 25, 'bold'))
    l1.place(x=0, y=0,relwidth=1,relheight=0.1)
    user = Label(swin8, text="Enter your ID", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'))
    user.grid(row=1,column=0,pady=50,padx=20)
    user1 = tk.Entry(swin8, textvariable=usy)
    user1.grid(row=1, column=1, pady=50, padx=10)
    usy.set("Enter ID")
    pwd = Label(swin8, text="Enter your password", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'))
    pwd.grid(row=2,column=0,padx=20,pady=5)
    pwd1 = tk.Entry(swin8, textvariable=psy,show='*')
    pwd1.grid(row=2, column=1, pady=20, padx=10)
    psy.set("Enter")
    quitbut1 = Button(swin8, text="Quit", bg='orange', fg='white', font=("Times New Roman", 20, 'bold'),command=swin8.quit)
    quitbut1.place(x=241, y=190, relwidth=0.2, relheight=0.1)
    logs = Button(swin8, text="Enter", bg='green', fg='white', font=("Times New Roman", 20, 'bold'),command=checkad)
    logs.place(x=141, y=190, relwidth=0.2, relheight=0.1)
    Button(swin8,text="Previous page", bg='orange', fg='white', font=("Times New Roman", 19, 'bold'),command=qs1w331).place(x=201, y=260, relwidth=0.4, relheight=0.1)
    swin8.geometry('450x450')
def qs1w331():
    global ty
    ty=4
    acsspage()
def checkad():#Admin check
    v=12
    global kuy
    kuy=0
    cursor = hi.cursor("create table admin(id int(4),name varchar(20),pwd varchar(10)) if not exists")
    cursor.execute("select id,pwd from admin")
    a1 = usy.get()
    b1 = psy.get()
    for i in cursor.fetchall():
        if a1.isalpha():
            v=0
            break
        if i[0] == int(a1) and i[1] == b1:
            adinter()
            kuy+=1
    if v ==0:
        engine.say("Please enter only numeric value in id field")
        engine.runAndWait()
        usy.set(0000)
    elif kuy==0:
        incrt_adm()
def incrt_adm():
    global inc0
    inc0 = Tk()
    inc0.iconbitmap(r'D:\CS\Media\library.ico')
    inc0.title("Library Management")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',145)
    engine.say('Sorry Login Information is incorrect retry to continue')
    engine.runAndWait()
    e1=Label(inc0,text="Incorrect Login info",bg='orange', fg='white',font=("Times New Roman", 15, 'bold'))
    e1.pack()
    e2=Label(inc0,text="If you want to retry press here", bg='green', fg='yellow', font=("Times New Roman", 15, 'bold'))
    e2.pack(padx=30,pady=20)
    b0=Button(inc0,text="Retry", bg='green', fg='white', font=("Times New Roman", 20, 'bold'),command=ret_adm2)
    b0.pack(padx=20,pady=40)
    inc0.geometry('350x250')
    inc0.mainloop()
def ret_adm2():
    inc0.destroy()
    usy.set('Enter your name')
    psy.set('Password')
def adinter():
    global vid
    global swin9
    if ga==0:
        swin8.destroy()
        '''engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 145)
        engine.say('A good day is a good day A bad day is a good story')
        engine.runAndWait()
        engine.say('It\'s nice to meet you again')
        engine.runAndWait()'''
    elif ga==1:
        tm1.destroy()
    elif ga==2:
        tm19.destroy()
    elif ga==3:
        abo1.destroy()
    swin9=Tk()
    swin9.iconbitmap(r'D:\CS\Media\library.ico')
    swin9.title("Library Management")
    Button(swin9, text="Books", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'), command=abo).pack(pady=5)
    Button(swin9, text="Teacher", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=teach).pack(pady=5)
    Button(swin9, text="Student", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=studen).pack(pady=5)
    Button(swin9, text="Logout", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=adl).pack(padx=20, pady=30)
    swin9.geometry('450x400')
    swin9.mainloop()
def adl():
    global ty
    ty=5
    global ga 
    ga=0
    acsspage()
def studen():
    global tm1
    global es
    es = 1
    if q12==0:
        swin9.destroy()
    elif q12==1:
        sl.destroy()
    elif q12==2:
        tm.destroy()
    elif q12==4:
        bw2.destroy()
    elif q12==7:
        tm6.destroy()
    elif q12==9:
        sdel.destroy()
    elif q12==23:
        tm6.destroy()
    elif q12==34:
        sl90.destroy()
    elif q12==344:
        sl90.destroy()
    tm1 = Tk()
    tm1.iconbitmap(r'D:\CS\Media\library.ico')
    tm1.title("Library Management")
    b1 = Button(tm1, text="Register student", bg='blue', fg='white',font=("Times New Roman", 19, 'bold'), command=studentr)
    b1.place(x=221, y=55, relwidth=0.4, relheight=0.07)
    b5 = Button(tm1, text="Update student records", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=upd_stu).place(x=221, y=135, relwidth=0.4, relheight=0.07)
    b23= Button(tm1, text="list of students who missed the due date", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=lambda:view_list(3)).place(x=221, y=375, relwidth=0.4, relheight=0.07)
    b6 = Button(tm1, text="list of students borrowed", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=lambda:view_list(2)).place(x=221, y=215, relwidth=0.4, relheight=0.07)
    b7 = Button(tm1, text="Delete student records", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=del_stu).place(x=221, y=295, relwidth=0.4, relheight=0.07)
    #Button(tm19, text="Student who have not returned", bg='orange', fg='white', font=("Times New Roman", 17, 'bold'),
    #       command=lambda:trex(2)).place(
    #    x=505, y=325, relwidth=0.5, relheight=0.1)
    quitbut = Button(tm1, text="Quit", bg='orange', fg='white', font=("Times New Roman", 19, 'bold'),command=tm1.quit).place(x=291, y=455, relwidth=0.2, relheight=0.07)
    Button(tm1, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 18, 'bold'),command=re1).place(x=351, y=475, relwidth=0.4, relheight=0.08)
    tm1.geometry('850x600')
    tm1.mainloop()
def re1():
    global ga
    global q12
    ga=1
    q12=0
    adinter()
def studentr():
    global tm
    global rsna
    global rsid
    global rscl
    global rsse
    global er
    er=3
    tm1.destroy()
    tm=tk.Tk()
    rsna=StringVar()
    rsid=StringVar()
    rscl=StringVar()
    rsse=StringVar()
    tm.iconbitmap(r'D:\CS\Media\library.ico')
    tm.title("Library Management")
    Label(tm, text="Please enter details below", bg="black", fg="white").pack()
    Label(tm, text="Student Id * ").pack()
    tid2=Entry(tm, textvariable=rsid)
    tid2.pack()
    rsid.set('abc')
    tpass1 = Label(tm, text="Name * ")
    tpass1.pack()
    tpass2 = Entry(tm, textvariable=rsna)
    tpass2.pack()
    rsna.set('0000')
    tdep1 = Label(tm, text="Class * ")
    tdep1.pack()
    tdep2 = Entry(tm, textvariable=rscl)
    tdep2.pack()
    rscl.set('000')
    tname1 = Label(tm, text="Section * ")
    tname1.pack()
    tname2 = Entry(tm, textvariable=rsse)
    tname2.pack()
    rsse.set('0000')
    b0 = Button(tm, text="Register", width=10, height=1, bg="blue", fg="white",command=register_stu).pack()
    Button(tm, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=retm1).pack(padx=20,pady=30)
    tm.geometry("600x300")
    tm.mainloop()
def retm1():
    global q12
    q12=2
    studen()
def register_stu():
    tid3=rsid.get()
    tname3=rsna.get()
    tdep3=rscl.get()
    tpass3=rsse.get()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha() and tpass3.isalpha():
        try:
            cursor = hi.cursor("create table student(studid integer(4) primary key, Name varchar(20),class varchar(4),section varchar(1)) if not exists")
            ins = "insert into student values('{}', '{}','{}','{}')".format(int(tid3), tname3, tdep3, tpass3)
            cursor.execute(ins)
            hi.commit()
            messagebox.showinfo(title='Library Management',message='Registered successfully')
        except:
            engine.say('A Student with same id already exists')
            engine.say('Please give a different id')
            rsid.set('abc')
            engine.runAndWait()
    else:
        incrt_ent()
def upd_stu():
    global bw2
    global stid1
    global stna1
    global scla1
    global ssec1
    global er
    er=4
    tm1.destroy()
    bw2 = tk.Tk()
    stid1 = StringVar()
    stna1 = StringVar()
    scla1 = StringVar()
    ssec1 = StringVar()
    bw2.iconbitmap(r'D:\CS\Media\library.ico')
    bw2.title("Library Management")
    Label(bw2, text="Student Id * ").pack()
    tid2 = Entry(bw2, textvariable=stid1)
    tid2.pack()
    stid1.set('abc')
    tpass1 = Label(bw2, text="Student Name * ")
    tpass1.pack()
    tpass2 = Entry(bw2, textvariable=stna1)
    tpass2.pack()
    stna1.set('enter')
    tdep1 = Label(bw2, text="Class * ")
    tdep1.pack()
    tdep2 = Entry(bw2, textvariable=scla1)
    tdep2.pack()
    scla1.set('enter')
    tname1 = Label(bw2, text="Section * ")
    tname1.pack()
    tname2 = Entry(bw2, textvariable=ssec1)
    tname2.pack()
    ssec1.set('enter')
    b0 = Button(bw2, text="Modify", width=10, height=1, bg="blue", fg="white", command=upd_det).pack()
    Button(bw2, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret3).pack(padx=20, pady=20)
    bw2.geometry("600x300")
    bw2.mainloop()
def ret3():
    global q12
    q12=4
    studen()
def upd_det():
    tid3 = stid1.get()
    tname3 = stna1.get()
    tdep3 = scla1.get()
    tpass3 = ssec1.get()
    cursor = hi.cursor("create table student(studid integer(4) primary key, Name varchar(20),class varchar(4),sec varchar(1)) if not exists")
    cursor.execute("select studid,Name,class,sec from student")
    x = cursor.fetchall()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha() and tpass3.isalpha():
        for i in x:
            if i[0]==int(tid3):
                cursor = hi.cursor(
                    "create table student(studid integer(4) , name varchar(20),class varchar(4),sec varchar(1)) if not exists")
                ins = "update student set name='{}',class='{}',sec='{}' where studid={}".format(tname3, tdep3, tpass3,int(tid3))
                cursor.execute(ins)
                hi.commit()
                messagebox.showinfo(title='Library Management',message='Student details updated successfully')
                break
        else:
            engine.say('Student id does not exist')
            engine.say('Please enter a valid student id')
            engine.runAndWait()
            stid1.set('abc')
    else:
        incrt_ent()
def del_stu():
    global tm6
    global sid1
    global sna
    global er
    er=5
    if se==0:
        tm1.destroy()
    tm6 = tk.Tk()
    sna = StringVar()
    sid1 = StringVar()
    Label(tm6, text="Please enter details below", bg="black", fg="white").pack()
    Label(tm6, text="Student Id * ").pack()
    tid2 = Entry(tm6, textvariable=sid1)
    tid2.pack()
    sid1.set('abc')
    b0 = Button(tm6, text="Submit", width=10, height=1, bg="blue", fg="white", command=del_st)
    b0.pack()
    quitbut = Button(tm6,text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'), command=tm6.quit)
    quitbut.pack(padx=46,pady=20)
    Button(tm6, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret_tea11).pack(padx=20,pady=40)
    tm6.geometry("600x300")
    tm6.mainloop()
def ret_tea11():
    global q12
    q12=23
    studen()
def ret9():
    global q1
    q1=7
    abo()
def del_st():
    global j
    global sdel
    tid3 = sid1.get()
    cursor = hi.cursor("create table student(studid integer(4) primary key, Name varchar(20),class varchar(4),sec varchar(1)) if not exists")
    cursor.execute("select studid,Name,class,sec from student")
    x=cursor.fetchall()
    if tid3.isdigit():
        sdel = Tk()
        for iv in x:
            if str(tid3) == str(iv[0]):
                j=tid3
                Label(sdel,text=iv, bg="black", fg="white",font=("Times New Roman", 35, 'bold')).pack(pady=50)
                b0 = Button(sdel, text="Submit", width=10, height=1, bg="blue", fg="white", command=asd)
                b0.pack()
                break
        else:
            Label(sdel, text="Student does not exist", bg='blue', fg='white',
                  font=("Times New Roman", 19, 'bold')).pack()
        Button(sdel, text="Admin-Student menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
               command=rtu).pack(padx=20, pady=40)
    else:
        tm6.destroy()
        incrt_ent()
def asd():
    cursor = hi.cursor("create table student(studid integer(4) primary key, Name varchar(20),class varchar(4),sec varchar(1)) if not exists")
    cursor.execute("select studid from student")
    x = cursor.fetchall()
    for i in x:
        if i[0]==int(j):
            ins = "delete from student where studid='{}'".format(j)
            cursor.execute(ins)
            hi.commit()
            Label(sdel, text="Student removed successfully", bg='blue', fg='white',font=("Times New Roman", 19, 'bold')).pack()
            break
    else:
        Label(sdel, text="Student does not exist", bg='blue', fg='white',
              font=("Times New Roman", 19, 'bold')).pack()
def rtu():
    global q12
    q12=9
    studen()
def teach():
    global tm19
    global es
    es=2
    if q127==0:
        swin9.destroy()
    elif q127==1:
        sl.destroy()
    elif q127==2:
        tm45.destroy()
    elif q127==10:
        bw21.destroy()
    elif q127==7:
        tm6.destroy()
    elif q127==9:
        sdel1.destroy()
    elif q127==21:
        tm62.destroy()
    elif q127==54:
        sl90.destroy()
    tm19 = Tk()
    tm19.iconbitmap(r'D:\CS\Media\library.ico')
    tm19.title("Library Management")
    b1 = Button(tm19, text="Register Teacher", bg='blue', fg='white',font=("Times New Roman", 19, 'bold'), command=teacherr)
    b1.place(x=221, y=55, relwidth=0.4, relheight=0.07)
    b5 = Button(tm19, text="Update Teacher records", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=upd_teach).place(x=221, y=135, relwidth=0.4, relheight=0.07)
    b6 = Button(tm19, text="list of teachers borrowed", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=lambda:view_list(1)).place(x=221, y=215, relwidth=0.4, relheight=0.07)
    b7 = Button(tm19, text="Delete teacher records", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=del_tea).place(x=221, y=295, relwidth=0.4, relheight=0.07)
    quitbut = Button(tm19, text="Quit", bg='orange', fg='white', font=("Times New Roman", 19, 'bold'),command=tm19.quit).place(x=315, y=375, relwidth=0.2, relheight=0.07)
    #Button(tm19, text="Teachers who have not returned", bg='orange', fg='white', font=("Times New Roman", 17, 'bold'),
    #       command=lambda:trex(1)).place(
    #    x=505, y=325, relwidth=0.5, relheight=0.1)
    Button(tm19, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 17, 'bold'),command=re2).place(x=355, y=475, relwidth=0.4, relheight=0.08)
    tm19.geometry('750x600')
    tm19.mainloop()
    #datetime.strptime(date_time_str, '%d/%m/%y')
awm=0
#def trex(args):
    #global awm
    #if awm==1:
    #elif awm==2:
def re2():
    global ga
    global q127
    ga = 2
    q127=0
    adinter()
def teacherr():
    global tm45
    global rsna1
    global rsid1
    global rscl1
    global rsse1
    global er
    er=6
    tm19.destroy()
    tm45=tk.Tk()
    rsna1=StringVar()
    rsid1=StringVar()
    rscl1=StringVar()
    rsse1=StringVar()
    tm45.iconbitmap(r'D:\CS\Media\library.ico')
    tm45.title("Library Management")
    Label(tm45, text="Please enter details below", bg="black", fg="white").pack()
    Label(tm45, text="Teacher Id * ").pack()
    tid2=Entry(tm45, textvariable=rsid1)
    tid2.pack()
    rsid1.set('abc')
    tpass1 = Label(tm45, text="Name * ")
    tpass1.pack()
    tpass2 = Entry(tm45, textvariable=rsna1)
    tpass2.pack()
    rsna1.set('0000')
    tdep1 = Label(tm45, text="Department * ")
    tdep1.pack()
    tdep2 = Entry(tm45, textvariable=rscl1)
    tdep2.pack()
    rscl1.set('000')
    b0 = Button(tm45, text="Register", width=10, height=1, bg="blue", fg="white",command=register_tea2).pack()
    Button(tm45, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=retm11).pack(padx=20,pady=30)
    tm45.geometry("600x300")
    tm45.mainloop()
def retm11():
    global q127
    q127=2
    teach()
def register_tea2():
    tid3=rsid1.get()
    tname3=rsna1.get()
    tdep3=rscl1.get()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha() :
        try:
            cursor = hi.cursor(
                "create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
            ins = "insert into teacher values('{}','{}','{}')".format(tid3, tname3, tdep3)
            cursor.execute(ins)
            hi.commit()
            messagebox.showinfo(title='Library Management',message='Teacher added successfully')
        except:
            engine.say('A Teacher with same id already exists')
            engine.say('Please give a different id')
            rsid1.set('abc')
            engine.runAndWait()
    else:
        incrt_ent()
def del_tea():
    global tm62
    global sid11
    global er
    er = 8
    if se1 == 0:
        tm19.destroy()
    tm62 = tk.Tk()
    sid11 = StringVar()
    Label(tm62, text="Please enter details below", bg="black", fg="white").pack()
    Label(tm62, text="Teacher Id * ").pack()
    tid2 = Entry(tm62, textvariable=sid11)
    tid2.pack()
    sid11.set('abc')
    b0 = Button(tm62, text="Submit", width=10, height=1, bg="blue", fg="white", command=del_te)
    b0.pack()
    quitbut = Button(tm62,text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'), command=tm62.quit)
    quitbut.pack(padx=46,pady=20)
    Button(tm62 , text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ab_ret11).pack(padx=20, pady=40)
    tm62.geometry("600x300")
    tm62.mainloop()
def ab_ret11():
    global q127
    q127=21
    teach()
def del_te():
    global j1
    global sdel1
    tid3 = sid11.get()
    cursor = hi.cursor("create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
    cursor.execute("select Tid,Name,Department from teacher")
    x=cursor.fetchall()
    if tid3.isdigit():
        sdel1 = Tk()
        for iv in x:
            if tid3 == str(iv[0]):
                j1 = tid3
                Label(sdel1, text=iv, bg="black", fg="white", font=("Times New Roman", 35, 'bold')).pack(pady=50)
                b0 = Button(sdel1, text="Submit", width=10, height=1, bg="blue", fg="white", command=asd7)
                b0.pack()
                break
        else:
            Label(sdel1, text="Teacher does not exist", bg='blue', fg='white',
                  font=("Times New Roman", 19, 'bold')).pack()
        Button(sdel1, text="Admin-Teacher menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),
               command=rtuy).pack(padx=20, pady=40)
    else:
        tm62.destroy()
        incrt_ent()
def asd7():
    cursor = hi.cursor("create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
    cursor.execute("select Tid from teacher")
    x = cursor.fetchall()
    for i in x:
        if i[0]==j1:
            ins = "delete from teacher where Tid='{}'".format(j1)
            cursor.execute(ins)
            hi.commit()
            Label(sdel1, text="Teacher removed successfully", bg='blue', fg='white',font=("Times New Roman", 19, 'bold')).pack()
            break
    else:
        Label(sdel1, text="Teacher does not exist", bg='blue', fg='white',
              font=("Times New Roman", 19, 'bold')).pack()
def rtuy():
    global q127
    q127=9
    teach()
def upd_teach():
    global bw21
    global stid11
    global stna11
    global scla11
    global er
    er=7
    tm19.destroy()
    bw21 = tk.Tk()
    stid11 = StringVar()
    stna11 = StringVar()
    scla11 = StringVar()
    bw21.iconbitmap(r'D:\CS\Media\library.ico')
    bw21.title("Library Management")
    Label(bw21, text="Teacher Id * ").pack()
    tid2 = Entry(bw21, textvariable=stid11)
    tid2.pack()
    stid11.set('abc')
    tpass1 = Label(bw21, text="Teacher Name * ")
    tpass1.pack()
    tpass2 = Entry(bw21, textvariable=stna11)
    tpass2.pack()
    stna11.set('enter')
    tdep11 = Label(bw21, text="Department * ")
    tdep11.pack()
    tdep2 = Entry(bw21, textvariable=scla11)
    tdep2.pack()
    scla11.set('enter')
    b0 = Button(bw21, text="Modify", width=10, height=1, bg="blue", fg="white", command=upd_det8).pack()
    Button(bw21, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret23).pack(padx=20, pady=20)
    bw21.geometry("600x300")
    bw21.mainloop()
def ret23():
    global q127
    q127=10
    teach()
def upd_det8():
    tid3 = stid11.get()
    tname3 = stna11.get()
    tdep3 = scla11.get()
    cursor = hi.cursor("create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
    cursor.execute("select Tid from teacher")
    x = cursor.fetchall()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha():
        for i in x:
            if i[0] == int(tid3):
                cursor = hi.cursor("create table teacher(Tid varchar(3) primary key, Name varchar(20),Department varchar(10)) if not exists")
                ins = "update teacher set Name='{}',Department='{}' where Tid='{}'".format(tname3, tdep3, tid3)
                cursor.execute(ins)
                hi.commit()
                messagebox.showinfo(title='Library Management',message='Teacher details updated successfully')
                break
        else:
            engine.say('Teacher id does not exist')
            engine.say('Please enter a valid teacher id')
            engine.runAndWait()
            bid2.set('abc')
    else:
        incrt_ent()
def abo():
    global abo1
    global es
    es=0
    if q1==0:
        swin9.destroy()
    elif q1==3:
        bw.destroy()
    elif q1==5:
        tm6.destroy()
    elif q1==6:
        bw1.destroy()
    elif q1==7:
        sl90.destroy()
    abo1=Tk()
    Button(abo1,text="Add books", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=add_book).pack()
    Button(abo1,text="Delete books", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'),command=del_book).pack()
    Button(abo1,  text="Modify books", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'), command=mod_book).pack()
    Button(abo1, text="View books", bg='blue', fg='white', font=("Times New Roman", 19, 'bold'), command=view_book).pack()
    Button(abo1, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=re3).pack(padx=20, pady=30)
    abo1.mainloop()
def re3():
    global ga
    global q1
    ga = 3
    q1=0
    adinter()
def add_book():
    global bw
    global bid
    global bnam
    global baut
    global bpub
    global bno
    global tqty2
    global bcat
    abo1.destroy()
    bw = Tk()
    bid = StringVar()
    bnam = StringVar()
    baut = StringVar()
    bpub = StringVar()
    bno =StringVar()
    bcat=StringVar()
    a2=Label(bw, text="Please enter book details below", bg="black", fg="white").pack()
    p2=Label(bw, text="Book Id * ").pack()
    tid2 = Entry(bw, textvariable=bid)
    tid2.pack()
    bid.set('abc')
    tpass1 = Label(bw, text="Book Name * ")
    tpass1.pack()
    tpass2 = Entry(bw, textvariable=bnam)
    tpass2.pack()
    bnam.set('abcd')
    tdep1 = Label(bw, text="Author of the book * ")
    tdep1.pack()
    tdep2 = Entry(bw, textvariable=baut)
    tdep2.pack()
    baut.set("0000")
    tname1 = Label(bw, text="Publication * ")
    tname1.pack()
    tname2 = Entry(bw, textvariable=bpub)
    tname2.pack()
    bpub.set("0000")
    tcat1 = Label(bw, text="Category * ")
    tcat1.pack()
    tcat2 = ttk.Combobox(bw,width=15,textvariable=bcat)
    tcat2['values']=("fantasy","adventure","horror","fiction","scientific","reference")
    tcat2.pack()
    tqty1 = Label(bw, text="Qty * ")
    tqty1.pack()
    tqty2 =Spinbox(bw,from_=0,to=100)
    tqty2.pack()
    b0 = Button(bw, text="Add book", width=10, height=1, bg="blue", fg="white", command=register_book).pack()
    Button(bw, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ab_ret).pack(padx=20,pady=40)
    quitbut = Button(bw, text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'),command=bw.quit).pack(padx=46, pady=20)
    bw.geometry("600x600")
    bw.mainloop()
def ab_ret():
    global q1
    q1=3
    abo()
def register_book():
    global er
    er=0
    tid3=bid.get()
    tname3=bnam.get()
    tdep3=baut.get()
    tpass3=bpub.get()
    tno3=tqty2.get()
    tcat3=bcat.get()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha() and tpass3.isalpha():
        try:
            cursor = hi.cursor(
                "create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
            ins = "insert into books values('{}', '{}','{}','{}','{}','{}')".format(int(tid3), tname3, tdep3, tpass3, tno3,tcat3)
            cursor.execute(ins)
            hi.commit()
            messagebox.showinfo(title='Book',message='Book added successfully')
        except:
            engine.say('Book with same book id already exists')
            engine.say('Please give a different id')
            bid.set('abc')
            engine.runAndWait()
    else:
        incrt_ent()
def incrt_ent():
    global inc01
    inc01 = Tk()
    inc01.iconbitmap(r'D:\CS\Media\library.ico')
    inc01.title("Library Management")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',145)
    if es==0:
        engine.say('Please enter only numeric value while entering book id')
        engine.runAndWait()
    elif es==1:
        engine.say('Please enter only numeric value while entering student id')
        engine.runAndWait()
    elif es==2:
        engine.say('Please enter only numeric value while entering teacher id')
        engine.runAndWait()
    e1=Label(inc01,text="Enter correct values ",bg='orange', fg='white',font=("Times New Roman", 15, 'bold'))
    e1.pack()
    e2=Label(inc01,text="If you want to retry press here", bg='green', fg='yellow', font=("Times New Roman", 15, 'bold'))
    e2.pack(padx=30,pady=20)
    b0=Button(inc01,text="Retry", bg='green', fg='white', font=("Times New Roman", 20, 'bold'),command=ret_add)
    b0.pack(padx=20,pady=40)
    inc01.geometry('350x250')
    inc01.mainloop()
def ret_add():
    inc01.destroy()
    if er==0:
        bid.set('abc')
    if er==1:
        bid1.set('abc')
    if er==2:
        bid2.set('abc')
    if er==3:
        rsid.set('abc')
    if er==4:
        stid1.set('abc')
    if er==5:
        global se
        se=1
        del_stu()
    if er==6:
        rsid1.set('abc')
    if er==7:
        stid11.set('abc')
    if er==8:
        global se1
        se1=1
        del_tea()
#del
def del_book():
    global tm6
    global bid1
    global bna
    global er
    er=1
    abo1.destroy()
    tm6 = tk.Tk()
    bna = StringVar()
    bid1 = StringVar()
    Label(tm6, text="Please enter details below", bg="black", fg="white").pack()
    Label(tm6, text="Book Id * ").pack()
    tid2 = Entry(tm6, textvariable=bid1)
    tid2.pack()
    bid1.set('abc')
    tpass1 = Label(tm6, text="Name * ")
    tpass1.pack()
    tpass2 = Entry(tm6, textvariable=bna)
    tpass2.pack()
    bna.set('0000')
    b0 = Button(tm6, text="Delete", width=10, height=1, bg="blue", fg="white", command=del_bo)
    b0.pack()
    u1=Button(tm6, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret4)
    u1.pack(padx=20, pady=40)
    quitbut = Button(tm6,text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'), command=tm6.quit)
    quitbut.pack(padx=46,pady=20)
    tm6.geometry("600x600")
    tm6.mainloop()
def ret4():
    global q1
    q1=5
    abo()
def del_bo():
    tid3 = bid1.get()
    tname3 = bna.get()
    cursor = hi.cursor("create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
    i="select bname,bid from books"
    cursor.execute(i)
    x=cursor.fetchall()
    if tid3.isdigit() and tname3.isalpha():
        for iv in x:
            if tname3 in iv[0] and str(tid3) in str(iv[1]):
                ins = "delete from books where bname='{}'".format(tname3)
                cursor.execute(ins)
                hi.commit()
                Label(tm6, text="Book removed successfully", bg='blue', fg='white',
                      font=("Times New Roman", 19, 'bold')).pack()
                break
        else:
            engine.say('Book does not exist')
            engine.runAndWait()
            Label(tm6, text="Book does not exist", bg='blue', fg='white',
                  font=("Times New Roman", 19, 'bold')).pack()
    else:
        incrt_ent()
def mod_book():
    global bw1
    global bid2
    global bna2
    global baut2
    global bpub2
    global bcat2
    global tpass8
    global er
    er=2
    abo1.destroy()
    bw1 = tk.Tk()
    bna2 = StringVar()
    bid2 = StringVar()
    baut2=StringVar()
    bpub2=StringVar()
    bqua2=StringVar()
    bcat2=StringVar()
    Label(bw1, text="Book Id * ").pack()
    tid2 = Entry(bw1, textvariable=bid2)
    tid2.pack()
    bid2.set('abc')
    tpass1 = Label(bw1, text="Book Name * ")
    tpass1.pack()
    tpass2 = Entry(bw1, textvariable=bna2)
    tpass2.pack()
    bna2.set('enter')
    tdep1 = Label(bw1, text="Author of the book * ")
    tdep1.pack()
    tdep2 = Entry(bw1, textvariable=baut2)
    tdep2.pack()
    baut2.set('enter')
    tname1 = Label(bw1, text="Publication * ")
    tname1.pack()
    tname2 = Entry(bw1, textvariable=bpub2)
    tname2.pack()
    bpub2.set('enter')
    tcat31 = Label(bw1, text="Category * ")
    tcat31.pack()
    tcat21 = ttk.Combobox(bw1, width=15, textvariable=bcat2)
    tcat21['values'] = ("fantasy", "adventure", "horror", "fiction", "scientific", "reference")
    tcat21.pack()
    tpass7= Label(bw1, text="qty * ")
    tpass7.pack()
    tpass8 = Spinbox(bw1,from_=0,to=100)
    tpass8.pack()
    bqua2.set('enter')
    b0 = Button(bw1, text="Modify", width=10, height=1, bg="blue", fg="white", command=mod_bo).pack()
    Button(bw1, text="Return to Main menu", bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ret5).pack(padx=20, pady=40)
    quitbut = Button(bw1, text="Quit", bg='orange', fg='white', font=("Times New Roman", 25, 'bold'),command=bw1.quit).pack(padx=46, pady=20)
    bw1.geometry("600x600")
    bw1.mainloop()
def ret5():
    global q1
    q1=6
    abo()
def mod_bo():
    tid3 = bid2.get()
    tname3 = bna2.get()
    tdep3 = baut2.get()
    tpass3 = bpub2.get()
    tqua3=tpass8.get()
    tcat3=bcat2.get()
    cursor = hi.cursor("create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
    i = "select bname,bid from books"
    cursor.execute(i)
    x = cursor.fetchall()
    if tid3.isdigit() and tname3.isalpha() and tdep3.isalpha() and tpass3.isalpha():
        for iv in x:
            if int(tid3) == iv[1]:
                cursor = hi.cursor(
                    "create table books(bid integer(4) primary key , bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
                ins = "update books set bname='{}',author='{}',pub='{}',qty='{}',category='{}' where bid={}".format(tname3,tdep3,tpass3,tqua3,tcat3,int(tid3))
                cursor.execute(ins)
                hi.commit()
                messagebox.showinfo(title='Book',message='Modified details successfully')
                break
        else:
            engine.say('Book id does not exist')
            engine.say('Please enter a valid book id')
            engine.runAndWait()
            bid2.set('abc')
    else:
        incrt_ent()
y5=0
def view_book():
    global view1
    global bcat5
    if y5==0:
        abo1.destroy()
    elif y5==1:
        sl90.destroy()
    view1 = Tk()
    bcat5=StringVar()
    view1.iconbitmap(r'D:\CS\Media\library.ico')
    view1.title("Library Management")
    engine.setProperty('rate', 145)
    engine.say('Enter book category')
    engine.runAndWait()
    v1=Label(view1, text="Enter book category", bg='brown', fg='white', font=("Times New Roman", 25, 'bold'))
    v1.pack(padx=50,pady=20)
    tcat29 = ttk.Combobox(view1, width=15, textvariable=bcat5)
    tcat29['values'] = ("fantasy", "adventure", "horror", "fiction", "scientific", "reference")
    tcat29.pack()
    b1 = Button(view1, text="Press here to view", relief=RAISED, bg='orange', fg='white',font=("Times New Roman", 19, 'bold'),command=lambda:view_list(0))
    b1.pack(padx=20,pady=20)
    view1.geometry('951x568')
    view1.mainloop()
pd2={}
pageno2=0
h2=0
pgno2=0
q22=0
che=0
def view_list(args):
    global sl90
    global che
    che=args
    global z112
    if che==0:
        view1.destroy()
        a=bcat5.get()
        cursor = hi.cursor("create table books(bid integer(4) primary key, bname varchar(20),author varchar(15),pub varchar(10),qty integer(2),category varchar(20)) if not exists")
        cursor.execute("select * from books where category='{}'".format(a))
        z112=cursor.fetchall()
    elif che==1:
        tm19.destroy()
        cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
        ins = "select * from lend"
        cursor.execute(ins)
        gg=cursor.fetchall()
        cursor.execute("select tid from teacher")
        oo=cursor.fetchall()
        kgf=[]
        for i in oo:
            kgf.append(i[0])
        z112=[]
        for v in gg:
            if v[0] in kgf:
                z112.append(v)
    elif che==2:
        tm1.destroy()
        cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
        ins = "select * from lend"
        cursor.execute(ins)
        gg=cursor.fetchall()
        cursor.execute("select studid from student")
        oo=cursor.fetchall()
        kgf=[]
        for i in oo:
            kgf.append(i[0])
        z112=[]
        for v in gg:
            if v[0] in kgf:
                z112.append(v)
    elif che==3:
        tm1.destroy()
        cursor = hi.cursor("create table lend(sid int(4) primary key,sname varchar(20),bname varchar(20),author varchar(20),borrow_date date,return_date date) if not exists")
        ins = "select * from lend where return_date < curdate()"
        cursor.execute(ins)
        gg=cursor.fetchall()
        cursor.execute("select studid from student")
        oo=cursor.fetchall()
        kgf=[]
        for i in oo:
            kgf.append(i[0])
        z112=[]
        for v in gg:
            if v[0] in kgf:
                z112.append(v)
    sl90=Tk()
    sl90.iconbitmap(r'D:\CS\Media\library.ico')
    sl90.title("Library Management")
    global len32
    global len22
    global pageno2
    global pd2
    len32=len(z112)
    if len32%7==0:
        print('hi')
    else:
        if len32>7:
            len22=int(len32%7)
    if len32>7:
        pageno2=2
        if len32>14:
            pageno2=int((len32-len22)/7)
    else:
        pageno2=1
    a9=0;b9=7
    for i in range(1,pageno2+1):
        pd2[i]=[a9,b9]
        a9=b9
        b9+=7
    if len32>14:
        if pageno2>1:
            pd2[pageno2+1]=[len32-len22,len32+1]
    if q22==0:
        h13=0
        g13=7
    hello1()
    sl90.geometry('1200x600')
    sl90.mainloop()
def hello1():
    z=1
    if che==0:
        a=bcat5.get()+'  '+'books'
        lw=["Book Id","Name","Author","publication","Category","Qty"]
        Button(sl90,text="Other Category",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ocat).place(x=250, y=520)
    elif che==1:
        a='List of Teachers borrowed'
        lw=["Teacher Id","Name","Book","Author","R.Date","B.Date"]
        Button(sl90,text="Main menu",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ocat1).place(x=250, y=520)
    elif che==2:
        a='List of Students borrowed'
        lw=["Student Id","Name","Book","Author","R.Date","B.Date"]
        Button(sl90,text="Main menu",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ocat2).place(x=250, y=520)
    elif che==3:
        a='List of Students who missed the due date'
        lw=["Student Id","Name","Book","Author","R.Date","B.Date"]
        Button(sl90,text="Main menu",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=ocat3).place(x=250, y=520)    
    l1 = Label(sl90,text="{}".format(a.upper()), bg='brown', fg='white', font=("Times New Roman", 25, 'bold')).place(x=0, y=0,relwidth=1,relheight=0.08)
    l1 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=45,relwidth=1,relheight=0.004)
    l2 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=2, y=105, relwidth=1, relheight=0.004)
    l3 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=170, y=1, relwidth=0.004, relheight=1)
    l4 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=0, y=1,relwidth=0.004, relheight=1)
    l5 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=390, y=1, relwidth=0.004, relheight=1)
    l6 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=600, y=1, relwidth=0.004, relheight=1)
    l7 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=800, y=1, relwidth=0.004, relheight=1)
    l8 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=1000, y=1, relwidth=0.004, relheight=1)
    l9 = Label(sl90, bg='brown', font=("Times New Roman", 25, 'bold')).place(x=1195, y=1, relwidth=0.004, relheight=1)
    Label(sl90,text=lw[0], fg='green', font=("Times New Roman", 25, 'bold')).place(x=15, y=55)
    Label(sl90,text=lw[1], fg='green', font=("Times New Roman", 25, 'bold')).place(x=210, y=55)
    Label(sl90,text=lw[2], fg='green', font=("Times New Roman", 25, 'bold')).place(x=420, y=55)
    Label(sl90,text=lw[3], fg='green', font=("Times New Roman", 25, 'bold')).place(x=610, y=55)
    Label(sl90,text=lw[4], fg='green', font=("Times New Roman", 25, 'bold')).place(x=820, y=55)
    Label(sl90,text=lw[5], fg='green', font=("Times New Roman", 25, 'bold')).place(x=1050, y=55)
    global pgno2
    a=55;b=125
    if h2==0:
        pgno2=1
    try:
        h13=pd2[pgno2][0]
        g13=pd2[pgno2][1]
    except:
        engine.say('No more books available')
        engine.runAndWait()
    if len3>14:
        if pgno2==pageno2+1 :
            Button(sl90,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back12).place(x=250, y=470)
        elif pgno2==1 and pd2.get(2)!=None:
            Button(sl90,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next12).place(x=450, y=470)
        elif pgno2>1:
            Button(sl90,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next12).place(x=450, y=470)
            Button(sl90,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back12).place(x=250, y=470)
    else:
        if pgno2==2:
            Button(sl90,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back12).place(x=250, y=470)
        elif pgno2==1 and pd2.get(2)!=None:
            Button(sl90,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next12).place(x=450, y=470)
        elif pgno2>1:
            Button(sl90,text="Next Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=next12).place(x=450, y=470)
            Button(sl90,text="Previous Page",bg='orange', fg='white', font=("Times New Roman", 15, 'bold'),command=back12).place(x=250, y=470)
    for i in z112[h13:g13]:
        Label(sl90,text=i[0],font=("Times New Roman", 20, 'bold')).place(x=a,y=b)
        Label(sl90,text=i[1],font=("Times New Roman", 20, 'bold')).place(x=a+165,y=b)
        Label(sl90,text=i[2],font=("Times New Roman", 20, 'bold')).place(x=a+379,y=b)
        Label(sl90, text=i[3], font=("Times New Roman", 20, 'bold')).place(x=a +585, y=b)
        Label(sl90, text=i[5], font=("Times New Roman", 20, 'bold')).place(x=a + 799, y=b)
        Label(sl90, text=i[4], font=("Times New Roman", 20, 'bold')).place(x=a + 1009, y=b)
        z+=1
        b+=50
def ocat():
    global y5
    y5=1
    view_book()
def ocat1():
    global q127
    q127=54
    teach()
def ocat2():
    global q12
    q12=34
    studen()
def ocat3():
    global q12
    q12=344
    studen()
def next12():
    #global f12
    #f12=1
    global h2
    h2=1
    global pgno2
    pgno2=pgno2+1
    global q22
    q22=1
    lst=sl90.place_slaves()
    for i in lst:
        i.destroy() 
    hello1()
def back12():
    #2global f12
    #f12=1
    global h2
    h2=1
    global pgno2
    pgno2=pgno2-1  
    global q22
    q22=1
    lst=sl90.place_slaves()
    for i in lst:
        i.destroy()
    hello1()
def ret_tea99():
    global q1
    q1=7
    abo()
def stream():
    global root
    while True:
        try:         
            image = video.get_next_data()            
            frame_image = Image.fromarray(image)
            frame_image=ImageTk.PhotoImage(frame_image)
            l1.config(image=frame_image)
            l1.image = frame_image
            while True:
                try:
                    p.play()
                    l1.after(delay,lambda: stream())
                    return
                except:
                    break
        except:
            engine.setProperty('rate',205)
            engine.say('Welcome to MAG library management and Thank you for using me')
            engine.runAndWait()
            Button(root,text='Press to continue',relief=SUNKEN,fg='white',bg='orange',font=("Times New Roman", 19, 'bold'),command=acsspage).place(x=1100,y=500)
            root.bind('<Return>',lambda event=None:acsspage())
            return
########### Main Program ############
vid=0
p = vlc.MediaPlayer(r'D:\CS\Media\mainaud123.mp3')
video_name =r'D:\CS\Media\T3.mp4' #Image-path
p = vlc.MediaPlayer(r'D:\CS\Media\mainaud123.mp3')
root = Tk()
root.title('Library Management')
root.iconbitmap(r'D:\CS\Media\library.ico')
'''f1=Frame()
l1 = Label(f1)
l1.pack()
f1.pack()
video = imageio.get_reader(video_name)
delay = int(30/ video.get_meta_data()['fps'])'''
stream()
root.mainloop()