import os
import csv
import json
import sqlite3

# ================================
# Create Data Directory
# ================================
DATA_DIR = "student_data_sources"
os.makedirs(DATA_DIR, exist_ok=True)


# ================================
# 1) CSV FILE — basic_student_info.csv
# ================================
csv_path = os.path.join(DATA_DIR, "basic_student_info.csv")

csv_data = [
    [1, "Vicky Patil",  "vicky.p@example.com",  "CS",  "M"],
    [2, "Anita Sharma", "anita.s@example.com",  "BCA", "F"],
    [3, "Rohit Kumar",  "rohit.k@example.com",  "CS",  "M"],
    [4, "Priya Desai",  "priya.d@example.com",  "BBA", "F"],
    [5, "Karan Mehta",  "karan.m@example.com",  "MCA", "M"],
    [6, "Sneha Joshi",  "sneha.j@example.com",  "CS",  "F"],
    [7, "Arjun Singh",  "arjun.s@example.com",  "BCA", "M"],
    [8, "Muskan Patel", "muskan.p@example.com", "IMCA","F"],
    [9, "Neeraj Verma", "neeraj.v@example.com", "MCA", "M"],
    [10, "Kavita More", "kavita.m@example.com", "CS",  "F"]
]

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email", "department", "gender"])
    writer.writerows(csv_data)

print(f"[✔] CSV created: {csv_path}")


# ================================
# 2) JSON FILE — hostel_contact_info.json
# ================================
hostel_json_path = os.path.join(DATA_DIR, "hostel_contact_info.json")

hostel_data = {
    "hostel_contact_info": [
        {"id": 1, "room": "A101", "phone": "9991110001", "warden": "Mr. Suresh"},
        {"id": 2, "room": "B203", "phone": "9991110002", "warden": "Mrs. Rekha"},
        {"id": 3, "room": "C110", "phone": "9991110003", "warden": "Mr. Suresh"},
        {"id": 4, "room": "A202", "phone": "9991110004", "warden": "Mrs. Rekha"},
        {"id": 5, "room": "D305", "phone": "9991110005", "warden": "Mr. Suresh"},
        {"id": 6, "room": "A118", "phone": "9991110006", "warden": "Mrs. Rekha"},
        {"id": 7, "room": "B109", "phone": "9991110007", "warden": "Mr. Suresh"},
        {"id": 8, "room": "C207", "phone": "9991110008", "warden": "Mrs. Rekha"},
        {"id": 9, "room": "D404", "phone": "9991110009", "warden": "Mr. Suresh"},
        {"id": 10, "room": "A310", "phone": "9991110010", "warden": "Mrs. Rekha"}
    ]
}

with open(hostel_json_path, "w") as f:
    json.dump(hostel_data, f, indent=2)

print(f"[✔] JSON created: {hostel_json_path}")


# ================================
# 3) SQLite DB — academic_details.sqlite
# ================================
sqlite_path = os.path.join(DATA_DIR, "academic_details.sqlite")

conn = sqlite3.connect(sqlite_path)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS academic_records;")

cur.execute("""
CREATE TABLE academic_records (
    id INTEGER PRIMARY KEY,
    attendance INTEGER,
    semester INTEGER,
    marks_internal INTEGER,
    marks_external INTEGER,
    total_marks INTEGER,
    result_status TEXT
);
""")

sqlite_rows = [
    (1,  88, 5, 28, 55, 83, "Pass"),
    (2,  76, 3, 25, 42, 67, "Pass"),
    (3,  92, 5, 30, 58, 88, "Pass"),
    (4,  81, 2, 23, 40, 63, "Pass"),
    (5,  69, 4, 20, 37, 57, "Pass"),
    (6,  95, 6, 30, 60, 90, "Pass"),
    (7,  72, 3, 22, 39, 61, "Pass"),
    (8,  84, 5, 27, 50, 77, "Pass"),
    (9,  63, 4, 18, 32, 50, "Pass"),
    (10, 90, 6, 29, 59, 88, "Pass")
]

cur.executemany("INSERT INTO academic_records VALUES (?, ?, ?, ?, ?, ?, ?);", sqlite_rows)

conn.commit()
conn.close()

print(f"[✔] SQLite DB created: {sqlite_path}")


# ================================
# 4) MongoDB Simulated JSON — student_financial_library_info.json
# ================================
mongo_json_path = os.path.join(DATA_DIR, "student_financial_library_info.json")

mongo_data = {
    "student_financial_library_info": [
        {"id": 1, "fees_paid": 40000, "fees_due": 5000, "library_fine": 0, "disciplinary_action": "None"},
        {"id": 2, "fees_paid": 35000, "fees_due": 10000, "library_fine": 20, "disciplinary_action": "None"},
        {"id": 3, "fees_paid": 45000, "fees_due": 0, "library_fine": 10, "disciplinary_action": "None"},
        {"id": 4, "fees_paid": 30000, "fees_due": 15000, "library_fine": 0, "disciplinary_action": "Warning issued"},
        {"id": 5, "fees_paid": 42000, "fees_due": 2000, "library_fine": 5, "disciplinary_action": "None"},
        {"id": 6, "fees_paid": 46000, "fees_due": 0, "library_fine": 0, "disciplinary_action": "None"},
        {"id": 7, "fees_paid": 28000, "fees_due": 18000, "library_fine": 15, "disciplinary_action": "None"},
        {"id": 8, "fees_paid": 39000, "fees_due": 6000, "library_fine": 0, "disciplinary_action": "None"},
        {"id": 9, "fees_paid": 41000, "fees_due": 4000, "library_fine": 25, "disciplinary_action": "None"},
        {"id": 10, "fees_paid": 47000, "fees_due": 0, "library_fine": 0, "disciplinary_action": "None"}
    ]
}

with open(mongo_json_path, "w") as f:
    json.dump(mongo_data, f, indent=2)

print(f"[✔] Mongo JSON created: {mongo_json_path}")


print("\n🎉 ALL DATA SOURCES GENERATED SUCCESSFULLY!")
print(f"📁 Folder: {DATA_DIR}")
