import random
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.database.models import User, Exercise, Exam, Module, Topic
from app.progress.service import get_active_period

EXAM_QUESTION_COUNT = 20
EXAM_TIME_MINUTES = 45


def create_exam(db: Session, user: User) -> Exam:
    """Crea un nuevo simulacro con 20 preguntas aleatorias del anio del alumno."""
    period = get_active_period(db, user)

    # Obtener todos los ejercicios activos del anio del usuario
    exercises = (
        db.query(Exercise)
        .join(Topic, Exercise.topic_id == Topic.id)
        .join(Module, Topic.module_id == Module.id)
        .filter(Module.year_level == user.current_year, Exercise.is_active == True)
        .all()
    )

    if len(exercises) < EXAM_QUESTION_COUNT:
        selected = exercises
    else:
        # Seleccion estratificada: mezclar dificultades
        basic = [e for e in exercises if e.difficulty == "basic"]
        intermediate = [e for e in exercises if e.difficulty == "intermediate"]
        advanced = [e for e in exercises if e.difficulty == "advanced"]

        random.shuffle(basic)
        random.shuffle(intermediate)
        random.shuffle(advanced)

        # Proporcion: 5 basic, 10 intermediate, 5 advanced
        selected = basic[:5] + intermediate[:10] + advanced[:5]
        if len(selected) < EXAM_QUESTION_COUNT:
            remaining = [e for e in exercises if e not in selected]
            random.shuffle(remaining)
            selected += remaining[: EXAM_QUESTION_COUNT - len(selected)]
        random.shuffle(selected)
        selected = selected[:EXAM_QUESTION_COUNT]

    ex_ids = [e.id for e in selected]
    now = datetime.now(timezone.utc)

    exam = Exam(
        user_id=user.id,
        period_id=period.id,
        year_level=user.current_year,
        started_at=now,
        time_limit_minutes=EXAM_TIME_MINUTES,
        total_questions=len(ex_ids),
        status="in_progress",
        questions_json=ex_ids,
        answers_json={},
    )
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam


def get_exam_exercises(db: Session, exam: Exam) -> list:
    """Devuelve los ejercicios del simulacro en orden."""
    if not exam.questions_json:
        return []
    exercises = []
    for ex_id in exam.questions_json:
        ex = db.query(Exercise).filter(Exercise.id == ex_id).first()
        if ex:
            exercises.append(ex)
    return exercises


def submit_exam(db: Session, exam: Exam, answers: dict) -> dict:
    """Evalua el simulacro y guarda el resultado."""
    exercises = get_exam_exercises(db, exam)
    correct_count = 0
    results = []

    for ex in exercises:
        user_ans = answers.get(str(ex.id), "").strip().upper()
        is_correct = user_ans == ex.correct_answer.strip().upper()
        if is_correct:
            correct_count += 1
        results.append({
            "exercise_id": ex.id,
            "statement": ex.statement,
            "options": ex.options,
            "user_answer": user_ans,
            "correct_answer": ex.correct_answer,
            "is_correct": is_correct,
            "explanation": ex.explanation,
            "solution_steps": ex.solution_steps,
            "topic_name": ex.topic.name if ex.topic else "",
            "difficulty": ex.difficulty,
        })

    total = len(exercises)
    score_pct = round((correct_count / total * 100), 1) if total > 0 else 0.0

    exam.correct_count = correct_count
    exam.score_percent = score_pct
    exam.status = "completed"
    exam.finished_at = datetime.now(timezone.utc)
    exam.answers_json = answers
    db.commit()

    # Clasificacion
    if score_pct >= 85:
        grade = "Excelente"
        grade_color = "emerald"
    elif score_pct >= 70:
        grade = "Muy Bueno"
        grade_color = "green"
    elif score_pct >= 55:
        grade = "Bueno"
        grade_color = "amber"
    elif score_pct >= 40:
        grade = "Suficiente"
        grade_color = "orange"
    else:
        grade = "Necesita Repasar"
        grade_color = "red"

    return {
        "exam": exam,
        "results": results,
        "correct_count": correct_count,
        "total": total,
        "score_percent": score_pct,
        "grade": grade,
        "grade_color": grade_color,
    }
