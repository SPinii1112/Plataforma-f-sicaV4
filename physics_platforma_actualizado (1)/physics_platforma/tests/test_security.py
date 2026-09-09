from app.core.security import hash_password, verify_password, create_access_token, decode_access_token

def test_argon2id_hashing_security():
    plain = "contrasena123"
    hashed = hash_password(plain)

    # 1. Nunca debe ser igual al texto plano
    assert hashed != plain
    assert "$" in hashed

    # 2. La verificacion segura debe dar True
    assert verify_password(plain, hashed) is True

    # 3. Otra contrasena debe dar False
    assert verify_password("otra_clave_incorrecta", hashed) is False

def test_jwt_token_creation_and_decode():
    data = {"sub": "42", "username": "Spini", "role": "student"}
    token = create_access_token(data)
    assert isinstance(token, str)

    payload = decode_access_token(token)
    assert payload is not None
    assert payload["sub"] == "42"
    assert payload["username"] == "Spini"
    assert payload["role"] == "student"
