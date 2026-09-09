# Full database seeder with 20+ questions per topic and extensive theory
import json
import random
from sqlalchemy.orm import Session
from app.database.engine import SessionLocal, Base, engine
from app.database.models import Module, Topic, Concept, Exercise, ExerciseConcept, Attempt, TopicProgress, ConceptMastery
from app.learning.question_helper import make_mc

# Cargar teoria extendida
with open('app/learning/theory_5to.json', 'r', encoding='utf-8') as f:
    theory_5to = json.load(f)

with open('app/learning/theory_6to.json', 'r', encoding='utf-8') as f:
    theory_6to = json.load(f)

print('Teorias cargadas con exito.')
