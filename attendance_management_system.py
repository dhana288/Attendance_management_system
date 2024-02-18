import mysql.connector
from datetime import datetime

print("Welcome to the codenera attendance management system!!")

def student_login():
    mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
    cur=mydb.cursor()
    mail=input("Enter your mail id : ")
    pwd=input("Enter your password : ")
    my_data=(mail,)
    m="SELECT Mail_id,Password FROM login_details WHERE Mail_id=%s"
    cur.execute(m,my_data)
    result=cur.fetchone()
    try : 
        if(result[0]==mail and result[1][:-3]==pwd):
            print("Login successful!!")
            print("For marking the attendance : ")
            now=datetime.now()
            today=now.strftime("%Y/%m/%d %H:%M:%S")
            mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
            cur=mydb.cursor()
            course=int(input("Enter your course (1 - C, 2 - C++, 3 - Python, 4 - Java, 5 - Data Science, 6 - Machine learning) : "))
            roll=int(input("Enter your roll no. : "))
            att=input("Enter P - present A - Absent : ")
            if(course==1):
                sd="INSERT INTO c_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==2):
                sd="INSERT INTO cpp_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==3):
                sd="INSERT INTO py_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==4):
                sd="INSERT INTO java_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==5):
                sd="INSERT INTO ds_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==6):
                sd="INSERT INTO ml_attend (Roll_no,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(roll,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
    except:
        print("Login failed!!")

def trainer_login():
    mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
    cur=mydb.cursor()
    mail=input("Enter your mail id : ")
    pwd=input("Enter your password : ")
    my_data=(mail,)
    m="SELECT Mail_id,Password FROM login_details WHERE Mail_id=%s"
    cur.execute(m,my_data)
    result=cur.fetchone()
    try : 
        if(result[0]==mail and result[1][:-3]==pwd):
            print("Login successful!!")
            print("For marking the attendance : ")
            now=datetime.now()
            today=now.strftime("%Y/%m/%d %H:%M:%S")
            mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
            cur=mydb.cursor()
            course=int(input("Enter your course (1 - C, 2 - C++, 3 - Python, 4 - Java, 5 - Data Science, 6 - Machine learning) : "))
            emp=int(input("Enter your employee id : "))
            att=input("Enter P - present A - Absent : ")
            if(course==1):
                sd="INSERT INTO c_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==2):
                sd="INSERT INTO cpp_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==3):
                sd="INSERT INTO py_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==4):
                sd="INSERT INTO java_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==5):
                sd="INSERT INTO ds_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
            elif(course==6):
                sd="INSERT INTO ml_attend (Emp_id,Timestamp,Attendance) VALUES(%s,%s,%s)"
                d=(emp,today,att.upper())
                cur.execute(sd,d)
                mydb.commit()
    except:
        print("Login failed!!")


#For admin
role=int(input("Enter 1 - Admin, 2 - Student, 3 - Trainer : "))
if(role==1):
    print("Welcome to the admin portal")
    id=input("Enter your user id : ")
    pwd=input("Enter your password : ")
    if(id=="12345" and pwd=="pass@123"):
        print("Login successful!!")
        att=int(input("Whose attendance you want to view?? Enter 1 : Students, 2 : Trainers : "))
        crs=int(input("Which course attendance you want to view?? Enter 1 : C, 2 : C++ 3, : Python, 4 : Java, 5: Data Science, 6 : Machine Learning : "))
        if(att==1):
            if(crs==1):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM c_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==2) :
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM cpp_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==3):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM py_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==4):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM java_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==5):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM ds_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==6):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
                cur=mydb.cursor()
                c="SELECT * FROM ml_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            else:
                ("Invalid course")
        elif(att==2):
            if(crs==1):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM c_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==2) :
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM cpp_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==3):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM py_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==4):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM java_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==5):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM ds_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            elif(crs==6):
                mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
                cur=mydb.cursor()
                c="SELECT * FROM ml_attend"
                cur.execute(c)
                result=cur.fetchall()
                for ele in result:
                    print(ele)
            else:
                ("Invalid course")
        else:
            print("Invalid")
    else:
        print("Login failed!!")

#For student
elif(role==2):
    print("Welcome to the Student portal")
    login=int(input("1 - Login, 2 - Register : "))
    if(login==1):
        student_login()

    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='student')
        cur=mydb.cursor()
        sd="INSERT INTO stu_details (Roll_no,Full_name,Mail_id,Contact_no,Course) VALUES(%s,%s,%s,%s,%s)"
        print("Welcome to the student registration portal!!")
        roll=int(input("Enter your roll no. : "))
        name=input("Enter your name : ")
        mail=input("Enter your mail id : ")
        mobile=input("Enter your contact no. : ")
        course=input("Enter your course (C,C++,Python,Java,Data Science,Machine learning) : ")
        d=(roll,name,mail,mobile,course)
        cur.execute(sd,d)
        mydb.commit()
        ld="INSERT INTO login_details (Mail_id,Password) VALUES(%s,%s)"
        pwd=input("Enter your password : ")
        pd=(mail,pwd+"123")
        cur.execute(ld,pd)
        mydb.commit()
        print("Welcome to the student login portal!! ")
        student_login()

#For trainer
elif(role==3):
    print("Welcome to the Trainer portal!!")
    login=int(input("1 - Login, 2 - Register : "))
    if(login==1):
        trainer_login()

    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Dhanashri@28',database='trainer')
        cur=mydb.cursor()
        sd="INSERT INTO tra_details (Emp_id,Full_name,Mail_id,Contact_no,Course) VALUES(%s,%s,%s,%s,%s)"
        print("Welcome to the trainer registration prtal!!")
        emp=int(input("Enter your employee id : "))
        name=input("Enter your name : ")
        mail=input("Enter your mail id : ")
        mobile=input("Enter your contact no. : ")
        course=input("Enter your course (C,C++,Python,Java,Data Science,Machine learning) : ")
        d=(emp,name,mail,mobile,course)
        cur.execute(sd,d)
        mydb.commit()
        ld="INSERT INTO login_details (Mail_id,Password) VALUES(%s,%s)"
        pwd=input("Enter your password : ")
        pd=(mail,pwd+"123")
        cur.execute(ld,pd)
        mydb.commit()
        print("Welcome to the trainer login portal!! ")
        trainer_login()






