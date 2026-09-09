from app.auth.service import register_new_student
from app.auth.schemas import RegisterRequest
from app.progress.service import promote_student, get_academic_history

def test_history_retention_on_promotion(test_db):
    # Registrar alumno en 5.º ano
    req = RegisterRequest(username="SantiTest", full_name="Santiago", password="password123", current_year=5)
    user = register_new_student(test_db, req)

    # Simular que completo el ano con 87% de progreso
    from app.progress.service import get_active_period
    period_5 = get_active_period(test_db, user)
    period_5.final_progress = 87.0
    test_db.commit()

    # Promover a 6.º ano
    new_period_6 = promote_student(test_db, user, target_year=6)

    # Verificar que el usuario ahora esta en 6to
    assert user.current_year == 6
    assert new_period_6.year_level == 6
    assert new_period_6.status == "active"

    # Verificar historial completo
    history = get_academic_history(test_db, user)
    assert len(history) == 2

    # El periodo de 5.º ano debe conservar su 87% final y estar completado
    period_5_hist = [h for h in history if h["year_level"] == 5][0]
    assert period_5_hist["final_progress"] == 87
    assert period_5_hist["status"] == "completed"

    # El periodo de 6.º ano comienza con 0% y activo
    period_6_hist = [h for h in history if h["year_level"] == 6][0]
    assert period_6_hist["final_progress"] == 0
    assert period_6_hist["status"] == "active"
