import uuid
from fastapi.testclient import TestClient
from app.main import app
from app.database.engine import SessionLocal
from app.database.models import User, Topic, Module, Exercise, Attempt, TopicProgress

def test_exercise_submission_and_progress_flow():
    client = TestClient(app)
    user_name = f"TestEx_{uuid.uuid4().hex[:6]}"

    # 1. Registrar usuario en 5.º ano
    res_reg = client.post(
        "/auth/register",
        data={
            "full_name": "Estudiante Prueba",
            "username": user_name,
            "password": "passSeguro123",
            "current_year": 5
        },
        follow_redirects=False
    )
    assert res_reg.status_code == 303

    db = SessionLocal()
    try:
        # Obtener un ejercicio de 5to ano de forma limpia
        exercise = db.query(Exercise).join(Topic).join(Module).filter(
            Module.year_level == 5
        ).first()
        assert exercise is not None
        ex_id = exercise.id
        correct_ans = exercise.correct_answer

        # 2. Enviar respuesta correcta vía HTMX
        res_submit_correct = client.post(
            f"/ejercicio/{ex_id}/submit",
            data={"user_answer": correct_ans, "time_spent_seconds": 25.0},
            headers={"HX-Request": "true"}
        )
        assert res_submit_correct.status_code == 200
        assert "Respuesta Correcta" in res_submit_correct.text
        assert "Explicacion teorica" in res_submit_correct.text

        # 3. Enviar respuesta incorrecta a otro ejercicio
        res_submit_wrong = client.post(
            f"/ejercicio/{ex_id}/submit",
            data={"user_answer": "OPCION_INVENTADA", "time_spent_seconds": 12.0},
            headers={"HX-Request": "true"}
        )
        assert res_submit_wrong.status_code == 200
        assert "Respuesta Incorrecta" in res_submit_wrong.text
        assert "Reintentar Ejercicio" in res_submit_wrong.text

        # 4. Verificar que se grabaron los intentos en la BD
        user = db.query(User).filter(User.username == user_name).first()
        attempts = db.query(Attempt).filter(Attempt.user_id == user.id).all()
        assert len(attempts) == 2
        assert attempts[0].is_correct is True
        assert attempts[1].is_correct is False
    finally:
        u = db.query(User).filter(User.username == user_name).first()
        if u:
            db.delete(u)
            db.commit()
        db.close()
