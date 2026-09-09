class EloCalibrator:
    """
    Sistema de rating Elo en Python puro.
    Permite emparejar al estudiante con ejercicios acordes a su nivel
    y calibrar la dificultad intrinseca de cada problema.
    """
    def __init__(self, k_student: float = 32.0, k_exercise: float = 16.0):
        self.k_student = k_student
        self.k_exercise = k_exercise

    def expected_score(self, student_rating: float, exercise_rating: float) -> float:
        """Probabilidad esperada de exito segun diferencia de ratings."""
        return 1.0 / (1.0 + 10.0 ** ((exercise_rating - student_rating) / 400.0))

    def update_ratings(self, student_rating: float, exercise_rating: float, is_correct: bool) -> tuple[float, float]:
        actual = 1.0 if is_correct else 0.0
        exp = self.expected_score(student_rating, exercise_rating)

        new_student = student_rating + self.k_student * (actual - exp)
        new_exercise = exercise_rating + self.k_exercise * (exp - actual)

        return round(new_student, 1), round(new_exercise, 1)

elo = EloCalibrator()
