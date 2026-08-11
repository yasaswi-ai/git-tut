import mysql.connector

# 1. Connect to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="My1stjob@2026"
)

mycursor = mydb.cursor()
# 2. CREATE DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS crud_db")
mycursor.execute("USE crud_db")
print("Connected to MySQL successfully!")

# 3. CREATE TABLE
mycursor.execute("CREATE TABLE IF NOT EXISTS students (roll INT PRIMARY KEY, name VARCHAR(50), marks INT)")

# 4. INSERT - CREATE
sql="INSERT INTO students(roll, name,marks)VALUES(%s, %s, %s)"
val=[
     (101,"yasaswi",85),
     (102,"dhrithika",92),
     (103,"rushika",78),
     (104,"rushika",98),
     (105,"isshika",98)
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("\nCREATE: students records inserted")

# 5. READ BEFORE
mycursor.execute("SELECT * FROM students")
print("\nREAD BEFORE UPDATE/DELETE:")
for x in mycursor.fetchall():
  print(x)

# 6. UPDATE
mycursor.execute("UPDATE students SET marks = 95 WHERE roll = 101")
mydb.commit()
print("\nUPDATE: yasaswi marks updated to 95")

# 7. DELETE
mycursor.execute("DELETE FROM students WHERE roll = 105")
mydb.commit()
print("DELETE: isshika deleted")

# 8. READ AFTER
mycursor.execute("SELECT * FROM students")
print("\nFINAL DATA AFTER CRUD:")
for x in mycursor.fetchall():
  print(x)

mydb.close()