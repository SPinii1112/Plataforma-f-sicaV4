from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.database.models import User, AcademicPeriod, Module, Topic, TopicProgress
from app.core.security import hash_password, verify_password, create_access_token
from app.auth.schemas import RegisterRequest

def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username.ilike(username.strip())).first()

def register_new_student(db: Session, req: RegisterRequest) -> User:
    # 1. Verificar si ya existe el usuario
    if get_user_by_username(db, req.username):
        raise ValueError("El nombre de usuario ya esta en uso.")

    # 2. Hashear password con Argon2id
    hashed = hash_password(req.password)

    # 3. Crear usuario
    now = datetime.now(timezone.utc)
    user = User(
        username=req.username.strip(),
        password_hash=hashed,
        full_name=req.full_name.strip(),
        current_year=req.current_year,
        role="student",
        created_at=now,
        updated_at=now,
        is_active=True
    )
    db.add(user)
    db.flush()

    # 4. Crear periodo academico inicial
    current_calendar_year = now.year
    period = AcademicPeriod(
        user_id=user.id,
        year_level=req.current_year,
        calendar_year=current_calendar_year,
        status="active",
        final_progress=0.0,
        created_at=now
    )
    db.add(period)
    db.flush()

    # 5. Inicializar progreso para los temas correspondientes a su ano
    modules = db.query(Module).filter(Module.year_level == req.current_year).all()
    for mod in modules:
        for topic in mod.topics:
            prog = TopicProgress(
                user_id=user.id,
                period_id=period.id,
                topic_id=topic.id,
                status="available",
                completion_percent=0.0,
                last_activity=now
            )
            db.add(prog)

    db.commit()
    db.refresh(user)
    return user

def authenticate_student(db: Session, username: str, password: str) -> User | None:
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    if not user.is_active:
        return None
    return user
