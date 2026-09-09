import json
import random
from pathlib import Path
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal, Base, engine
from app.database.models import Module, Topic, Concept, Exercise, ExerciseConcept, Attempt, TopicProgress, ConceptMastery

random.seed(42)  # Semilla para reproducibilidad controlada pero distribución uniforme

def _balance_option(text: str, target_len: int, max_ratio: float = 1.4) -> str:
    """Trunca opciones que son mucho más largas que el target (evita delatar respuesta correcta)."""
    if len(text) > target_len * max_ratio:
        return text[:int(target_len * max_ratio)].rstrip() + "."
    return text

def make_mc(statement, correct_text, distractors, explanation, solution_steps,
            difficulty='intermediate', elo=1200, hint=''):
    """
    Crea un ejercicio multiple choice con opciones barajadas aleatoriamente.
    hint: pista socrática que se muestra en el 1er intento incorrecto (NO revela la respuesta).
    """
    all_texts = [correct_text] + list(distractors)
    # Longitud media de todas las opciones
    avg_len = sum(len(t) for t in all_texts) / len(all_texts)
    # Balancear opciones que excedan mucho el promedio
    all_texts = [_balance_option(t, int(avg_len)) for t in all_texts]
    correct_text_balanced = all_texts[0]

    random.shuffle(all_texts)
    correct_idx = all_texts.index(correct_text_balanced)
    letters = ['A', 'B', 'C', 'D']
    correct_letter = letters[correct_idx]
    formatted = [{'id': l, 'text': t} for l, t in zip(letters, all_texts)]
    return {
        'statement': statement,
        'options': formatted,
        'correct': correct_letter,
        'explanation': explanation,
        'solution': solution_steps,
        'difficulty': difficulty,
        'elo': elo,
        'hint': hint or '¿Revisaste qué fórmula o principio físico aplica a esta situación?'
    }

print('make_mc listo')

