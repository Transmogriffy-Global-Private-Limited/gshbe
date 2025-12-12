# app/auth/logic/deps.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from auth.logic.tokens import decode_access_token

bearer = HTTPBearer(auto_error=True)

def get_current_account_id(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
) -> str:
    try:
        payload = decode_access_token(creds.credentials)
        sub = payload.get("sub")
        if not sub:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return str(sub)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
