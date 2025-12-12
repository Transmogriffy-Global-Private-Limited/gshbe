# app/auth/logic/tokens.py
from datetime import datetime, timedelta, timezone
from jose import jwt

# Put these in env later:
JWT_SECRET = "CHANGE_ME"
JWT_ALG = "HS256"
JWT_EXPIRES_MIN = 60 * 24  # 24h

def create_access_token(*, sub: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=JWT_EXPIRES_MIN)).timestamp()),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def decode_access_token(token: str) -> dict:
    # raises JWTError on invalid/expired token
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
