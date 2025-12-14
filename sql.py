import sqlite3

DB_PATH = "institute.db"

def get_connection():
    return sqlite3.connect(DB_PATH)


def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_subjects_by_course(course_name):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT subjects.subject_name
    FROM subjects
    JOIN courses ON subjects.course_id = courses.course_id
    WHERE courses.course_name = ?
    """
    cursor.execute(query, (course_name,))
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_top_scorers(min_marks=85):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT exam_results.student_id, subjects.subject_name, exam_results.marks
    FROM exam_results
    JOIN subjects ON exam_results.subject_id = subjects.subject_id
    WHERE exam_results.marks >= ?
    ORDER BY exam_results.marks DESC
    """
    cursor.execute(query, (min_marks,))
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_student_marks(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT subjects.subject_name, exam_results.marks
    FROM exam_results
    JOIN subjects ON exam_results.subject_id = subjects.subject_id
    WHERE exam_results.student_id = ?
    """
    cursor.execute(query, (student_id,))
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_timetable_for_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT day, time, subject FROM timetable WHERE course_id = ?",
        (course_id,)
    )
    rows = cursor.fetchall()

    conn.close()
    return rows
