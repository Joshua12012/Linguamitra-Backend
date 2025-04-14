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

# ================================
# Flet UI (Backend Demo)
# ================================

def main(page: ft.Page):
    page.title = "LinguaMitra - Lesson Backend"
    page.scroll = "adaptive"
    
    # For demonstration, we load Lesson 1.
    lesson_id = 1
    lesson = fetch_lesson(lesson_id)
    flashcards = fetch_flashcards(lesson_id)
    quiz_questions = fetch_quiz_questions(lesson_id)
    match_sets = fetch_match_sets(lesson_id)
    
    # Build UI to display lesson details:
    lesson_title = lesson.get("title", "Lesson not found")
    lesson_content = lesson.get("content", "No content available.")
    
    title_text = ft.Text(lesson_title, size=24, weight="bold")
    content_text = ft.Text(lesson_content, size=18)
    
    # Create controls for flashcards
    flashcard_controls = []
    for fc in flashcards:
        # Each flashcard should have word, sentence, pronunciation, and Marathi translation.
        text = f"{fc['word']}:\n   Sentence: {fc['sentence']}\n   Pronunciation: {fc['pronunciation']}\n   Marathi: {fc['translation']}"
        flashcard_controls.append(ft.Text(text, size=14))
    
    # Create controls for quiz questions
    quiz_controls = []
    for q in quiz_questions:
        text = f"Q: {q['question_text']} | Answer: {q['correct_answer']}"
        quiz_controls.append(ft.Text(text, size=14))
    
    # Create controls for matching sets
    match_controls = []
    for mset in match_sets:
        set_title = mset.get("title", "Match Set")
        items_text = "\n".join([f"{item['left_text']} -> {item['right_text']}" for item in mset.get("items", [])])
        match_controls.append(ft.Text(f"{set_title}:\n{items_text}", size=14))
    
    # Build the page UI
    page.add(
        ft.Column(
            controls=[
                title_text,
                content_text,
                ft.Divider(),
                ft.Text("Flashcards:", weight="bold", size=18),
                *flashcard_controls,
                ft.Divider(),
                ft.Text("Quiz Questions:", weight="bold", size=18),
                *quiz_controls,
                ft.Divider(),
                ft.Text("Matching Sets:", weight="bold", size=18),
                *match_controls
            ],
            spacing=15
        )
    )

# Run the Flet app
ft.app(target=main)
