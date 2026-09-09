from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database.engine import get_db
from app.database.models import User
from app.auth.dependencies import get_current_user
from app.progress.service import get_academic_history, promote_student

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/progreso", tags=["progress"])

@router.get("/historial", response_class=HTMLResponse)
def history_view(
    request: Request,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    history = get_academic_history(db, user)
    return templates.TemplateResponse(
        request=request,
        name="progress/history.html",
        context={"user": user, "history": history}
    )

@router.post("/cambiar-ano", response_class=HTMLResponse)
def change_year_view(
    request: Request,
    target_year: int = Form(...),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if target_year not in [5, 6]:
        raise HTTPException(status_code=400, detail="Ano invalido.")

    if target_year != user.current_year:
        promote_student(db, user, target_year)

    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
