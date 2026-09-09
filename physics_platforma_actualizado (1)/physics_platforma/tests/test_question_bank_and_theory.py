# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal
from app.database.models import Topic, Exercise

def test_every_topic_has_at_least_20_questions():
    db: Session = SessionLocal()
    try:
        topics = db.query(Topic).all()
        assert len(topics) == 20, f"Se esperaban 20 temas oficiales, se encontraron {len(topics)}"

        for topic in topics:
            count = db.query(Exercise).filter(Exercise.topic_id == topic.id).count()
            assert count >= 20, f"El tema {topic.name} ({topic.slug}) tiene {count} ejercicios, se requieren mínimo 20"
    finally:
        db.close()

def test_no_topic_has_all_answers_as_A_and_answers_are_randomized():
    db: Session = SessionLocal()
    try:
        topics = db.query(Topic).all()
        global_answers = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        for topic in topics:
            exercises = db.query(Exercise).filter(Exercise.topic_id == topic.id).all()
            topic_answers = [ex.correct_answer for ex in exercises]
            
            # Ningun tema debe tener todas las respuestas iguales a 'A'
            assert set(topic_answers) != {'A'}, f"El tema {topic.name} tiene todas sus respuestas como 'A'"
            # Cada tema debe tener variedad de letras (al menos 3 letras distintas representadas en sus 20 ejercicios)
            assert len(set(topic_answers)) >= 3, f"El tema {topic.name} tiene poca variedad de respuestas: {set(topic_answers)}"

            for a in topic_answers:
                global_answers[a] += 1

        # En las 400 preguntas la distribución debe ser uniforme y equilibrada (~25% cada una)
        print('Distribución global:', global_answers)
        for letter in ['A', 'B', 'C', 'D']:
            assert global_answers[letter] >= 70, f"La letra {letter} tiene muy pocas respuestas: {global_answers[letter]}"

    finally:
        db.close()

def test_topics_have_rich_theory_content():
    db: Session = SessionLocal()
    try:
        topics = db.query(Topic).all()
        for topic in topics:
            assert topic.theory_content, f"El tema {topic.name} no tiene contenido teórico"
            assert len(topic.theory_content) > 300, f"El contenido teórico de {topic.name} es demasiado corto ({len(topic.theory_content)} caracteres)"
    finally:
        db.close()
