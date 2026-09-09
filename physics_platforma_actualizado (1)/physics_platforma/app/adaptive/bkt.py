class BKTTracker:
    """
    Bayesian Knowledge Tracing (BKT) en Python puro (sin IA ni dependencias externas).
    Calcula la probabilidad P(L) de que el alumno domine un concepto atomico.
    """
    def __init__(
        self,
        p_init: float = 0.20,   # P(L0): probabilidad inicial a priori
        p_trans: float = 0.15,  # P(T): probabilidad de transicion/aprendizaje tras practicar
        p_guess: float = 0.20,  # P(G): probabilidad de adivinar correctamente por suerte
        p_slip: float = 0.10    # P(S): probabilidad de resbalon/error sabiendo el tema
    ):
        self.p_init = p_init
        self.p_trans = p_trans
        self.p_guess = p_guess
        self.p_slip = p_slip

    def update_mastery(self, p_prior: float, is_correct: bool) -> float:
        """Calcula la probabilidad posterior tras una observacion (acierto o error)."""
        # Asegurar limites
        p_prior = max(0.01, min(0.99, p_prior))

        if is_correct:
            # P(L | correcto)
            num = p_prior * (1.0 - self.p_slip)
            den = num + (1.0 - p_prior) * self.p_guess
        else:
            # P(L | incorrecto)
            num = p_prior * self.p_slip
            den = num + (1.0 - p_prior) * (1.0 - self.p_guess)

        if den == 0:
            p_post = p_prior
        else:
            p_post = num / den

        # Aplicar probabilidad de aprendizaje durante la practica
        p_next = p_post + (1.0 - p_post) * self.p_trans
        return round(float(min(0.99, max(0.01, p_next))), 4)

bkt = BKTTracker()
