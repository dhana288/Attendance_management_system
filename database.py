import mysql.connector

# creating databases
mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28')
cur=mydb.cursor()
cur.execute("CREATE DATABASE student")
cur.execute("CREATE DATABASE trainer")
cur.execute("CREATE DATABASE admin")


# creating tables for student database
mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
cur=mydb.cursor()
d="CREATE TABLE stu_details (Roll_no INT PRIMARY KEY,Full_name VARCHAR(50) NOT NULL,Mail_id VARCHAR(50) UNIQUE NOT NULL,Contact_no VARCHAR(10) NOT NULL,Course VARCHAR(50) NOT NULL)"
l="CREATE TABLE login_details (Mail_id VARCHAR(50) PRIMARY KEY,Password VARCHAR(25) UNIQUE NOT NULL)"
cur.execute(d)
cur.execute(l)
c="CREATE TABLE c_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
cpp="CREATE TABLE cpp_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
py="CREATE TABLE py_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
java="CREATE TABLE java_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
ds="CREATE TABLE ds_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
ml="CREATE TABLE ml_attend (Roll_no INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
for ele in [c,cpp,py,java,ds,ml]:
    cur.execute(ele)


# creating tables for trainer database
mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
cur=mydb.cursor()
td="CREATE TABLE tra_details (Emp_id INT PRIMARY KEY,Full_name VARCHAR(50) NOT NULL,Mail_id VARCHAR(50) UNIQUE NOT NULL,Contact_no VARCHAR(10) NOT NULL,Course VARCHAR(50) NOT NULL)"
tl="CREATE TABLE login_details (Mail_id VARCHAR(50) PRIMARY KEY,Password VARCHAR(25) UNIQUE NOT NULL)"
cur.execute(td)
cur.execute(tl)
c="CREATE TABLE c_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
cpp="CREATE TABLE cpp_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
py="CREATE TABLE py_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
java="CREATE TABLE java_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
ds="CREATE TABLE ds_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
ml="CREATE TABLE ml_attend (Emp_id INT NOT NULL,Timestamp DATETIME,Attendance VARCHAR(1))"
for ele in [c,cpp,py,java,ds,ml]:
    cur.execute(ele)


# Creating table for admin database
mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='admin')
cur=mydb.cursor()
a="CREATE TABLE admin_login (User_id VARCHAR(25) NOT NULL,Password VARCHAR(25) NOT NULL)"
cur.execute(a)






