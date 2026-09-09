from datetime import datetime, timezone
import math
from sqlalchemy.orm import Session
from app.database.models import User, Exercise, Attempt, TopicProgress
from app.progress.service import get_active_period
from app.adaptive.engine import AdaptiveEngine


def evaluate_numeric_answer(user_val_str: str, correct_val_str: str, tolerance: float = 0.03) -> bool:
    try:
        u_val = float(user_val_str.replace(",", ".").strip())
        c_val = float(correct_val_str.replace(",", ".").strip())
        if c_val == 0:
            return abs(u_val) < 1e-4
        rel_error = abs(u_val - c_val) / abs(c_val)
        return rel_error <= tolerance
    except ValueError:
        return False


def compute_weighted_topic_score(db: Session, user: User, period_id: int, topic_exercises: list) -> float:
    """
    Puntaje ponderado real: puede bajar si el alumno comete muchos errores.
    base_score = (resueltos_correctamente / total) * 100
    penalizacion = 3 pts por cada intento incorrecto antes del primer acierto
    """
    if not topic_exercises:
        return 0.0

    ex_ids = [e.id for e in topic_exercises]
    total = len(ex_ids)
    base_score = 0.0
    penalty = 0.0

    for ex_id in ex_ids:
        attempts = db.query(Attempt).filter(
            Attempt.user_id == user.id,
            Attempt.period_id == period_id,
            Attempt.exercise_id == ex_id
        ).order_by(Attempt.created_at.asc()).all()

        if not attempts:
            continue

        correct_attempts = [a for a in attempts if a.is_correct]
        if correct_attempts:
            base_score += (1 / total) * 100
            first_correct_idx = attempts.index(correct_attempts[0])
            penalty += first_correct_idx * 3.0
        else:
            penalty += len(attempts) * 1.5

    return max(0.0, min(100.0, round(base_score - penalty, 1)))


def submit_exercise(
    db: Session,
    user: User,
    exercise_id: int,
    user_answer: str,
    time_spent_seconds: float = 0.0
) -> dict:
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise ValueError("Ejercicio no encontrado.")

    period = get_active_period(db, user)
    clean_answer = user_answer.strip()

    if exercise.exercise_type == "numeric":
        is_correct = evaluate_numeric_answer(clean_answer, exercise.correct_answer, exercise.tolerance)
    else:
        is_correct = (clean_answer.upper() == exercise.correct_answer.strip().upper())

    prev_attempts = db.query(Attempt).filter(
        Attempt.user_id == user.id,
        Attempt.exercise_id == exercise.id,
        Attempt.period_id == period.id
    ).order_by(Attempt.created_at.asc()).all()
    attempt_num = len(prev_attempts) + 1

    # Hint socrático almacenado en common_errors JSON
    hint = ""
    if exercise.common_errors and isinstance(exercise.common_errors, dict):
        hint = exercise.common_errors.get("hint", "")
    if not hint:
        hint = "Antes de reintentar: revisá qué formula o principio fisico aplica a esta situacion."

    # Retroalimentacion progresiva
    if is_correct:
        feedback = "Excelente! Tu respuesta es correcta."
        show_hint = False
        show_steps = False
        show_answer = False
        reveal_mode = "correct"
    else:
        prev_errors = sum(1 for a in prev_attempts if not a.is_correct)

        if prev_errors == 0:
            feedback = "No es correcto. Antes de volver a intentarlo, pensa en lo siguiente:"
            show_hint = True
            show_steps = False
            show_answer = False
            reveal_mode = "hint"
        elif prev_errors == 1:
            feedback = "Todavia no. Aca tenes los pasos para guiarte; intenta de nuevo:"
            show_hint = False
            show_steps = True
            show_answer = False
            reveal_mode = "steps"
        else:
            feedback = "Despues de varios intentos, aca esta la solucion completa:"
            show_hint = False
            show_steps = True
            show_answer = True
            reveal_mode = "full"

    now = datetime.now(timezone.utc)
    attempt = Attempt(
        user_id=user.id,
        exercise_id=exercise.id,
        period_id=period.id,
        user_answer=clean_answer,
        is_correct=is_correct,
        attempt_number=attempt_num,
        time_spent_seconds=time_spent_seconds,
        feedback_message=feedback,
        created_at=now
    )
    db.add(attempt)
    db.flush()

    AdaptiveEngine.process_attempt(db, user, exercise, is_correct)

    topic_prog = db.query(TopicProgress).filter(
        TopicProgress.user_id == user.id,
        TopicProgress.period_id == period.id,
        TopicProgress.topic_id == exercise.topic_id
    ).first()

    if not topic_prog:
        topic_prog = TopicProgress(
            user_id=user.id,
            period_id=period.id,
            topic_id=exercise.topic_id,
            status="in_progress",
            completion_percent=0.0,
            last_activity=now
        )
        db.add(topic_prog)
        db.flush()

    topic_exercises = exercise.topic.exercises
    weighted_score = compute_weighted_topic_score(db, user, period.id, topic_exercises)
    topic_prog.completion_percent = weighted_score
    topic_prog.last_activity = now
    if weighted_score >= 80.0:
        topic_prog.status = "completed"
        topic_prog.completed_at = now
    else:
        topic_prog.status = "in_progress"

    db.commit()

    return {
        "is_correct": is_correct,
        "feedback": feedback,
        "reveal_mode": reveal_mode,
        "hint": hint if show_hint else "",
        "show_steps": show_steps,
        "show_answer": show_answer,
        "correct_answer": exercise.correct_answer if show_answer else None,
        "solution_steps": exercise.solution_steps if show_steps else "",
        "explanation": exercise.explanation if (is_correct or show_answer) else "",
        "topic_percent": int(topic_prog.completion_percent) if topic_prog else 0,
        "attempt_number": attempt_num
    }
