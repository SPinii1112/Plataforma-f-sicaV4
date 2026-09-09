from app.adaptive.bkt import bkt
from app.adaptive.elo import elo

def test_bkt_deterministic_updates():
    p_prior = 0.20

    # Acierto incrementa P(L)
    p_after_correct = bkt.update_mastery(p_prior, is_correct=True)
    assert p_after_correct > p_prior

    # Error decrementa o mantiene acotado
    p_after_wrong = bkt.update_mastery(p_prior, is_correct=False)
    assert p_after_wrong < p_after_correct

def test_elo_calibration():
    student_rating = 1200.0
    exercise_rating = 1200.0

    # Si el alumno acierta un ejercicio de igual nivel, su rating sube y el del ejercicio baja
    new_s, new_e = elo.update_ratings(student_rating, exercise_rating, is_correct=True)
    assert new_s > student_rating
    assert new_e < exercise_rating
