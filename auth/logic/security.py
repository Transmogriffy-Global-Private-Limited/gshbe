# app/auth/logic/security.py
from datetime import datetime, timedelta
from typing import Dict

from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "bd0c71b86d63ca6579656f7edc0670f9c8b2f0b309e859927b024607fbe63090358eaf0a4af5664f6e1de46ccd393ab916088a941a69d0320f6286f6fb3aca6e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: Dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
