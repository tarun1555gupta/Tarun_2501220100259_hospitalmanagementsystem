# Steps to Create — Student Record Management System

This document explains the **logic and reasoning** behind every file in the
project, in the order you would build them from scratch. Follow it top-to-bottom
if you want to recreate the project yourself.

---

## 1. Plan the Database (`school_2026`)

Before writing any Python, decide **what data must be stored**. A school needs:

- **Students** — one row per child (identity, class, section, guardian).
- **Attendance** — one row per student per school day (Present / Absent).
- **Marks** — one row per student per subject per term.
- **Fees** — one row per student per month (Paid / Pending).

This gives four tables inside a single MySQL database named `school_2026`.

| Table       | Key columns                                                  | Why                                          |
|-------------|--------------------------------------------------------------|----------------------------------------------|
| `student`   | sid (PK), sname, class, section, dob, guardian, phone        | Master record for every child.               |
| `attendance`| sid, adate, status                                           | Daily P/A log, linked to student by `sid`.   |
| `marks`     | sid, subject, marks, term                                    | Academic score per subject per term.         |
| `fees`      | sid, amount, fmonth, status                                  | Fee payment ledger per student.              |

The Student ID (`sid`) is the common **foreign concept** used across all tables.

---

## 2. `blank_table.py` — Database bootstrap

**Purpose:** Programmatically create the database and all four empty tables so
the user does not have to type SQL by hand.

**Logic:**
1. Connect to MySQL as `root` **without selecting a database**.
2. `CREATE DATABASE IF NOT EXISTS school_2026`.
3. Reconnect, this time selecting `school_2026`.
4. Run four `CREATE TABLE IF NOT EXISTS` statements for `student`,
   `attendance`, `marks`, `fees`.
5. Commit and close.

Use `IF NOT EXISTS` everywhere so the script is **idempotent** — running it a
second time does not break anything.

---

## 3. `seed_data.sql` — Sample data

**Purpose:** Give the project realistic data to demo without manual entry.

**Logic:**
- `DROP` and re-`CREATE` the database (clean slate).
- Recreate all four tables.
- Insert **100 students** across classes 6–12, sections A/B/C.
- For each student, generate:
  - **10 attendance rows** (roughly 85% Present, 15% Absent).
  - **12 marks rows** (6 subjects × 2 terms: T1 and T2).
  - **3 fee rows** (three consecutive months, mixed Paid/Pending).
- Total: ~100 students, ~1000 attendance, ~1200 marks, ~300 fee rows.

Load with:
```bash
mysql -u root -p < seed_data.sql
```

---

## 4. Common module pattern

Every functional module (`students.py`, `attendance.py`, `marks.py`,
`fees.py`, `graphs.py`) follows the same skeleton:

1. `import mysql.connector` (and `matplotlib` for graphs).
2. Define one function per operation (add / view / update / delete / report).
3. Each function:
   - Opens a MySQL connection.
   - Creates a cursor.
   - Runs the query.
   - Prints results in a readable table format.
   - Commits (for writes) and closes the connection.
4. A `while True` menu at the bottom that dispatches to the right function
   based on the user's choice; last option `return`s to `mainmenu.py`.

This keeps each file **independent** and easy to debug in isolation.

---

## 5. `students.py` — Student Details

CRUD operations on the `student` table:
- **Insert** a new student — collect fields, `INSERT INTO student`.
- **Delete** by `sid` — `DELETE FROM student WHERE sid=…`.
- **Search** by `sid` or name (`LIKE`).
- **Update** class/section — `UPDATE student SET … WHERE sid=…`.
- **List all** — `SELECT * FROM student` and pretty-print.

---

## 6. `attendance.py` — Attendance Record

- **Mark attendance:** ask for `sid`, date, status — `INSERT INTO attendance`.
- **View by student:** `SELECT … WHERE sid=…`.
- **View by date:** `SELECT … WHERE adate=…`.
- **Attendance percentage:** count `P` rows / total rows × 100 for one student.

The percentage calculation is the key "logic" here — everything else is CRUD.

---

## 7. `marks.py` — Marks / Grades

- **Insert marks** per subject/term.
- **View marks** of a student.
- **Class topper by subject** — `SELECT max(marks) … WHERE subject=…` joined
  with `student` to print the top scorer's name.
- **Grade calculator** — compute average of a student's marks and map:
  - `>=90` → A+, `>=75` → A, `>=60` → B, `>=45` → C, `>=33` → D, else F.

The grade mapping is the "business rule" of this module.

---

## 8. `fees.py` — Fee Records

- **Record payment** — insert a row with `status='PAID'`.
- **View history** for a student.
- **Pending list** — `SELECT … WHERE status='PENDING'`.
- **Collection summary** — `SELECT sum(amount) WHERE status='PAID'` grouped by
  month for a quick revenue snapshot.

---

## 9. `graphs.py` — Performance Graphs

Uses **matplotlib** to visualize the same data:
- **Bar chart:** average marks per class (`GROUP BY class`).
- **Bar chart:** attendance % per student.
- **Pie chart:** distribution of fee status (Paid vs Pending).

Each graph pulls its data with a single SQL query, feeds it into
`plt.bar` / `plt.pie`, and calls `plt.show()`.

---

## 10. `mainmenu.py` — The entry point

**Purpose:** The single file the user runs. Everything else is invoked from
here.

**Logic:**
1. Print a banner and a numbered menu (1–6).
2. Read the user's choice.
3. Dispatch to the right module inside a `try / except`:
   - On success, the sub-module runs and eventually returns.
   - On any exception, print **what went wrong and why** (exception type +
     message), sleep 3 seconds, and **restart the main menu** automatically.
4. Option `6` cleanly exits.

The `try/except` + auto-restart is what makes the app robust: a MySQL outage or
a bad input in one module never crashes the whole program.

The file ends with:
```python
if __name__ == "__main__":
    mainmenu()
```
so it can be launched directly from the shell.

---

## 11. Order of creation (recommended)

1. `blank_table.py` — make sure the DB exists.
2. `seed_data.sql` — load sample data so later modules have something to show.
3. `students.py` — everything else depends on students existing.
4. `attendance.py`, `marks.py`, `fees.py` — in any order.
5. `graphs.py` — needs the other tables populated.
6. `mainmenu.py` — glue everything together last.
7. `README.md` and this `StepToCreate.md` — document the finished project.

---

_Created for SRM CEM Lucknow._
