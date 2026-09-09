from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database.engine import get_db
from app.database.models import Exam
from app.auth.dependencies import get_current_user
from app.database.models import User
from app.exam.service import create_exam, get_exam_exercises, submit_exam

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/simulacro", tags=["exam"])


@router.get("", response_class=HTMLResponse)
def simulacro_start(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Pantalla de inicio del simulacro."""
    return templates.TemplateResponse(
        request=request,
        name="exam/inicio.html",
        context={"user": user}
    )


@router.post("/nuevo", response_class=HTMLResponse)
def simulacro_nuevo(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Crea un nuevo simulacro y redirige a la pantalla de examen."""
    exam = create_exam(db, user)
    return RedirectResponse(url=f"/simulacro/{exam.id}", status_code=303)


@router.get("/{exam_id}", response_class=HTMLResponse)
def simulacro_view(
    exam_id: int,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Pantalla del simulacro en curso."""
    exam = db.query(Exam).filter(Exam.id == exam_id, Exam.user_id == user.id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Simulacro no encontrado.")
    if exam.status != "in_progress":
        return RedirectResponse(url=f"/simulacro/{exam_id}/resultado", status_code=303)

    exercises = get_exam_exercises(db, exam)
    return templates.TemplateResponse(
        request=request,
        name="exam/simulacro.html",
        context={"user": user, "exam": exam, "exercises": exercises}
    )


@router.post("/{exam_id}/entregar", response_class=HTMLResponse)
async def simulacro_entregar(
    exam_id: int,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Evalua y guarda el simulacro al entregarlo."""
    exam = db.query(Exam).filter(Exam.id == exam_id, Exam.user_id == user.id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Simulacro no encontrado.")
    if exam.status != "in_progress":
        return RedirectResponse(url=f"/simulacro/{exam_id}/resultado", status_code=303)

    form_data = await request.form()
    answers = {}
    for key, value in form_data.items():
        if key.startswith("answer_"):
            ex_id = key.replace("answer_", "")
            answers[ex_id] = str(value).strip().upper()

    submit_exam(db, exam, answers)
    return RedirectResponse(url=f"/simulacro/{exam_id}/resultado", status_code=303)


@router.get("/{exam_id}/resultado", response_class=HTMLResponse)
def simulacro_resultado(
    exam_id: int,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Pantalla de resultados del simulacro."""
    exam = db.query(Exam).filter(Exam.id == exam_id, Exam.user_id == user.id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Simulacro no encontrado.")
    if exam.status == "in_progress":
        return RedirectResponse(url=f"/simulacro/{exam_id}", status_code=303)

    from app.exam.service import get_exam_exercises
    exercises = get_exam_exercises(db, exam)
    answers = exam.answers_json or {}

    results = []
    for ex in exercises:
        user_ans = answers.get(str(ex.id), "").strip().upper()
        is_correct = user_ans == ex.correct_answer.strip().upper()
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

    score_pct = exam.score_percent
    if score_pct >= 85:
        grade, grade_color = "Excelente", "emerald"
    elif score_pct >= 70:
        grade, grade_color = "Muy Bueno", "green"
    elif score_pct >= 55:
        grade, grade_color = "Bueno", "amber"
    elif score_pct >= 40:
        grade, grade_color = "Suficiente", "orange"
    else:
        grade, grade_color = "Necesita Repasar", "red"

    return templates.TemplateResponse(
        request=request,
        name="exam/resultado.html",
        context={
            "user": user,
            "exam": exam,
            "results": results,
            "grade": grade,
            "grade_color": grade_color,
        }
    )
