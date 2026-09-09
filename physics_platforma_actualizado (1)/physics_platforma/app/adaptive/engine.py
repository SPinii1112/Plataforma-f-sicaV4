from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.database.models import User, Exercise, ConceptMastery, Concept
from app.adaptive.bkt import bkt
from app.adaptive.elo import elo

class AdaptiveEngine:
    """
    Coordina la adaptacion pedagogica determinista:
    - Actualiza dominio BKT en cada concepto involucrado
    - Calibra ratings Elo
    - Genera diagnosticos y recomendaciones claras y explicables
    """
    @staticmethod
    def process_attempt(db: Session, user: User, exercise: Exercise, is_correct: bool):
        now = datetime.now(timezone.utc)

        # 1. Actualizar cada concepto del ejercicio
        for ec in exercise.concepts:
            concept_id = ec.concept_id
            mastery = db.query(ConceptMastery).filter(
                ConceptMastery.user_id == user.id,
                ConceptMastery.concept_id == concept_id
            ).first()

            if not mastery:
                mastery = ConceptMastery(
                    user_id=user.id,
                    concept_id=concept_id,
                    mastery_probability=0.20,
                    elo_rating=1200.0,
                    total_attempts=0,
                    correct_attempts=0,
                    last_practiced=now
                )
                db.add(mastery)
                db.flush()

            mastery.total_attempts += 1
            if is_correct:
                mastery.correct_attempts += 1

            # BKT
            mastery.mastery_probability = bkt.update_mastery(mastery.mastery_probability, is_correct)

            # Elo
            new_user_elo, new_ex_elo = elo.update_ratings(mastery.elo_rating, exercise.elo_rating, is_correct)
            mastery.elo_rating = new_user_elo
            exercise.elo_rating = new_ex_elo
            mastery.last_practiced = now

        db.commit()

    @staticmethod
    def get_user_recommendation(db: Session, user: User) -> dict:
        """
        Determina la mejor recomendacion educativa explicable para el alumno:
        Prioriza conceptos con bajo dominio y ejercicios clave.
        """
        # Buscar conceptos donde el alumno haya practicado y tenga P(L) < 0.60
        struggling = db.query(ConceptMastery, Concept).join(
            Concept, ConceptMastery.concept_id == Concept.id
        ).filter(
            ConceptMastery.user_id == user.id,
            ConceptMastery.mastery_probability < 0.60
        ).order_by(ConceptMastery.mastery_probability.asc()).first()

        if struggling:
            mastery, concept = struggling
            pct = int(mastery.mastery_probability * 100)
            return {
                "has_recommendation": True,
                "type": "reinforce",
                "title": f"Reforzar concepto: {concept.name}",
                "message": f"Detectamos que tu dominio actual en '{concept.name}' es de {pct}%. Te sugerimos repasar la teoria y realizar ejercicios de fijacion.",
                "concept_name": concept.name
            }

        return {
            "has_recommendation": True,
            "type": "continue",
            "title": "¡Excelente ritmo de aprendizaje!",
            "message": "Vas con buen nivel de comprension. Te recomendamos continuar con el siguiente tema de tu programa.",
            "concept_name": None
        }
