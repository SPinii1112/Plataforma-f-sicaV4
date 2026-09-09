from fastapi import Request, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database.engine import get_db
from app.database.models import User
from app.core.security import decode_access_token

def get_token_from_request(request: Request) -> str | None:
    # 1. Buscar en cookie HttpOnly
    token = request.cookies.get("access_token")
    if token:
        return token
    # 2. Fallback a header Authorization: Bearer <token>
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:].strip()
    return None

def get_current_user_optional(request: Request, db: Session = Depends(get_db)) -> User | None:
    token = get_token_from_request(request)
    if not token:
        return None
    payload = decode_access_token(token)
    if not payload:
        return None
    user_id = payload.get("sub")
    if not user_id:
        return None
    user = db.query(User).filter(User.id == int(user_id)).first()
    return user

def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    user = get_current_user_optional(request, db)
    if not user:
        # Si es peticion API (acepta json), devolver 401
        accept = request.headers.get("accept", "")
        if "application/json" in accept and "text/html" not in accept:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No autenticado"
            )
        # Si es navegacion web, redirigir a login
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            headers={"Location": "/auth/login"}
        )
    return user

def require_role(*allowed_roles: str):
    def role_checker(user: User = Depends(get_current_user)) -> User:
        if user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a esta seccion"
            )
        return user
    return role_checker
