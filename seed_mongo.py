from pymongo import MongoClient

# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient("mongodb://localhost:27017")
db = client["langgraph_db"]

students_col = db["students"]
faculty_col = db["faculty"]
attendance_col = db["attendance"]

# -----------------------------
# Clear old data (safe for demo)
# -----------------------------
students_col.delete_many({})
faculty_col.delete_many({})
attendance_col.delete_many({})

# -----------------------------
# Faculty Data
# -----------------------------
faculty_data = [
    {
        "faculty_id": 1,
        "name": "Dr. Mehta",
        "department": "AI",
        "subjects": ["ML", "DL"]
    },
    {
        "faculty_id": 2,
        "name": "Prof. Sharma",
        "department": "CSE",
        "subjects": ["DBMS", "OS"]
    }
]

faculty_col.insert_many(faculty_data)

# -----------------------------
# Students Data (15 students)
# -----------------------------
students_data = [
    {"student_id": 101, "name": "Rohit Kumar", "department": "CSE", "year": 3, "hostel_room": "A-101", "fees_status": "pending"},
    {"student_id": 102, "name": "Amit Sharma", "department": "CSE", "year": 3, "hostel_room": "A-102", "fees_status": "paid"},
    {"student_id": 103, "name": "Neha Verma", "department": "AI", "year": 2, "hostel_room": "B-201", "fees_status": "paid"},
    {"student_id": 104, "name": "Pooja Singh", "department": "AI", "year": 2, "hostel_room": "B-202", "fees_status": "pending"},
    {"student_id": 105, "name": "Rahul Patil", "department": "CSE", "year": 1, "hostel_room": "C-301", "fees_status": "paid"},
    {"student_id": 106, "name": "Sneha Joshi", "department": "CSE", "year": 1, "hostel_room": "C-302", "fees_status": "paid"},
    {"student_id": 107, "name": "Ankit Yadav", "department": "AI", "year": 3, "hostel_room": "A-201", "fees_status": "pending"},
    {"student_id": 108, "name": "Kiran Deshmukh", "department": "AI", "year": 3, "hostel_room": "A-202", "fees_status": "paid"},
    {"student_id": 109, "name": "Priya Nair", "department": "CSE", "year": 2, "hostel_room": "B-101", "fees_status": "paid"},
    {"student_id": 110, "name": "Saurabh Kulkarni", "department": "CSE", "year": 2, "hostel_room": "B-102", "fees_status": "pending"},
    {"student_id": 111, "name": "Manish Gupta", "department": "AI", "year": 1, "hostel_room": "C-101", "fees_status": "paid"},
    {"student_id": 112, "name": "Riya Malhotra", "department": "AI", "year": 1, "hostel_room": "C-102", "fees_status": "paid"},
    {"student_id": 113, "name": "Vikas Rao", "department": "CSE", "year": 3, "hostel_room": "A-103", "fees_status": "pending"},
    {"student_id": 114, "name": "Nisha Pandey", "department": "AI", "year": 2, "hostel_room": "B-203", "fees_status": "paid"},
    {"student_id": 115, "name": "Arjun Kapoor", "department": "CSE", "year": 1, "hostel_room": "C-303", "fees_status": "paid"},
]

students_col.insert_many(students_data)

# -----------------------------
# Attendance Data
# -----------------------------
attendance_data = [
    {"student_id": 101, "subject": "DBMS", "attendance_percentage": 72},
    {"student_id": 102, "subject": "DBMS", "attendance_percentage": 88},
    {"student_id": 103, "subject": "ML", "attendance_percentage": 91},
    {"student_id": 104, "subject": "ML", "attendance_percentage": 69},
    {"student_id": 105, "subject": "OS", "attendance_percentage": 80},
    {"student_id": 106, "subject": "OS", "attendance_percentage": 85},
    {"student_id": 107, "subject": "DL", "attendance_percentage": 74},
    {"student_id": 108, "subject": "DL", "attendance_percentage": 90},
]

attendance_col.insert_many(attendance_data)

print("✅ MongoDB seeded successfully!")
print("📌 Collections created: students, faculty, attendance")
