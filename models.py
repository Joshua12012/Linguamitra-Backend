from sqlalchemy import create_engine, Column, Integer, String, Text, Enum, ForeignKey, JSON, Boolean, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Language(Base):
    __tablename__ = 'languages'
    language_id = Column(Integer, primary_key=True)
    language_name = Column(String(50), unique=True, nullable=False)

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum('student', 'teacher'), nullable=False)
    native_language_id = Column(Integer, ForeignKey('languages.language_id'))
    created_at = Column(DateTime)
    native_language = relationship("Language")

class Lesson(Base):
    __tablename__ = 'lessons'
    lesson_id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    language_id = Column(Integer, ForeignKey('languages.language_id'))
    level = Column(Enum('beginner', 'intermediate', 'advanced'), nullable=False)
    lesson_order = Column(Integer)
    language = relationship("Language")

class Flashcard(Base):
    __tablename__ = 'flashcards'
    flashcard_id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    term = Column(String(100), nullable=False)
    pronunciation = Column(String(100))
    sentence = Column(String(255))
    meaning = Column(Text)
    display_order = Column(Integer)
    lesson = relationship("Lesson")

class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    question_text = Column(Text, nullable=False)
    correct_answer = Column(String(255), nullable=False)
    options = Column(JSON, nullable=False)
    lesson = relationship("Lesson")

class UserProgress(Base):
    __tablename__ = 'user_progress'
    progress_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    lesson_id = Column(Integer, ForeignKey('lessons.lesson_id'))
    status = Column(Enum('not started', 'in progress', 'completed'), nullable=False)
    score = Column(Integer, default=0)
    last_accessed = Column(DateTime)
    user = relationship("User")
    lesson = relationship("Lesson")

class UserDailyProgress(Base):
    __tablename__ = 'user_daily_progress'
    daily_progress_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    progress_date = Column(Date, nullable=False)
    time_spent = Column(Integer, default=0)
    studied = Column(Boolean, default=False)
    user = relationship("User")

class Translation(Base):
    __tablename__ = 'translations'
    translation_id = Column(Integer, primary_key=True)
    word = Column(String(100), nullable=False)
    language_id = Column(Integer, ForeignKey('languages.language_id'))
    translation = Column(Text, nullable=False)
    language = relationship("Language")

class ChatbotConversation(Base):
    __tablename__ = 'chatbot_conversations'
    conversation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    conversation_text = Column(Text)
    generated_phone_number = Column(String(20))
    created_at = Column(DateTime)
    user = relationship("User")

class Friend(Base):
    __tablename__ = 'friends'
    friendship_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    friend_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime)
    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])

class Leaderboard(Base):
    __tablename__ = 'leaderboard'
    leaderboard_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    xp_points = Column(Integer, default=0)
    ranking = Column(Integer)
    user = relationship("User")

from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///linguamitra.db")
Base.metadata.create_all(bind=engine)
