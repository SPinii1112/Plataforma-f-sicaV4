from app.database.engine import engine, Base
from app.database.models import (
    User, AcademicPeriod, Module, Topic, Concept, Exercise,
    ExerciseConcept, Attempt, TopicProgress, ConceptMastery
)

def init_database():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    init_database()
