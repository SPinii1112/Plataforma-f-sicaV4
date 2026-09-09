from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.auth.router import router as auth_router
from app.learning.router import router as learning_router
from app.progress.router import router as progress_router
from app.exam.router import router as exam_router
from app.database.engine import engine, Base
from app.learning.seed_data import seed_physics_curriculum

# Crear tablas e inicializar curriculo al iniciar
Base.metadata.create_all(bind=engine)
seed_physics_curriculum()

app = FastAPI(
    title=settings.APP_NAME,
    description="Plataforma adaptativa de aprendizaje de Fisica para 5.º y 6.º ano de Liceo en Uruguay",
    version="1.0.0"
)

# Archivos estaticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Routers
app.include_router(auth_router)
app.include_router(learning_router)
app.include_router(progress_router)
app.include_router(exam_router)

@app.get("/")
def root_redirect(request: Request):
    # Si tiene cookie de sesion va a dashboard, si no a login
    if request.cookies.get("access_token"):
        return RedirectResponse(url="/dashboard", status_code=303)
    return RedirectResponse(url="/auth/login", status_code=303)
