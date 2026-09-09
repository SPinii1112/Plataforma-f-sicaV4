import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.engine import Base
from app.database.models import User, AcademicPeriod, Module, Topic, Concept, Exercise
from app.learning.seed_data import seed_physics_curriculum

TEST_DB_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def test_db():
    engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
