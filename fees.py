import mysql.connector
import mainmenu
mydb=mysql.connector.connect(host="localhost",
                             user="root", passwd="", database="school_2026",
                             auth_plugin='mysql_native_password')
con=mydb.cursor()

def menu():
    while True:
        print("\t\t##############FEE RECORDS#################")
        print("1. INSERT FEE PAYMENT")
        print("2. VIEW FEE HISTORY OF A STUDENT")
        print("3. LIST UNPAID / PENDING STUDENTS")
        print("4. TOTAL COLLECTION SUMMARY")
        print("5. EXIT TO MAIN MENU")
        print()
        ch=int(input("ENTER CHOICE "))
        print()
        if (ch==1):
            insertfee()
        if (ch==2):
            viewfee()
        if (ch==3):
            pending()
        if (ch==4):
            summary()
        if (ch==5):
            mainmenu.mainmenu()
        else:
            print("WHICH OPERATION DO YOU WANT TO PERFORM")

def insertfee():
    sid=int(input("ENTER STUDENT ID "))
    amount=int(input("ENTER AMOUNT "))
    month=input("ENTER MONTH (e.g. JAN-2026) ")
    status=input("ENTER STATUS (PAID/PENDING) ").upper()
    con.execute("insert into fees values('"+str(sid)+"','"+str(amount)+"','"+month+"','"+status+"')")
    mydb.commit()
    print("########FEE RECORD ADDED#######")

def viewfee():
    sid=int(input("ENTER STUDENT ID "))
    con.execute("select * from fees where sid='"+str(sid)+"'")
    for i in con:
        print(i)

def pending():
    con.execute("select f.sid, s.sname, f.amount, f.fmonth from fees f join student s on f.sid=s.sid where f.status='PENDING'")
    rows=con.fetchall()
    if not rows:
        print("NO PENDING FEES")
        return
    print("PENDING FEES:")
    for r in rows:
        print(r)

def summary():
    con.execute("select sum(amount) from fees where status='PAID'")
    paid=con.fetchone()[0] or 0
    con.execute("select sum(amount) from fees where status='PENDING'")
    pend=con.fetchone()[0] or 0
    print(f"TOTAL COLLECTED : {paid}")
    print(f"TOTAL PENDING   : {pend}")
    print(f"GRAND TOTAL     : {paid+pend}")
