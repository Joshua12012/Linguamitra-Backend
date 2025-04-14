from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password_hash: str
    role: str
    native_language_id: Optional[int]

class UserOut(BaseModel):
    user_id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True

class LessonCreate(BaseModel):
    title: str
    content: str
    language_id: int
    level: str
    lesson_order: Optional[int] = 1

class LessonOut(BaseModel):
    lesson_id: int
    title: str
    content: str
    level: str

    class Config:
        orm_mode = True

class FlashcardCreate(BaseModel):
    lesson_id: int
    term: str
    pronunciation: Optional[str]
    sentence: Optional[str]
    meaning: str
    display_order: Optional[int]

class QuestionCreate(BaseModel):
    lesson_id: int
    question_text: str
    correct_answer: str
    options: dict
