import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="", auth_plugin='mysql_native_password')
con=mydb.cursor()

con.execute("CREATE DATABASE IF NOT EXISTS school_2026")
con.execute("USE school_2026")

con.execute("""CREATE TABLE IF NOT EXISTS student(
    sid INT PRIMARY KEY,
    sname VARCHAR(60),
    class VARCHAR(10),
    section VARCHAR(5),
    dob DATE,
    guardian VARCHAR(60),
    phone VARCHAR(15)
)""")

con.execute("""CREATE TABLE IF NOT EXISTS attendance(
    sid INT,
    adate DATE,
    status CHAR(1)
)""")

con.execute("""CREATE TABLE IF NOT EXISTS marks(
    sid INT,
    subject VARCHAR(30),
    marks INT,
    term VARCHAR(10)
)""")

con.execute("""CREATE TABLE IF NOT EXISTS fees(
    sid INT,
    amount INT,
    fmonth VARCHAR(15),
    status VARCHAR(10)
)""")

mydb.commit()
print("ALL TABLES CREATED IN DATABASE school_2026")
