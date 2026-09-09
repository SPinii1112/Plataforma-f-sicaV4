from fastapi import APIRouter, Request, Depends, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database.engine import get_db
from app.auth.service import register_new_student, authenticate_student
from app.auth.schemas import RegisterRequest
from app.core.security import create_access_token
from app.core.config import settings

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/login.html",
        context={"error": None}
    )

@router.post("/login", response_class=HTMLResponse)
def login_action(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = authenticate_student(db, username, password)
    if not user:
        return templates.TemplateResponse(
            request=request,
            name="auth/login.html",
            context={"error": "Usuario o contrasena incorrectos. Verifica tus datos."},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    token = create_access_token({"sub": str(user.id), "username": user.username, "role": user.role})

    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        samesite="lax",
        secure=settings.APP_ENV == "production"
    )
    return response

@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/register.html",
        context={"error": None}
    )

@router.post("/register", response_class=HTMLResponse)
def register_action(
    request: Request,
    username: str = Form(...),
    full_name: str = Form(...),
    password: str = Form(...),
    current_year: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        req = RegisterRequest(
            username=username,
            full_name=full_name,
            password=password,
            current_year=current_year
        )
        user = register_new_student(db, req)

        token = create_access_token({"sub": str(user.id), "username": user.username, "role": user.role})
        response = RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            samesite="lax",
            secure=settings.APP_ENV == "production"
        )
        return response
    except ValueError as e:
        return templates.TemplateResponse(
            request=request,
            name="auth/register.html",
            context={"error": str(e)},
            status_code=status.HTTP_400_BAD_REQUEST
        )

@router.get("/logout")
@router.post("/logout")
def logout_action():
    response = RedirectResponse(url="/auth/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("access_token")
    return response
