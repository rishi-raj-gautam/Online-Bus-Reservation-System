import mysql.connector
ab=mysql.connector.connect(host="localhost", user="root", password="12345678")
cur=ab.cursor()
def table():
    cur.execute("use busrsv")
    cur.execute("create table register(email varchar(50), name varchar(50), phn varchar(11), pass varchar(20))")
    cur.execute("commit")

def show():
    cur.execute("use busrsv")
    cur.execute("select * from register")
    a=cur.fetchall()
    for i in a:
        print(i)
    cur.execute("commit")

def choice():
    ch=int(input("press 1 to create database or 2 to show log in details: "))
    if ch==1:
        table()
    elif ch==2:
        show()
    else:
        print("wrong input")
        choice()

choice()
