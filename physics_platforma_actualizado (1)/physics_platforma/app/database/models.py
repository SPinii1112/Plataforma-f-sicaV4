from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy import (
    String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.engine import Base

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(String(120), unique=True, nullable=True)
    current_year: Mapped[int] = mapped_column(Integer, nullable=False, default=5) # 5 o 6
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="student") # student, teacher, admin
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relaciones
    periods: Mapped[List["AcademicPeriod"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    attempts: Mapped[List["Attempt"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    progress: Mapped[List["TopicProgress"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    masteries: Mapped[List["ConceptMastery"]] = relationship(back_populates="user", cascade="all, delete-orphan")

class AcademicPeriod(Base):
    __tablename__ = "academic_periods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    year_level: Mapped[int] = mapped_column(Integer, nullable=False) # 5 o 6
    calendar_year: Mapped[int] = mapped_column(Integer, nullable=False) # 2025, 2026...
    status: Mapped[str] = mapped_column(String(20), default="active") # active, completed
    final_progress: Mapped[float] = mapped_column(Float, default=0.0) # 0 a 100%
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship(back_populates="periods")
    attempts: Mapped[List["Attempt"]] = relationship(back_populates="period")
    progress: Mapped[List["TopicProgress"]] = relationship(back_populates="period")

class Module(Base):
    __tablename__ = "modules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    year_level: Mapped[int] = mapped_column(Integer, index=True, nullable=False) # 5 o 6
    slug: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")
    order_index: Mapped[int] = mapped_column(Integer, default=1)
    icon: Mapped[str] = mapped_column(String(40), default="book")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    topics: Mapped[List["Topic"]] = relationship(back_populates="module", cascade="all, delete-orphan", order_by="Topic.order_index")

class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    module_id: Mapped[int] = mapped_column(Integer, ForeignKey("modules.id", ondelete="CASCADE"), nullable=False)
    slug: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    summary: Mapped[str] = mapped_column(Text, default="")
    content_file: Mapped[str] = mapped_column(String(255), default="")
    theory_content: Mapped[str] = mapped_column(Text, default="")
    order_index: Mapped[int] = mapped_column(Integer, default=1)
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=20)

    module: Mapped["Module"] = relationship(back_populates="topics")
    concepts: Mapped[List["Concept"]] = relationship(back_populates="topic", cascade="all, delete-orphan")
    exercises: Mapped[List["Exercise"]] = relationship(back_populates="topic", cascade="all, delete-orphan")
    progress: Mapped[List["TopicProgress"]] = relationship(back_populates="topic")

class Concept(Base):
    __tablename__ = "concepts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, default="")

    topic: Mapped["Topic"] = relationship(back_populates="concepts")
    masteries: Mapped[List["ConceptMastery"]] = relationship(back_populates="concept")

class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    exercise_type: Mapped[str] = mapped_column(String(30), default="multiple_choice") # numeric, multiple_choice
    difficulty: Mapped[str] = mapped_column(String(20), default="intermediate") # basic, intermediate, advanced
    statement: Mapped[str] = mapped_column(Text, nullable=False)
    given_data: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    options: Mapped[Optional[list]] = mapped_column(JSON, nullable=True) # Para multiple choice
    correct_answer: Mapped[str] = mapped_column(String(255), nullable=False)
    tolerance: Mapped[float] = mapped_column(Float, default=0.02) # Margen de error en numeros (+-2%)
    solution_steps: Mapped[str] = mapped_column(Text, default="")
    explanation: Mapped[str] = mapped_column(Text, default="")
    common_errors: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    elo_rating: Mapped[float] = mapped_column(Float, default=1200.0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    topic: Mapped["Topic"] = relationship(back_populates="exercises")
    attempts: Mapped[List["Attempt"]] = relationship(back_populates="exercise")
    concepts: Mapped[List["ExerciseConcept"]] = relationship(back_populates="exercise", cascade="all, delete-orphan")

class ExerciseConcept(Base):
    __tablename__ = "exercise_concepts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    exercise_id: Mapped[int] = mapped_column(Integer, ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False)
    concept_id: Mapped[int] = mapped_column(Integer, ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False)

    exercise: Mapped["Exercise"] = relationship(back_populates="concepts")
    concept: Mapped["Concept"] = relationship()

class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    exercise_id: Mapped[int] = mapped_column(Integer, ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False)
    period_id: Mapped[int] = mapped_column(Integer, ForeignKey("academic_periods.id", ondelete="CASCADE"), nullable=False)
    user_answer: Mapped[str] = mapped_column(String(255), nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    attempt_number: Mapped[int] = mapped_column(Integer, default=1)
    time_spent_seconds: Mapped[float] = mapped_column(Float, default=0.0)
    feedback_message: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    user: Mapped["User"] = relationship(back_populates="attempts")
    exercise: Mapped["Exercise"] = relationship(back_populates="attempts")
    period: Mapped["AcademicPeriod"] = relationship(back_populates="attempts")

class TopicProgress(Base):
    __tablename__ = "topic_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    period_id: Mapped[int] = mapped_column(Integer, ForeignKey("academic_periods.id", ondelete="CASCADE"), nullable=False)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="available") # locked, available, in_progress, completed
    completion_percent: Mapped[float] = mapped_column(Float, default=0.0)
    last_activity: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    user: Mapped["User"] = relationship(back_populates="progress")
    period: Mapped["AcademicPeriod"] = relationship(back_populates="progress")
    topic: Mapped["Topic"] = relationship(back_populates="progress")

class ConceptMastery(Base):
    __tablename__ = "concept_mastery"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    concept_id: Mapped[int] = mapped_column(Integer, ForeignKey("concepts.id", ondelete="CASCADE"), nullable=False)
    mastery_probability: Mapped[float] = mapped_column(Float, default=0.20) # BKT P(L)
    elo_rating: Mapped[float] = mapped_column(Float, default=1200.0)
    total_attempts: Mapped[int] = mapped_column(Integer, default=0)
    correct_attempts: Mapped[int] = mapped_column(Integer, default=0)
    last_practiced: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    user: Mapped["User"] = relationship(back_populates="masteries")
    concept: Mapped["Concept"] = relationship(back_populates="masteries")

class Exam(Base):
    """Modelo para guardar simulacros de prueba completos."""
    __tablename__ = "exams"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    period_id: Mapped[int] = mapped_column(Integer, ForeignKey("academic_periods.id", ondelete="CASCADE"), nullable=False)
    year_level: Mapped[int] = mapped_column(Integer, nullable=False)  # 5 o 6
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    time_limit_minutes: Mapped[int] = mapped_column(Integer, default=45)
    total_questions: Mapped[int] = mapped_column(Integer, default=20)
    correct_count: Mapped[int] = mapped_column(Integer, default=0)
    score_percent: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(20), default="in_progress")  # in_progress, completed, timed_out
    answers_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)  # {ex_id: user_answer}
    questions_json: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)  # ordered list of exercise ids

    user: Mapped["User"] = relationship()
    period: Mapped["AcademicPeriod"] = relationship()
