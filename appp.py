import mysql.connector

# 1. Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="My1stjob@2026"
)

mycursor = mydb.cursor()
