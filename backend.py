from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date
from typing import List

from models import Base, User, Lesson, Flashcard, Question, UserProgress, Language, Translation, ChatbotConversation, Friend, Leaderboard, UserDailyProgress
from pydantic_schemas import UserCreate, UserOut, LessonCreate, LessonOut, FlashcardCreate, QuestionCreate

from passlib.context import CryptContext

# ----------------------------------------------------------------
# Configure Password Hashing
# ----------------------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ----------------------------------------------------------------
# Database Setup: Change DATABASE_URL as required
# ----------------------------------------------------------------
DATABASE_URL = "sqlite:///./linguamitra.db"  # Using SQLite for demonstration

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables (if not already present)
Base.metadata.create_all(bind=engine)

# ----------------------------------------------------------------
# FastAPI App Instance
# ----------------------------------------------------------------
app = FastAPI(title="Linguamitra API")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------------------------------------------
# User Endpoints (Authentication)
# ----------------------------------------------------------------
@app.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hash the password using passlib
    hashed_password = pwd_context.hash(user.password_hash)
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password,
        role=user.role,
        native_language_id=user.native_language_id,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", response_model=UserOut)
def login(email: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user or not pwd_context.verify(password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    # In production, you'd return a token (e.g., JWT)
    return db_user

# Existing User creation endpoint for testing (optional)
@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict(), created_at=datetime.utcnow())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ----------------------------------------------------------------
# Lesson Endpoints
# ----------------------------------------------------------------
@app.post("/lessons/", response_model=LessonOut)
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

@app.get("/lessons/", response_model=List[LessonOut])
def get_lessons(db: Session = Depends(get_db)):
    lessons = db.query(Lesson).all()
    return lessons

# ----------------------------------------------------------------
# Flashcard Endpoints
# ----------------------------------------------------------------
@app.post("/flashcards/", response_model=dict)
def create_flashcard(flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    db_flashcard = Flashcard(**flashcard.dict())
    db.add(db_flashcard)
    db.commit()
    return {"message": "Flashcard added"}

@app.get("/lessons/{lesson_id}/flashcards", response_model=List[FlashcardCreate])
def get_flashcards_for_lesson(lesson_id: int, db: Session = Depends(get_db)):
    flashcards = db.query(Flashcard).filter(Flashcard.lesson_id == lesson_id).all()
    if not flashcards:
        raise HTTPException(status_code=404, detail="No flashcards found for this lesson")
    return flashcards

# ----------------------------------------------------------------
# Quiz Question Endpoints
# ----------------------------------------------------------------
@app.post("/questions/", response_model=dict)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    return {"message": "Question added"}

@app.get("/lessons/{lesson_id}/questions", response_model=List[QuestionCreate])
def get_questions_for_lesson(lesson_id: int, db: Session = Depends(get_db)):
    questions = db.query(Question).filter(Question.lesson_id == lesson_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found for this lesson")
    return questions

# ----------------------------------------------------------------
# Leaderboard Endpoints
# ----------------------------------------------------------------
@app.get("/leaderboard", response_model=List[UserOut])
def get_leaderboard(db: Session = Depends(get_db)):
    leaderboard_entries = db.query(Leaderboard).order_by(Leaderboard.xp_points.desc()).all()
    result = []
    for entry in leaderboard_entries:
        user = db.query(User).filter(User.user_id == entry.user_id).first()
        result.append(user)
    return result

@app.post("/leaderboard/update")
def update_leaderboard(user_id: int, xp_points: int, ranking: int, db: Session = Depends(get_db)):
    entry = db.query(Leaderboard).filter(Leaderboard.user_id == user_id).first()
    if not entry:
        entry = Leaderboard(user_id=user_id, xp_points=xp_points, ranking=ranking)
        db.add(entry)
    else:
        entry.xp_points = xp_points
        entry.ranking = ranking
    db.commit()
    return {"message": "Leaderboard updated"}

# ----------------------------------------------------------------
# Progress Tracking Endpoint
# ----------------------------------------------------------------
@app.post("/progress/update")
def update_progress(user_id: int, lesson_id: int, status: str, score: int, db: Session = Depends(get_db)):
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.lesson_id == lesson_id
    ).first()
    if not progress:
        progress = UserProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            status=status,
            score=score,
            last_accessed=datetime.utcnow()
        )
        db.add(progress)
    else:
        progress.status = status
        progress.score = score
        progress.last_accessed = datetime.utcnow()
    db.commit()
    return {"message": "Progress updated"}

# ----------------------------------------------------------------
# Quiz Submission Endpoint
# ----------------------------------------------------------------
@app.post("/quiz/submit")
def submit_quiz(user_id: int, lesson_id: int, answers: dict, db: Session = Depends(get_db)):
    """
    'answers' is a dict mapping question_id to the submitted answer. For example:
    { "1": "House", "2": "Computer", ... }
    """
    questions = db.query(Question).filter(Question.lesson_id == lesson_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No questions found for this lesson")
    
    score = 0
    total = len(questions)
    for q in questions:
        if str(q.question_id) in answers and answers[str(q.question_id)] == q.correct_answer:
            score += 1

    # Update user progress for the lesson
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.lesson_id == lesson_id
    ).first()
    if not progress:
        progress = UserProgress(
            user_id=user_id,
            lesson_id=lesson_id,
            status="completed" if score == total else "in progress",
            score=score,
            last_accessed=datetime.utcnow()
        )
        db.add(progress)
    else:
        progress.status = "completed" if score == total else "in progress"
        progress.score = score
        progress.last_accessed = datetime.utcnow()
    db.commit()
    return {"message": "Quiz submitted", "score": score, "total": total}

# ----------------------------------------------------------------
# Daily Activity Logging Endpoint
# ----------------------------------------------------------------
@app.post("/daily_activity")
def log_daily_activity(user_id: int, progress_date: date, time_spent: int, studied: bool, db: Session = Depends(get_db)):
    daily = db.query(UserDailyProgress).filter(
        UserDailyProgress.user_id == user_id,
        UserDailyProgress.progress_date == progress_date
    ).first()
    if not daily:
        daily = UserDailyProgress(
            user_id=user_id,
            progress_date=progress_date,
            time_spent=time_spent,
            studied=studied
        )
        db.add(daily)
    else:
        daily.time_spent = time_spent
        daily.studied = studied
    db.commit()
    return {"message": "Daily activity logged"}

# ----------------------------------------------------------------
# Root Endpoint (For Testing)
# ----------------------------------------------------------------
@app.get("/")
def read_root():
    return {"message": "Linguamitra backend is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    # To run the server, use the command: uvicorn backend:app --reload
