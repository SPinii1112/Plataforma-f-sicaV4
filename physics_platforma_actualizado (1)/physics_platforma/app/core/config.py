import os
import secrets
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

def _get_or_create_secret_key() -> str:
    env_key = os.getenv("SECRET_KEY")
    if env_key and env_key != "fallback_secret_key_needs_change_in_prod":
        return env_key
    
    key_file = BASE_DIR / "data" / ".secret_key"
    if key_file.exists():
        return key_file.read_text(encoding="utf-8").strip()
    
    # Generar una clave criptografica segura aleatoria y guardarla localmente
    new_key = secrets.token_hex(32)
    key_file.parent.mkdir(parents=True, exist_ok=True)
    key_file.write_text(new_key, encoding="utf-8")
    return new_key

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "PhysicsLab Uruguay")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    SECRET_KEY: str = _get_or_create_secret_key()
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/physics.db")

settings = Settings()

