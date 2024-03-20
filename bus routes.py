import mysql.connector
ab=mysql.connector.connect(host="localhost", user="root", password="12345678")
cur=ab.cursor()
def table():
    cur.execute("use busrsv")
    cur.execute("create table busroutes(from1 varchar(20), to1 varchar(20), dep1 time, cost int(4))")
    st2="insert into busroutes values('{}','{}','{}',{})".format('kolkata','delhi','09:00:00',1000)
    st3="insert into busroutes values('{}','{}','{}',{})".format('delhi','kolkata','09:00:00',1000)
    st4="insert into busroutes values('{}','{}','{}',{})".format('kolkata','patna','09:00:00',900)
    st5="insert into busroutes values('{}','{}','{}',{})".format('patna','kolkata','09:00:00',900)
    st6="insert into busroutes values('{}','{}','{}',{})".format('delhi','mumbai','09:00:00',700)
    st7="insert into busroutes values('{}','{}','{}',{})".format('mumbai','delhi','09:00:00',700)
    st8="insert into busroutes values('{}','{}','{}',{})".format('mumbai','hyderabad','09:00:00',1500)
    st9="insert into busroutes values('{}','{}','{}',{})".format('hyderabad','mumbai','09:00:00',1500)
    st10="insert into busroutes values('{}','{}','{}',{})".format('lucknow','kanpur','09:00:00',1000)
    st11="insert into busroutes values('{}','{}','{}',{})".format('kanpur','lucknow','09:00:00',1000)
    cur.execute(st2)
    cur.execute(st3)
    cur.execute(st4)
    cur.execute(st5)
    cur.execute(st6)
    cur.execute(st7)
    cur.execute(st8)
    cur.execute(st9)
    cur.execute(st10)
    cur.execute(st11)
    cur.execute("commit")
def show():
    cur.execute("use busrsv")
    cur.execute("select * from busroutes")
    a=cur.fetchall()
    for i in a:
        print(i)
    cur.execute("commit")

def choice():
    ch=int(input("press 1 to create busroutes or 2 to show busroutes: "))
    if ch==1:
        table()
    elif ch==2:
        show()
    else:
        print("wrong input")
        choice()

choice()
