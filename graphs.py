import mysql.connector
import matplotlib.pyplot as plt
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", database="school_2026", auth_plugin='mysql_native_password')
con=mydb.cursor()

def show_graph():
    print("\t\t##############PERFORMANCE GRAPH#################")
    print("1. AVERAGE MARKS PER CLASS")
    print("2. ATTENDANCE % PER STUDENT")
    print("3. FEE STATUS PIE CHART")
    ch=int(input("ENTER CHOICE "))
    if ch==1:
        con.execute("select s.class, avg(m.marks) from student s join marks m on s.sid=m.sid group by s.class")
        rows=con.fetchall()
        classes=[r[0] for r in rows]
        avgs=[float(r[1]) for r in rows]
        plt.bar(classes, avgs, color='steelblue')
        plt.xlabel("Class"); plt.ylabel("Average Marks"); plt.title("Average Marks per Class")
        plt.show()
    elif ch==2:
        con.execute("select sid, sum(status='P')/count(*)*100 from attendance group by sid")
        rows=con.fetchall()
        sids=[str(r[0]) for r in rows]
        pcts=[float(r[1]) for r in rows]
        plt.bar(sids, pcts, color='seagreen')
        plt.xlabel("Student ID"); plt.ylabel("Attendance %"); plt.title("Attendance % per Student")
        plt.show()
    elif ch==3:
        con.execute("select status, sum(amount) from fees group by status")
        rows=con.fetchall()
        labels=[r[0] for r in rows]
        vals=[float(r[1]) for r in rows]
        plt.pie(vals, labels=labels, autopct='%1.1f%%')
        plt.title("Fee Status Distribution")
        plt.show()
