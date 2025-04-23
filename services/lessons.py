import flet as ft
import mysql.connector
from mysql.connector import Error

# ================================
# Database Functions
# ================================

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Update if needed
            user="your_username",      # Replace with your MySQL user
            password="your_password",  # Replace with your MySQL password
            database="LinguaMitra"     # Your database name
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None

def fetch_lesson(lesson_id):
    conn = get_db_connection()
    lesson = {}
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM lessons WHERE lesson_id = %s"
        cursor.execute(query, (lesson_id,))
        lesson = cursor.fetchone()
        conn.close()
    return lesson

def fetch_flashcards(lesson_id):
    conn = get_db_connection()
    flashcards = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM flashcards WHERE lesson_id = %s"
        cursor.execute(query, (lesson_id,))
        flashcards = cursor.fetchall()
        conn.close()
    return flashcards

def fetch_quiz_questions(lesson_id):
    conn = get_db_connection()
    questions = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM questions WHERE lesson_id = %s"
        cursor.execute(query, (lesson_id,))
        questions = cursor.fetchall()
        conn.close()
    return questions

def fetch_match_sets(lesson_id):
    conn = get_db_connection()
    match_sets = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM match_sets WHERE lesson_id = %s"
        cursor.execute(query, (lesson_id,))
        match_sets = cursor.fetchall()
        # For each match_set, get items
        for mset in match_sets:
            set_id = mset["match_set_id"]
            cursor.execute("SELECT * FROM match_items WHERE match_set_id = %s", (set_id,))
            items = cursor.fetchall()
            mset["items"] = items
        conn.close()
    return match_sets