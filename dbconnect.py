import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@ssw0rd@123",
    database="AnkurDB"
)

# print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("SHOW tables")

#mycursor.execute("CREATE TABLE students (name varchar(255), age integer(10))")
#mycursor.execute("INSERT into students(name,age) values ('Bob', 24)")
#sql = ("select name from students ORDER BY name DESC LIMIT 3 OFFSET 2")
#sql1 = "UPDATE students SET age=13 where age=40"
#sql2 = "DELETE FROM students WHERE age = 13"
sql3 = "DROP TABLE IF EXISTS students"
mycursor.execute(sql3)
#for tb in mycursor:
#   print(tb)

#myresults =  mycursor.fetchall()
#for row in myresults:
# print(row)


# sqlFormula = "INSERT INTO students(name,age) VALUES(%s,%s)"
# students=[('Alok',21),('Amit',20)]
# mycursor.executemany(sqlFormula,students)
mydb.commit()
