# 🌐 LinguaMitra

An educational app designed to help rural students learn English through their native language — starting with Marathi.

This project uses:
- 🧠 FastAPI + SQLAlchemy for backend APIs
- 📦 SQLite for local development (supports MySQL too)
- 🧪 Pydantic for request validation
- 📘 10 beginner English lessons with flashcards and quizzes

---

## 📁 Project Structure

LinguaMitra/
├── backend.py              # Main FastAPI backend
├── models.py               # SQLAlchemy ORM models
├── pydantic_schemas.py     # Pydantic models for validation
├── seed_all_lessons.py     # Script to populate DB with lessons
├── linguamitra.db          # SQLite DB file (auto-generated)
├── README.md               # Project instructions (this file)

---

## 🚀 Getting Started

### 1. Install Dependencies

Use a virtual environment (recommended):

> python -m venv venv  
> venv\Scripts\activate   # On Windows  
> source venv/bin/activate  # On Mac/Linux

Then install all the required packages:

> pip install fastapi uvicorn sqlalchemy passlib[bcrypt] flet mysql-connector-python

---

### 2. Seed the Database

> python seed_all_lessons.py

This will create `linguamitra.db` and insert lessons, flashcards, and quizzes.

---

### 3. Run the Backend

> python -m uvicorn backend:app --reload

Swagger API docs available at:  
http://127.0.0.1:8000/docs

---


## 🛠 Configuration

- Default database: SQLite  
- If switching to MySQL, update `DATABASE_URL` in both `backend.py` and `seed_all_lessons.py`:

  Example:

  > DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/LinguaMitra"

---

## ✅ Features

- User signup/login with hashed passwords
- Lessons, flashcards, quizzes from DB
- Quiz submission and score tracking
- Leaderboard with XP and rank
- Daily activity log (minutes studied, etc.)
- Swagger UI for testing APIs






