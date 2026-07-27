import mysql.connector
import mainmenu
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="school_2026", auth_plugin='mysql_native_password')
con=mydb.cursor()

def menu():
    while True:
        print("\t\t##############STUDENT DETAILS#################")
        print("1. INSERT STUDENT DETAILS")
        print("2. DELETE STUDENT DETAILS")
        print("3. SEARCH A SPECIFIC STUDENT")
        print("4. UPDATE STUDENT CLASS/SECTION")
        print("5. SHOW ALL STUDENTS")
        print("6. EXIT TO MAIN MENU")
        print()
        ch=int(input("ENTER CHOICE "))
        print()
        if (ch==1):
            insertstudent()
        if (ch==2):
            deletestudent()
        if (ch==3):
            search()
        if (ch==4):
            updatestudent()
        if (ch==5):
            displayall()
        if (ch==6):
            mainmenu.mainmenu()
        else:
            print("WHICH OPERATION DO YOU WANT TO PERFORM")

def insertstudent():
    sid=int(input("ENTER STUDENT ID "))
    sname=input("ENTER STUDENT NAME ")
    cls=input("ENTER CLASS ")
    section=input("ENTER SECTION ")
    dob=input("ENTER DATE OF BIRTH (YYYY-MM-DD) ")
    guardian=input("ENTER GUARDIAN NAME ")
    phone=input("ENTER PHONE NUMBER ")
    con.execute("insert into student values('"+str(sid)+"','"+sname+"','"+cls+"','"+section+"','"+dob+"','"+guardian+"','"+phone+"')")
    mydb.commit()
    print("########STUDENT DETAILS INSERTED SUCCESSFULLY#######")

def deletestudent():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("delete from student where sid='"+str(sid)+"'")
    mydb.commit()
    print("########STUDENT DELETED#######")

def search():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("select * from student where sid='"+str(sid)+"'")
    for i in con:
        print(i)

def updatestudent():
    sid=int(input("ENTER STUDENT ID "))
    cls=input("ENTER NEW CLASS ")
    section=input("ENTER NEW SECTION ")
    con.execute("update student set class='"+cls+"', section='"+section+"' where sid='"+str(sid)+"'")
    mydb.commit()
    print("########STUDENT UPDATED#######")

def displayall():
    con.execute("select * from student")
    for i in con:
        print(i)
