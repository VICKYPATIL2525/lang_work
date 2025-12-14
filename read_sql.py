import sqlite3

DB_NAME = "institute.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

print("\n📌 COURSES")
for row in cursor.execute("SELECT * FROM courses"):
    print(row)

print("\n📌 SUBJECTS")
for row in cursor.execute("SELECT * FROM subjects"):
    print(row)

print("\n📌 EXAM RESULTS")
for row in cursor.execute("""
SELECT exam_results.student_id, subjects.subject_name, exam_results.marks
FROM exam_results
JOIN subjects ON exam_results.subject_id = subjects.subject_id
"""):
    print(row)

print("\n📌 TIMETABLE")
for row in cursor.execute("SELECT * FROM timetable"):
    print(row)

conn.close()
print("\n✅ All records displayed successfully")
