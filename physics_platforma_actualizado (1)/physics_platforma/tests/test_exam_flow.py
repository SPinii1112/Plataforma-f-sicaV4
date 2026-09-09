import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.engine import SessionLocal
from app.database.models import User, Exam

def test_simulacro_flow():
    client = TestClient(app)
    username = f"UserExam_{uuid.uuid4().hex[:6]}"

    # Registrar usuario
    client.post("/auth/register", data={
        "full_name": "Alumno Simulacro",
        "username": username,
        "password": "PasswordSegura123",
        "current_year": 6
    })

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        assert user is not None

        # 1. Acceder a inicio de simulacro
        res_init = client.get("/simulacro")
        assert res_init.status_code == 200
        assert "Simulacro de Examen" in res_init.text

        # 2. Iniciar nuevo simulacro
        res_new = client.post("/simulacro/nuevo", follow_redirects=True)
        assert res_new.status_code == 200
        assert "Simulacro #" in res_new.text
        assert "timer-badge" in res_new.text

        exam = db.query(Exam).filter(Exam.user_id == user.id).first()
        assert exam is not None
        assert exam.status == "in_progress"
        assert len(exam.questions_json) == 20

        # 3. Entregar simulacro
        answers = {}
        for q_id in exam.questions_json:
            answers[f"answer_{q_id}"] = "A"

        res_finish = client.post(f"/simulacro/{exam.id}/entregar", data=answers, follow_redirects=True)
        assert res_finish.status_code == 200
        assert "Resultado del Simulacro" in res_finish.text

        db.refresh(exam)
        assert exam.status == "completed"
        assert exam.finished_at is not None

    finally:
        # Cleanup
        if user:
            db.query(Exam).filter(Exam.user_id == user.id).delete()
            db.query(User).filter(User.id == user.id).delete()
            db.commit()
        db.close()
