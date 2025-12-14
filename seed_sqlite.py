import sqlite3

DB_NAME = "institute.db"

# -----------------------------
# Create / Connect SQLite DB
# -----------------------------
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

print("🔄 Creating SQLite database:", DB_NAME)

# -----------------------------
# Drop tables if already exist
# -----------------------------
cursor.execute("DROP TABLE IF EXISTS courses")
cursor.execute("DROP TABLE IF EXISTS subjects")
cursor.execute("DROP TABLE IF EXISTS exam_results")
cursor.execute("DROP TABLE IF EXISTS timetable")

# -----------------------------
# Create tables
# -----------------------------
cursor.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    subject_name TEXT,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
)
""")

cursor.execute("""
CREATE TABLE exam_results (
    student_id INTEGER,
    subject_id INTEGER,
    marks INTEGER,
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
)
""")

cursor.execute("""
CREATE TABLE timetable (
    course_id INTEGER,
    day TEXT,
    time TEXT,
    subject TEXT,
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
)
""")

print("✅ Tables created")

# -----------------------------
# Insert data
# -----------------------------
courses_data = [
    (1, "BCA", "CSE"),
    (2, "MCA", "CSE"),
    (3, "BSc AI", "AI")
]

subjects_data = [
    (1, "DBMS", 1),
    (2, "OS", 1),
    (3, "ML", 2),
    (4, "DL", 2),
    (5, "AI Basics", 3)
]

exam_results_data = [
    (101, 1, 78),
    (102, 1, 85),
    (103, 3, 92),
    (104, 3, 88),
    (107, 4, 81),
    (108, 4, 90),
    (109, 2, 75),
    (110, 2, 69)
]

timetable_data = [
    (1, "Monday", "10:00", "DBMS"),
    (1, "Wednesday", "12:00", "OS"),
    (2, "Tuesday", "11:00", "ML"),
    (2, "Thursday", "02:00", "DL"),
    (3, "Friday", "09:00", "AI Basics")
]

cursor.executemany("INSERT INTO courses VALUES (?, ?, ?)", courses_data)
cursor.executemany("INSERT INTO subjects VALUES (?, ?, ?)", subjects_data)
cursor.executemany("INSERT INTO exam_results VALUES (?, ?, ?)", exam_results_data)
cursor.executemany("INSERT INTO timetable VALUES (?, ?, ?, ?)", timetable_data)

conn.commit()
conn.close()

print("✅ SQLite database created and data inserted successfully")
print("📁 Database file created:", DB_NAME)


