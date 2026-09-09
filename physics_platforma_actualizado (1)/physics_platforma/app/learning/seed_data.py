import json
from pathlib import Path
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal
from app.database.models import Module, Topic, Concept, Exercise, ExerciseConcept

BASE_DIR = Path(__file__).resolve().parent

def seed_physics_curriculum():
    from app.database.engine import engine, Base
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    try:
        if db.query(Module).first():
            print('Curriculo ya inicializado.')
            return

        print('Cargando los temas oficiales pedidos para 5.º y 6.º...')

        # 1. 5.º Ano
        path_5to = BASE_DIR / 'curriculum_5to.json'
        with open(path_5to, 'r', encoding='utf-8') as f:
            data_5 = json.load(f)

        for m_idx, m_data in enumerate(data_5, start=1):
            mod = Module(
                year_level=5,
                slug=m_data['slug'],
                name=m_data['module_name'],
                description=m_data['desc'],
                order_index=m_idx,
                icon=m_data.get('icon', 'book')
            )
            db.add(mod)
            db.flush()

            for t_idx, t_data in enumerate(m_data['topics'], start=1):
                top = Topic(
                    module_id=mod.id,
                    slug=t_data['slug'],
                    name=t_data['name'],
                    summary=t_data['summary'],
                    theory_content=t_data['theory'],
                    order_index=t_idx,
                    estimated_minutes=25
                )
                db.add(top)
                db.flush()

                concept_objs = []
                for c_name in t_data['concepts']:
                    c = Concept(topic_id=top.id, name=c_name, description=c_name)
                    db.add(c)
                    concept_objs.append(c)
                db.flush()

                for ex_data in t_data['exercises']:
                    ex = Exercise(
                        topic_id=top.id,
                        exercise_type='multiple_choice',
                        difficulty=ex_data.get('difficulty', 'intermediate'),
                        statement=ex_data['statement'],
                        options=ex_data['options'],
                        correct_answer=ex_data['correct'],
                        solution_steps=ex_data['solution'],
                        explanation=ex_data['explanation'],
                        elo_rating=1200.0
                    )
                    db.add(ex)
                    db.flush()
                    if concept_objs:
                        db.add(ExerciseConcept(exercise_id=ex.id, concept_id=concept_objs[0].id))

        # 2. 6.º Ano
        path_6to = BASE_DIR / 'curriculum_6to.json'
        with open(path_6to, 'r', encoding='utf-8') as f:
            data_6 = json.load(f)

        for m_idx, m_data in enumerate(data_6, start=1):
            mod = Module(
                year_level=6,
                slug=m_data['slug'],
                name=m_data['module_name'],
                description=m_data['desc'],
                order_index=m_idx,
                icon=m_data.get('icon', 'zap')
            )
            db.add(mod)
            db.flush()

            for t_idx, t_data in enumerate(m_data['topics'], start=1):
                top = Topic(
                    module_id=mod.id,
                    slug=t_data['slug'],
                    name=t_data['name'],
                    summary=t_data['summary'],
                    theory_content=t_data['theory'],
                    order_index=t_idx,
                    estimated_minutes=30
                )
                db.add(top)
                db.flush()

                concept_objs = []
                for c_name in t_data['concepts']:
                    c = Concept(topic_id=top.id, name=c_name, description=c_name)
                    db.add(c)
                    concept_objs.append(c)
                db.flush()

                for ex_data in t_data['exercises']:
                    ex = Exercise(
                        topic_id=top.id,
                        exercise_type='multiple_choice',
                        difficulty=ex_data.get('difficulty', 'intermediate'),
                        statement=ex_data['statement'],
                        options=ex_data['options'],
                        correct_answer=ex_data['correct'],
                        solution_steps=ex_data['solution'],
                        explanation=ex_data['explanation'],
                        elo_rating=1200.0
                    )
                    db.add(ex)
                    db.flush()
                    if concept_objs:
                        db.add(ExerciseConcept(exercise_id=ex.id, concept_id=concept_objs[0].id))

        db.commit()
        print('¡Curriculo oficial sembrado exitosamente!')
    finally:
        db.close()

if __name__ == '__main__':
    seed_physics_curriculum()
