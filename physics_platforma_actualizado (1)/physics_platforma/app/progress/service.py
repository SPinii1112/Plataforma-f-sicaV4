from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.database.models import User, AcademicPeriod, Module, Topic, TopicProgress, Attempt
from app.adaptive.engine import AdaptiveEngine

def get_active_period(db: Session, user: User) -> AcademicPeriod:
    period = db.query(AcademicPeriod).filter(
        AcademicPeriod.user_id == user.id,
        AcademicPeriod.status == "active"
    ).order_by(AcademicPeriod.created_at.desc()).first()

    if not period:
        now = datetime.now(timezone.utc)
        period = AcademicPeriod(
            user_id=user.id,
            year_level=user.current_year,
            calendar_year=now.year,
            status="active",
            final_progress=0.0,
            created_at=now
        )
        db.add(period)
        db.commit()
        db.refresh(period)
    return period

def get_student_dashboard_data(db: Session, user: User) -> dict:
    period = get_active_period(db, user)

    # 1. Modulos del ano del alumno
    modules = db.query(Module).filter(
        Module.year_level == user.current_year,
        Module.is_active == True
    ).order_by(Module.order_index.asc()).all()

    module_data = []
    total_topics_count = 0
    completed_topics_count = 0

    for mod in modules:
        mod_topics = []
        mod_completed = 0
        for topic in mod.topics:
            total_topics_count += 1
            # Buscar progreso del tema en el periodo activo
            prog = db.query(TopicProgress).filter(
                TopicProgress.user_id == user.id,
                TopicProgress.period_id == period.id,
                TopicProgress.topic_id == topic.id
            ).first()

            pct = prog.completion_percent if prog else 0.0
            status = prog.status if prog else "available"
            if status == "completed" or pct >= 100.0:
                mod_completed += 1
                completed_topics_count += 1

            mod_topics.append({
                "id": topic.id,
                "name": topic.name,
                "slug": topic.slug,
                "summary": topic.summary,
                "order_index": topic.order_index,
                "estimated_minutes": topic.estimated_minutes,
                "status": status,
                "percent": int(pct)
            })

        mod_pct = int((mod_completed / len(mod.topics) * 100)) if mod.topics else 0
        module_data.append({
            "id": mod.id,
            "name": mod.name,
            "description": mod.description,
            "slug": mod.slug,
            "order_index": mod.order_index,
            "percent": mod_pct,
            "topics": mod_topics
        })

    # Progreso general del ano activo
    global_progress = int((completed_topics_count / total_topics_count * 100)) if total_topics_count > 0 else 0
    period.final_progress = float(global_progress)
    db.commit()

    # 2. Continuar donde dejaste
    # Buscar el ultimo tema con progreso reciente o en progreso
    last_prog = db.query(TopicProgress, Topic, Module).join(
        Topic, TopicProgress.topic_id == Topic.id
    ).join(
        Module, Topic.module_id == Module.id
    ).filter(
        TopicProgress.user_id == user.id,
        TopicProgress.period_id == period.id,
        Module.year_level == user.current_year
    ).order_by(TopicProgress.last_activity.desc()).first()

    resume_topic = None
    if last_prog and last_prog[0].completion_percent < 100.0:
        prog, topic, mod = last_prog
        resume_topic = {
            "id": topic.id,
            "name": topic.name,
            "module_name": mod.name,
            "percent": int(prog.completion_percent)
        }
    elif modules and modules[0].topics:
        # Fallback al primer tema disponible
        first_topic = modules[0].topics[0]
        resume_topic = {
            "id": first_topic.id,
            "name": first_topic.name,
            "module_name": modules[0].name,
            "percent": 0
        }

    # 3. Estadisticas de intentos
    attempts = db.query(Attempt).filter(
        Attempt.user_id == user.id,
        Attempt.period_id == period.id
    ).all()
    total_attempts = len(attempts)
    correct_attempts = sum(1 for a in attempts if a.is_correct)
    accuracy = int((correct_attempts / total_attempts * 100)) if total_attempts > 0 else 0

    # 4. Recomendacion adaptativa
    recommendation = AdaptiveEngine.get_user_recommendation(db, user)

    # 5. Temas más flojos: ordenados por puntaje ponderado ascendente
    all_topic_stats = []
    for mod_d in module_data:
        for top_d in mod_d["topics"]:
            all_topic_stats.append({
                "id": top_d["id"],
                "name": top_d["name"],
                "module_name": mod_d["name"],
                "percent": top_d["percent"],
                "status": top_d["status"],
            })

    # Solo los que tienen alguna actividad (percent < 100 y > 0)
    weak_topics = sorted(
        [t for t in all_topic_stats if 0 < t["percent"] < 100],
        key=lambda t: t["percent"]
    )[:5]  # Top 5 más flojos

    return {
        "user": user,
        "period": period,
        "global_progress": global_progress,
        "resume_topic": resume_topic,
        "total_attempts": total_attempts,
        "correct_attempts": correct_attempts,
        "accuracy": accuracy,
        "recommendation": recommendation,
        "modules": module_data,
        "weak_topics": weak_topics,
    }

def get_academic_history(db: Session, user: User) -> list[dict]:
    """Obtiene todo el historial de periodos del alumno preservando el progreso."""
    periods = db.query(AcademicPeriod).filter(
        AcademicPeriod.user_id == user.id
    ).order_by(AcademicPeriod.calendar_year.asc(), AcademicPeriod.year_level.asc()).all()

    history = []
    for p in periods:
        history.append({
            "id": p.id,
            "year_level": p.year_level,
            "calendar_year": p.calendar_year,
            "status": p.status,
            "final_progress": int(p.final_progress),
            "created_at": p.created_at.strftime("%d/%m/%Y") if p.created_at else "",
            "completed_at": p.completed_at.strftime("%d/%m/%Y") if p.completed_at else ""
        })
    return history

def promote_student(db: Session, user: User, target_year: int) -> AcademicPeriod:
    """Promueve al estudiante a otro ano (ej 5to a 6to) conservando el historial previo."""
    now = datetime.now(timezone.utc)
    # Cerrar periodo actual
    current_period = get_active_period(db, user)
    current_period.status = "completed"
    current_period.completed_at = now

    # Actualizar usuario
    user.current_year = target_year
    user.updated_at = now

    # Crear nuevo periodo
    new_period = AcademicPeriod(
        user_id=user.id,
        year_level=target_year,
        calendar_year=now.year,
        status="active",
        final_progress=0.0,
        created_at=now
    )
    db.add(new_period)
    db.flush()

    # Inicializar temas del nuevo ano
    new_modules = db.query(Module).filter(Module.year_level == target_year).all()
    for mod in new_modules:
        for t in mod.topics:
            prog = TopicProgress(
                user_id=user.id,
                period_id=new_period.id,
                topic_id=t.id,
                status="available",
                completion_percent=0.0,
                last_activity=now
            )
            db.add(prog)

    db.commit()
    db.refresh(new_period)
    return new_period
