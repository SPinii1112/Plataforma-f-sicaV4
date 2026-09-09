# -*- coding: utf-8 -*-
"""
Script de instalacion y arranque inicial de PhysicsLab Uruguay.
Ejecutar: python setup.py
"""
import os
import sys
import secrets
from pathlib import Path

def setup_project():
    print("==================================================")
    print("Configurando PhysicsLab Uruguay...")
    print("==================================================")

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    secret_file = data_dir / ".secret_key"
    if not secret_file.exists():
        new_key = secrets.token_hex(32)
        secret_file.write_text(new_key, encoding="utf-8")
        print(f"[OK] Clave de seguridad generada en: {secret_file}")
    else:
        print(f"[OK] Clave de seguridad existente detectada.")

    # Crear .env si no existe a partir de .env.example
    env_file = Path(".env")
    example_file = Path(".env.example")
    if not env_file.exists() and example_file.exists():
        env_file.write_text(example_file.read_text(encoding="utf-8"), encoding="utf-8")
        print("[OK] Archivo .env inicializado desde .env.example")

    print("\nInicializando base de datos y esquema...")
    try:
        from app.database.engine import engine, Base
        import app.database.models
        Base.metadata.create_all(bind=engine)
        print("[OK] Tablas de base de datos verificadas.")
    except Exception as e:
        print(f"[ERROR] Error al inicializar tablas: {e}")
        return 1

    print("\n¡Proyecto configurado exitosamente!")
    print("Para iniciar el servidor ejecuta:")
    print("    python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000")
    print("==================================================")
    return 0

if __name__ == "__main__":
    sys.exit(setup_project())
