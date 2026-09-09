from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional

class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2, max_length=100)
    password: str = Field(..., min_length=6, max_length=128)
    current_year: int = Field(..., ge=5, le=6)

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        v = v.strip()
        if not v.isalnum() and "_" not in v and "-" not in v:
            raise ValueError("El usuario solo puede contener letras, numeros y guiones")
        return v

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    full_name: str
    current_year: int
    role: str
    is_active: bool
