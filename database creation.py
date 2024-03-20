import mysql.connector
ab=mysql.connector.connect(host="localhost", user="root", password="12345678")
cur=ab.cursor()
cur.execute("create database busrsv")
cur.execute("commit")
