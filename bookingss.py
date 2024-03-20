import mysql.connector
ab=mysql.connector.connect(host="localhost", user="root", password="12345678")
cur=ab.cursor()
def table():
    cur.execute("use busrsv")
    cur.execute("create table bookings(email varchar(50), id int(6) not null primary key, name varchar(50), age int(3), from1 varchar(20), to1 varchar(20), tddate date not null, tdttime time not null, journeydate date not null)")
    cur.execute("commit")

def show():
    cur.execute("use busrsv")
    cur.execute("select * from bookings")
    a=cur.fetchall()
    for i in a:
        print(i)
    cur.execute("commit")

def choice():
    ch=int(input("press 1 to create database or 2 to show bookings: "))
    if ch==1:
        table()
    elif ch==2:
        show()
    else:
        print("wrong input")
        choice()

choice()
