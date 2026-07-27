# Output Reference — Function Behaviour & Sample Output

This document lists every function in the project, what it is supposed to do,
and a sample of what you should see on screen when it runs.

Sample data assumes `seed_data.sql` has been loaded (100 students, IDs 1–100).

---

## `mainmenu.py`

### `mainmenu()`
**Does:** Prints the main menu and dispatches to a module. Wraps each call in
`try/except` — on any error it prints the reason and auto-restarts after 3s.

**Example:**
```
*****************STUDENT RECORD MANAGEMENT SYSTEM - MAIN MENU*****************
    1. STUDENT DETAILS
    2. ATTENDANCE RECORD
    3. MARKS / GRADES
    4. FEE RECORDS
    5. SHOW PERFORMANCE GRAPH
    6. EXIT
ENTER YOUR CHOICE: 1
```

**On error:**
```
!! ERROR IN MODULE: ProgrammingError
   REASON: 1146 (42S02): Table 'school_2026.student' doesn't exist
   RESTARTING IN 3 SECONDS...
```

---

## `students.py`

### `insertstudent()`
**Does:** Adds a new row to the `student` table.

**Example:**
```
ENTER STUDENT ID 101
ENTER STUDENT NAME Aarav Sharma
ENTER CLASS 10
ENTER SECTION A
ENTER DATE OF BIRTH (YYYY-MM-DD) 2010-05-14
ENTER GUARDIAN NAME Rakesh Sharma
ENTER PHONE NUMBER 9876543210
########STUDENT DETAILS INSERTED SUCCESSFULLY#######
```

### `deletestudent()`
**Does:** Removes a student by `sid`.

**Example:**
```
ENTER STUDENT ID 101
########STUDENT DELETED#######
```

### `search()`
**Does:** Prints the row of a single student.

**Example:**
```
ENTER STUDENT ID 5
(5, 'Priya Verma', '8', 'B', datetime.date(2012, 3, 22), 'Suresh Verma', '9812345670')
```

### `updatestudent()`
**Does:** Updates class and section for a student.

**Example:**
```
ENTER STUDENT ID 5
ENTER NEW CLASS 9
ENTER NEW SECTION A
########STUDENT UPDATED#######
```

### `displayall()`
**Does:** Lists every student in the table.

**Example (truncated):**
```
(1, 'Aarav Kumar', '6', 'A', ...)
(2, 'Ishaan Singh', '6', 'B', ...)
(3, 'Riya Gupta', '7', 'A', ...)
...
```

---

## `attendance.py`

### `markattendance()`
**Does:** Inserts a P/A record for a student on a given date.

**Example:**
```
ENTER STUDENT ID 5
ENTER DATE (YYYY-MM-DD) 2026-07-24
ENTER STATUS (P/A) P
########ATTENDANCE MARKED#######
```

### `viewbystudent()`
**Does:** Shows every attendance row of one student.

**Example:**
```
ENTER STUDENT ID 5
(5, datetime.date(2026, 7, 15), 'P')
(5, datetime.date(2026, 7, 16), 'P')
(5, datetime.date(2026, 7, 17), 'A')
...
```

### `viewbydate()`
**Does:** Shows every student's status for a given date.

**Example:**
```
ENTER DATE (YYYY-MM-DD) 2026-07-16
(1, datetime.date(2026, 7, 16), 'P')
(2, datetime.date(2026, 7, 16), 'A')
(3, datetime.date(2026, 7, 16), 'P')
...
```

### `attendancepercent()`
**Does:** Computes attendance % = (Present days / Total days) × 100.

**Example:**
```
ENTER STUDENT ID 5
ATTENDANCE: 9/10 (90.00%)
```

---

## `marks.py`

### `insertmarks()`
**Does:** Adds a mark row for a subject/term.

**Example:**
```
ENTER STUDENT ID 5
ENTER SUBJECT Math
ENTER MARKS 87
ENTER TERM (T1/T2/FINAL) T1
########MARKS INSERTED#######
```

### `viewmarks()`
**Does:** Lists every subject/term mark of a student.

**Example:**
```
ENTER STUDENT ID 5
('Math', 87, 'T1')
('Science', 78, 'T1')
('English', 82, 'T1')
('Math', 91, 'T2')
...
```

### `topper()`
**Does:** Prints the class topper for a subject in a given term.

**Example:**
```
ENTER SUBJECT Math
ENTER TERM (T1/T2/FINAL) T1
TOPPER: Priya Verma (SID 5) - 98
```

### `grade()`
**Does:** Averages a student's marks and returns a letter grade.

Grading logic:
`>=90 A+`, `>=75 A`, `>=60 B`, `>=45 C`, `>=33 D`, `<33 F`.

**Example:**
```
ENTER STUDENT ID 5
AVERAGE MARKS: 82.50
GRADE: A
```

---

## `fees.py`

### `recordpayment()`
**Does:** Inserts a fee row marked PAID.

**Example:**
```
ENTER STUDENT ID 5
ENTER AMOUNT 2500
ENTER MONTH (e.g. JUL-2026) JUL-2026
########FEE PAYMENT RECORDED#######
```

### `viewfees()`
**Does:** Shows every fee row of a student.

**Example:**
```
ENTER STUDENT ID 5
(5, 2500, 'MAY-2026', 'PAID')
(5, 2500, 'JUN-2026', 'PAID')
(5, 2500, 'JUL-2026', 'PENDING')
```

### `pendinglist()`
**Does:** Lists all students with PENDING dues.

**Example:**
```
(5, 'Priya Verma', 2500, 'JUL-2026')
(12, 'Rohan Das', 2500, 'JUL-2026')
(27, 'Neha Iyer', 2500, 'JUN-2026')
...
```

### `collectionsummary()`
**Does:** Sums all PAID amounts grouped by month.

**Example:**
```
MAY-2026 : 235000
JUN-2026 : 240000
JUL-2026 : 187500
TOTAL COLLECTION: 662500
```

---

## `graphs.py`

### `avgmarksperclass()`
**Does:** Bar chart of average marks for each class (6–12).

**Example (window opens):**
```
X-axis: Class 6, 7, 8, 9, 10, 11, 12
Y-axis: Average marks (e.g. 72, 68, 75, 70, 78, 74, 80)
```

### `attendancechart()`
**Does:** Bar chart of attendance % per student.

**Example (window opens):**
```
X-axis: SID 1..100
Y-axis: Attendance % (0-100)
```

### `feestatuschart()`
**Does:** Pie chart showing share of PAID vs PENDING fees.

**Example (window opens):**
```
PAID    - 68%
PENDING - 32%
```

---

## `blank_table.py`

### `createtables()` (script body)
**Does:** Creates database `school_2026` and the four empty tables
(`student`, `attendance`, `marks`, `fees`). Idempotent — safe to re-run.

**Example:**
```
$ python blank_table.py
DATABASE school_2026 READY
TABLE student CREATED
TABLE attendance CREATED
TABLE marks CREATED
TABLE fees CREATED
```

---

_Created for SRM CEM Lucknow._
