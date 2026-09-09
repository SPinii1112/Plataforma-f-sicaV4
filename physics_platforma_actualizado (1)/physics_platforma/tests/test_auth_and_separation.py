import pytest
from app.auth.service import register_new_student, authenticate_student
from app.auth.schemas import RegisterRequest
from app.database.models import User, Module
from app.progress.service import get_student_dashboard_data
from app.learning.seed_data import seed_physics_curriculum

def test_student_separation_5th_and_6th_year(test_db):
    # Inicializar curriculo
    from app.database.engine import engine
    from app.learning.seed_data import seed_physics_curriculum
    from app.database.engine import SessionLocal

    # Crear modulos de prueba en la base de test
    mod_5 = Module(year_level=5, slug="5to-test", name="Cinematica 5to", order_index=1)
    mod_6 = Module(year_level=6, slug="6to-test", name="Electrostatica 6to", order_index=1)
    test_db.add_all([mod_5, mod_6])
    test_db.commit()

    # 1. Registrar a Spini en 6.º
    req_spini = RegisterRequest(username="Spini", full_name="Santiago Pini", password="password6to", current_year=6)
    user_spini = register_new_student(test_db, req_spini)

    # 2. Registrar a Pedrito en 5.º
    req_pedrito = RegisterRequest(username="Pedrito", full_name="Pedro", password="password5to", current_year=5)
    user_pedrito = register_new_student(test_db, req_pedrito)

    assert user_spini.id != user_pedrito.id
    assert user_spini.current_year == 6
    assert user_pedrito.current_year == 5

    # 3. Verificar que Spini solo ve modulos de 6.º ano
    data_spini = get_student_dashboard_data(test_db, user_spini)
    assert len(data_spini["modules"]) == 1
    assert data_spini["modules"][0]["name"] == "Electrostatica 6to"

    # 4. Verificar que Pedrito solo ve modulos de 5.º ano
    data_pedrito = get_student_dashboard_data(test_db, user_pedrito)
    assert len(data_pedrito["modules"]) == 1
    assert data_pedrito["modules"][0]["name"] == "Cinematica 5to"

    # 5. Probar autenticacion segura
    auth_spini = authenticate_student(test_db, "Spini", "password6to")
    assert auth_spini is not None
    assert auth_spini.id == user_spini.id

    # Clave incorrecta
    assert authenticate_student(test_db, "Spini", "clave_mala") is None
