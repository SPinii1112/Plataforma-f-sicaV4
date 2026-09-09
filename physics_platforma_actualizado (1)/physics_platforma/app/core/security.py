from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

# Configuracion recomendada de Argon2id
ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,  # 64 MB
    parallelism=4,
    hash_len=32,
    salt_len=16
)

def hash_password(password: str) -> str:
    """Calcula el hash seguro de la contrasena con Argon2id."""
    return ph.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """Verifica de forma segura la contrasena contra el hash Argon2id."""
    try:
        return ph.verify(hashed_password, password)
    except (VerifyMismatchError, VerificationError):
        return False

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Genera un JWT firmado con los datos del usuario."""
    to_encode = data.copy()
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": now})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str) -> dict | None:
    """Decodifica y valida la firma y expiracion del JWT."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
