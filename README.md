# Student Record Management System

A menu-driven **Python + MySQL** project to manage students in a school. Modeled after a classic CBSE-style CS project: multiple modules, a main menu, MySQL persistence, and matplotlib-powered charts.

---

## Feartures

The system exposes **four core functionalities** plus a graphing module:

1. **Student Details (`students.py`)**
   - Insert, delete, search, update (class/section), and list all students.
2. **Attendance Record (`attendance.py`)**
   - Mark daily attendance (P/A), view by student, view by date, and compute **attendance percentage**.
3. **Marks / Grades (`marks.py`)**
   - Insert marks per subject/term, view a student's marks, find **class topper by subject**, compute **average and letter grade** (A+ / A / B / C / D / F).
4. **Fee Records (`fees.py`)**
   - Record fee payments, view fee history, list students with **pending fees**, and print a **total collection summary**.
5. **Performance Graphs (`graphs.py`)**
   - Average marks per class (bar), attendance % per student (bar), fee status distribution (pie).

---

## Project Structure

```
student_record_management/
├── mainmenu.py       # Entry point – shows the main menu
├── students.py             # Student details module
├── attendance.py             # Attendance module
├── marks.py             # Marks / grades module
├── fees.py             # Fee records module
├── graphs.py             # Graphs module (matplotlib)
├── blank_table.py    # Creates DB + empty tables programmatically
├── seed_data.sql     # 100 sample students + attendance + marks + fees
└── README.md
```

---

## Database Schema (`school_2026`)

| Table       | Columns                                                                 |
|-------------|-------------------------------------------------------------------------|
| `student`   | sid (PK), sname, class, section, dob, guardian, phone                   |
| `attendance`| sid, adate, status (`P`/`A`)                                            |
| `marks`     | sid, subject, marks, term (`T1`/`T2`/`FINAL`)                           |
| `fees`      | sid, amount, fmonth (e.g. `JUL-2026`), status (`PAID`/`PENDING`)        |

---

## Sample Data Included

`seed_data.sql` seeds the database with realistic dummy data:

- **100 students** across classes 6–12 (sections A/B/C).
- **~1000 attendance rows** – 10 school days per student, ~85% present.
- **~1200 marks rows** – 6 subjects × 2 terms per student.
- **300 fee rows** – 3 months per student, mix of PAID/PENDING.

---

## Requirements

- Python 3.8+
- MySQL 5.7+ / MariaDB running on `localhost`
- Python packages:
  ```bash
  pip install mysql-connector-python matplotlib
  ```

Default connection used in the code:
```
host=localhost  user=root  password=""  database=school_2026
```
Update credentials in each module and `blank_table.py` if your MySQL setup differs.

---

## Setup

**Option A — using the SQL seed (recommended):**
```bash
mysql -u root -p < seed_data.sql
```

**Option B — create empty tables from Python:**
```bash
python blank_table.py
```

---

## Run

```bash
python mainmenu.py
```

You will see:

```
*****************STUDENT RECORD MANAGEMENT SYSTEM - MAIN MENU*****************
    1. STUDENT DETAILS
    2. ATTENDANCE RECORD
    3. MARKS / GRADES
    4. FEE RECORDS
    5. SHOW PERFORMANCE GRAPH
    6. EXIT
```

Pick a module, follow the prompts. Choosing the last option in any submodule returns you to the main menu.

---

## Example Walk-through

1. Launch: `python mainmenu.py`
2. Enter `2` → Attendance → `4` → enter `SID = 5` → prints e.g. `ATTENDANCE: 9/10 (90.00%)`.
3. Back to main menu → `3` → Marks → `3` → subject `Math`, term `T1` → prints class topper.
4. Main menu → `4` → Fees → `3` → lists every student with pending dues.
5. Main menu → `5` → `1` → bar chart of average marks per class opens in a matplotlib window.

---

## Notes

- SQL statements use straightforward string formatting to match the classroom-project style; in production, use **parameterized queries** to prevent SQL injection.
- All modules import `mainmenu` to bounce back to the main screen — do not rename `mainmenu.py`.
- Charts require a working GUI backend for matplotlib; on headless servers use `matplotlib.use('Agg')` and save figures instead.

---

_Created for SRM CEM Lucknow._
