import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="pythonuser",
    password="mypassword")
print(mydb.connection_id)
c=mydb.cursor()
c.execute("show databases")
for i in c:
    print(i)
c.execute("create database sample")



