import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="My1stjob@2026")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS crud_db")
mycursor.execute("USE crud_db")
mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT, email VARCHAR(100))")
mydb.commit()