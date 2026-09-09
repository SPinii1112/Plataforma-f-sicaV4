from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database.engine import get_db
from app.database.models import User, Topic, Module, Exercise, TopicProgress, Attempt
from app.auth.dependencies import get_current_user
from app.progress.service import get_student_dashboard_data, get_active_period
from app.exercises.service import submit_exercise

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(tags=["learning"])

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_view(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    data = get_student_dashboard_data(db, user)
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"data": data, "user": user}
    )

@router.get("/tema/{topic_id}", response_class=HTMLResponse)
def topic_view(
    topic_id: int,
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Tema no encontrado.")

    if topic.module.year_level != user.current_year:
        raise HTTPException(
            status_code=403,
            detail=f"Este tema pertenece al programa de {topic.module.year_level}.º ano. Tu ano activo es {user.current_year}.º ano."
        )

    period = get_active_period(db, user)

    prog = db.query(TopicProgress).filter(
        TopicProgress.user_id == user.id,
        TopicProgress.period_id == period.id,
        TopicProgress.topic_id == topic.id
    ).first()

    if prog and prog.status == "available":
        prog.status = "in_progress"
        db.commit()

    exercises_data = []
    for ex in topic.exercises:
        last_attempt = db.query(Attempt).filter(
            Attempt.user_id == user.id,
            Attempt.exercise_id == ex.id,
            Attempt.period_id == period.id
        ).order_by(Attempt.created_at.desc()).first()

        exercises_data.append({
            "exercise": ex,
            "last_attempt": last_attempt
        })

    return templates.TemplateResponse(
        request=request,
        name="learning/topic.html",
        context={
            "user": user,
            "topic": topic,
            "module": topic.module,
            "progress": prog,
            "exercises_data": exercises_data
        }
    )

@router.post("/ejercicio/{exercise_id}/submit", response_class=HTMLResponse)
def submit_exercise_view(
    exercise_id: int,
    request: Request,
    user_answer: str = Form(...),
    time_spent_seconds: float = Form(0.0),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Ejercicio no encontrado.")

    result = submit_exercise(
        db=db,
        user=user,
        exercise_id=exercise_id,
        user_answer=user_answer,
        time_spent_seconds=time_spent_seconds
    )

    if request.headers.get("HX-Request"):
        return templates.TemplateResponse(
            request=request,
            name="components/exercise_feedback.html",
            context={
                "exercise": exercise,
                "result": result,
                "user_answer": user_answer
            }
        )

    return RedirectResponse(
        url=f"/tema/{exercise.topic_id}#exercise-{exercise.id}",
        status_code=status.HTTP_303_SEE_OTHER
    )
