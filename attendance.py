import mysql.connector
import mainmenu
import datetime as dt
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="school_2026", auth_plugin='mysql_native_password')
con=mydb.cursor()

def menu():
    while True:
        print("\t\t##############ATTENDANCE RECORD#################")
        print("1. MARK ATTENDANCE")
        print("2. VIEW ATTENDANCE OF A STUDENT")
        print("3. VIEW ATTENDANCE BY DATE")
        print("4. ATTENDANCE PERCENTAGE OF A STUDENT")
        print("5. EXIT TO MAIN MENU")
        print()
        ch=int(input("ENTER CHOICE "))
        print()
        if (ch==1):
            markattendance()
        if (ch==2):
            viewstudent()
        if (ch==3):
            viewbydate()
        if (ch==4):
            percentage()
        if (ch==5):
            mainmenu.mainmenu()
        else:
            print("WHICH OPERATION DO YOU WANT TO PERFORM")

def markattendance():
    sid=int(input("ENTER STUDENT ID "))
    date=input("ENTER DATE (YYYY-MM-DD) or leave blank for today ")
    if date=="":
        date=str(dt.date.today())
    status=input("ENTER STATUS (P/A) ").upper()
    con.execute("insert into attendance values('"+str(sid)+"','"+date+"','"+status+"')")
    mydb.commit()
    print("########ATTENDANCE MARKED#######")

def viewstudent():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("select * from attendance where sid='"+str(sid)+"'")
    for i in con:
        print(i)

def viewbydate():
    date=input("ENTER DATE (YYYY-MM-DD) ")
    con.execute("select * from attendance where adate='"+date+"'")
    for i in con:
        print(i)

def percentage():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("select status from attendance where sid='"+str(sid)+"'")
    rows=con.fetchall()
    if not rows:
        print("NO ATTENDANCE RECORD FOUND")
        return
    total=len(rows)
    present=sum(1 for r in rows if r[0]=='P')
    pct=(present/total)*100
    print(f"ATTENDANCE: {present}/{total}  ({pct:.2f}%)")

