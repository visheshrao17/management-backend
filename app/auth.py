from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

SECRET_KEY = "your_secret_key"
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token.")
