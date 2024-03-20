print('''-----------------------------------------------------------------------------------
|                                                                                 |
|                                                                                 |
|                    WELCOME TO ONLINE BUS RESERVATION  PORTAL                    |
|                                                                                 |
|                                                                                 |
-----------------------------------------------------------------------------------
''')
import mysql.connector
ab=mysql.connector.connect(host="localhost", user="root", password="12345678")
cur=ab.cursor()
import random
from datetime import date
todayd=date.today()
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#<------------------------CHOICE FOR SIGNUP AND LOG IN--------------------------------->
def choice():
    print("1.register")
    print("2.log in")
    ch=int(input("enter your choice: "))
    if ch==1:
        register()
    elif ch==2:
        login()
    else:
        print("wrong choice")
        choice()
#<-----------------------REGISTRATION--------------------------------------------------->
def register():
    print("<-------------------------------REGISTER------------------------------------------->")
    global em
    global name
    em=input("enter your email adress: ")
    name=input("enter your name: ")
    def phone():
        global sp
        ph=int(input("enter your phone number: "))
        sp=str(ph)
        l=len(sp)
        if l==10:
            pass
        else:
            print("phone number more than 10 digits")
            phone()
    phone()
    pwd=input("enter your password: ")
    cur.execute("use busrsv")
    st="insert into register values('{}','{}','{}','{}')".format(em,name,sp,pwd)
    cur.execute(st)
    cur.execute("commit")
    print("registered")
    login()
#<-------------------------------LOGIN------------------------------------------->
def login():
    print("<-------------------------------LOG IN------------------------------------------->")
    flag=0
    global em2
    global pwd2
    em2=input("enter your email adress: ")
    pwd2=input("enter your password: ")
    cur.execute("use busrsv")
    cur.execute("select * from register")
    obj=cur.fetchall()
    for i in obj:
        if i[0]==em2 and i[3]==pwd2:
            flag=1
            cur.execute("commit")
            break
    if flag==1:
        print("-------------------------------------------------------------")
        print("logged in")
        print("-------------------------------------------------------------")
        print()
        print("1.book ticket")
        print("2.view ticket")
        print("3.cancel ticket")
        print("4.generate ticket")
        print("5.update profile")
        print("6.report problem")
        print("7.log out")
        print("8.delete account")
        ch2=int(input("enter your choice: "))
        if ch2==1:
            booking()
        elif ch2==2:
            view()
        elif ch2==3:
            cancel()
        elif ch2==4:
            generate()
        elif ch2==5:
            update()
        elif ch2==6:
            report()
        elif ch2==7:
            logout()
        else:
            delete()
    else:
        print("-------------------------------------------------------------")
        print("your email or password is wrong, try again or register")
        print("1.register")
        print("2.login again")
        ch=int(input("enter your choice: "))
        if ch==1:
            register()
        else:
            login()
#<-----------------------------------BOOKING--------------------------------------->
def booking():
    print("<----------------DAILY BUS ROUTES--------------->")
    print("NOTE:\nSelect cities from:-\nKOLKATA,DELHI,PATNA,HYDERABAD,MUMBAI,LUCKNOW") 
    cur.execute("use busrsv")
    from1=input("enter FROM location: ")
    cur.execute("select * from busroutes")
    obj=cur.fetchall()
    for i in obj:
        if i[0]==from1:
            print(i[0]+"---------->"+i[1]+"---------->",i[2],"---------->",i[3],"\-")
    to1=input("enter TO location: ")
    s=int(input("enter no. of passengers: "))
    for j in range(0,s,1):
        psgr=input("enter name of the passenger: ")
        age=input("enter age of the passenger: ")
        jd=input("enter journey date (date should be in this format=year-month-date: ")
        tid=random.randint(100000,999999)
        st="insert into bookings values('{}',{},'{}',{},'{}','{}','{}','{}','{}')".format(em2,tid,psgr,age,from1,to1,todayd,current_time,jd)
        cur.execute(st)
        cur.execute("commit")
    print("-------------------------------------------------------------")
    print("ticket booked")
    print("-------------------------------------------------------------")
    print()
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<-----------------------------UPDATE PROFILE--------------------------------------------->
def update():
    cur.execute("use busrsv")
    cur.execute("select * from register")
    obj4=cur.fetchall()
    for i in obj4:
        if i[0]==em2:
            n=input("enter your name: ")
            st="update register set name='{}' where email='{}'".format(n,em2)
            cur.execute(st)
            def phone2():
                ph=int(input("enter your phone number: "))
                sp=str(ph)
                l=len(sp)
                if l==10:
                    st="update register set phn='{}' where email='{}'".format(sp,em2)
                    pass
                else:
                    print("phone number more than 10 digits")
                    phone2()
            phone2()
            print("do you want to change your password?? y->yes/n->no")
            ch=input("enter your choice: ")
            if ch=="y":
                pwd=input("enter new password: ")
                st="update register set pass='{}' where email='{}'".format(pwd,em2)
            else:
                break
    cur.execute("commit")
    print("-------------------------------------------------------------")
    print("profile updated")
    print("-------------------------------------------------------------")
    print()
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<----------------------------------CANCEL TICKET---------------------------------------->
def cancel():
    cur.execute("use busrsv")
    st="delete from bookings where email='{}'".format(em2)
    cur.execute(st)
    cur.execute("commit")
    print("-------------------------------------------------------------")
    print("booking canceled")
    print("-------------------------------------------------------------")
    print()
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<----------------------------------VIEW TICKET---------------------------------------->
def view():
    c=0
    cur.execute("use busrsv")
    cur.execute("select * from bookings")
    obj3=cur.fetchall()
    print()
    print("-------------------------------------------------------------")
    print("EMAIL: "+em2)
    print("-------------------------------------------------------------")
    print()
    for i in obj3:
        if i[0]==em2:
            print("BOOKING ID: ",i[1])
            print("PASSENGER'S NAME: "+i[2])
            print("AGE: ",i[3])
            print("FROM LOACATION: "+i[4])
            print("TO LOCATION: "+i[5])
            print("BOOKING DATE: ",i[6])
            print("BOOKING TIME: ",i[7])
            print("JOURNEY DATE: ",i[8])
            cur.execute("select * from busroutes")
            obj2=cur.fetchall()
            for j in obj2:
                if i[4]==j[0] and i[5]==j[1]:
                    print("DEPARTURE TIME: ",j[2])
                    amt=int(j[3])
                    c=c+amt
                    print()
                    print("-------------------------------------------------------------")
                    break
    print("TOTAL AMOUNT: ",c)
    print("-------------------------------------------------------------")
    print()
    cur.execute("commit")
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<----------------------------------GENERATE TICKET---------------------------------------->
def generate():
    c=0
    cur.execute("use busrsv")
    cur.execute("select * from bookings")
    obj3=cur.fetchall()
    nm=(r"C:\Users\RISHI PC\Desktop\online bus reservation\tickets\\"+em2+".txt")
    f=open(nm,"w")
    f.write("\n")
    f.write("-------------------------------------------------------------\n")
    f.write("EMAIL: ")
    f.write(em2)
    f.write("\n")
    f.write("-------------------------------------------------------------\n")
    f.write("\n")
    for i in obj3:
        if i[0]==em2:
            f.write("BOOKING ID: ")
            f.write(str(i[1]))
            f.write("\n")
            f.write("PASSENGER'S NAME: ")
            f.write(i[2]+"\n")
            f.write("AGE: ")
            f.write(str(i[3]))
            f.write("\n")
            f.write("FROM LOACATION: ")
            f.write(i[4]+"\n")
            f.write("TO LOCATION: ")
            f.write(i[5]+"\n")
            f.write("BOOKING DATE: ")
            f.write(str(i[6]))
            f.write("\n")
            f.write("BOOKING TIME: ")
            f.write(str(i[7]))
            f.write("\n")
            f.write("JOURNEY DATE: ")
            f.write(str(i[8]))
            f.write("\n")
            cur.execute("select * from busroutes")
            obj2=cur.fetchall()
            for j in obj2:
                if i[4]==j[0] and i[5]==j[1]:
                    f.write("DEPARTURE TIME: ")
                    f.write(str(j[2]))
                    f.write("\n")
                    amt=int(j[3])
                    c=c+amt
                    f.write("\n")
                    f.write("-------------------------------------------------------------\n")
                    break
    n=str(c)
    f.write("TOTAL AMOUNT: ")
    f.write(n)
    f.write("\n")
    f.write("-------------------------------------------------------------\n")
    f.close()
    cur.execute("commit")
    print("-------------------------------------------------------------")
    print("ticket downloaded in path: ",nm)
    print("-------------------------------------------------------------")
    print()
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<----------------------------------REPORT PROBLEM---------------------------------------->
def report():
    with open(r"C:\Users\RISHI PC\Desktop\online bus reservation\\reportproblems.txt","a")as f:
        f.write("feedback by: "+em2+"\n")
        f.write("feedback:\n")
        report=input("write your problem here: \n")
        f.write(report+"\n")
        f.write("-------------------------------------------------------------------\n")
    print()
    print("1.book another ticket")
    print("2.view ticket")
    print("3.cancel ticket")
    print("4.generate ticket")
    print("5.update profile")
    print("6.report problem")
    print("7.log out")
    print("8.delete account")
    ch2=int(input("enter your choice: "))
    if ch2==1:
        booking()
    elif ch2==2:
        view()
    elif ch2==3:
        cancel()
    elif ch2==4:
        generate()
    elif ch2==5:
        update()
    elif ch2==6:
        report()
    elif ch2==7:
        logout()
    else:
        delete()
#<----------------------------------LOGOUT---------------------------------------->
def logout():
    print("-------------------------------------------------------------")
    print("logged out")
    print("-------------------------------------------------------------")
    choice()
#<------------------------------------DELETE-------------------------------------->
def delete():
    cur.execute("use busrsv")
    st="delete from register where email='{}'".format(em2)
    cur.execute(st)
    cur.execute("commit")
    print("-------------------------------------------------------------")
    print("account deleted")
    print("-------------------------------------------------------------")
    choice()
choice()
    
