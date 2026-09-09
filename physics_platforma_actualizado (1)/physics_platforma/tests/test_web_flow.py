import uuid
from fastapi.testclient import TestClient
from app.main import app

def test_complete_web_flow():
    client = TestClient(app)
    unique_user = f"Spini_{uuid.uuid4().hex[:6]}"

    # 1. Pagina de login accesible
    res_login = client.get("/auth/login")
    assert res_login.status_code == 200
    assert "Iniciar Sesion" in res_login.text

    # 2. Registrar alumno Spini en 6.º ano
    res_reg = client.post(
        "/auth/register",
        data={
            "full_name": "Santiago Pini",
            "username": unique_user,
            "password": "miPasswordSeguro123",
            "current_year": 6
        },
        follow_redirects=False
    )
    assert res_reg.status_code == 303
    assert "access_token" in res_reg.cookies

    # 3. Acceder al dashboard con sesion activa
    res_dash = client.get("/dashboard")
    assert res_dash.status_code == 200
    assert "Santiago Pini" in res_dash.text
    assert "Electrostática" in res_dash.text or "Electrostatica" in res_dash.text or "6.º" in res_dash.text

    # 4. Probar acceso no autenticado con un cliente limpio -> debe redirigir a login
    clean_client = TestClient(app)
    res_unauth = clean_client.get("/dashboard", follow_redirects=False)
    assert res_unauth.status_code == 307
    assert "/auth/login" in res_unauth.headers["location"]

    # 5. Limpieza del usuario de prueba
    from app.database.engine import SessionLocal
    from app.database.models import User
    db = SessionLocal()
    try:
        u = db.query(User).filter(User.username == unique_user).first()
        if u:
            db.delete(u)
            db.commit()
    finally:
        db.close()
