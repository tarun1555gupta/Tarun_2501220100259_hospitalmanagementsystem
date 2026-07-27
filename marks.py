import mysql.connector
import mainmenu
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="school_2026", auth_plugin='mysql_native_password')
con=mydb.cursor()

def menu():
    while True:
        print("\t\t##############MARKS / GRADES#################")
        print("1. INSERT MARKS")
        print("2. VIEW MARKS OF A STUDENT")
        print("3. CLASS TOPPER BY SUBJECT")
        print("4. AVERAGE & GRADE OF A STUDENT")
        print("5. EXIT TO MAIN MENU")
        print()
        ch=int(input("ENTER CHOICE "))
        print()
        if (ch==1):
            insertmarks()
        if (ch==2):
            viewmarks()
        if (ch==3):
            topper()
        if (ch==4):
            averagegrade()
        if (ch==5):
            mainmenu.mainmenu()
        else:
            print("WHICH OPERATION DO YOU WANT TO PERFORM")

def insertmarks():
    sid=int(input("ENTER STUDENT ID "))
    subject=input("ENTER SUBJECT ")
    marks=int(input("ENTER MARKS (OUT OF 100) "))
    term=input("ENTER TERM (T1/T2/FINAL) ")
    con.execute("insert into marks values('"+str(sid)+"','"+subject+"','"+str(marks)+"','"+term+"')")
    mydb.commit()
    print("########MARKS INSERTED#######")

def viewmarks():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("select * from marks where sid='"+str(sid)+"'")
    for i in con:
        print(i)

def topper():
    subject=input("ENTER SUBJECT ")
    term=input("ENTER TERM (T1/T2/FINAL) ")
    con.execute("select m.sid, s.sname, m.marks from marks m join student s on m.sid=s.sid where subject='"+subject+"' and term='"+term+"' order by marks desc limit 1")
    row=con.fetchone()
    if row:
        print(f"TOPPER IN {subject} ({term}): SID={row[0]}, NAME={row[1]}, MARKS={row[2]}")
    else:
        print("NO RECORDS FOUND")

def averagegrade():
    sid=int(input("ENTER STUDENT ID "))
    term=input("ENTER TERM (T1/T2/FINAL) ")
    con.execute("select marks from marks where sid='"+str(sid)+"' and term='"+term+"'")
    rows=con.fetchall()
    if not rows:
        print("NO MARKS FOUND")
        return
    avg=sum(r[0] for r in rows)/len(rows)
    if avg>=90: grade='A+'
    elif avg>=80: grade='A'
    elif avg>=70: grade='B'
    elif avg>=60: grade='C'
    elif avg>=40: grade='D'
    else: grade='F'
    print(f"AVERAGE: {avg:.2f}   GRADE: {grade}")
