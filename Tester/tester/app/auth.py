from fastapi import HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.config import ADMIN_TOKEN

security = HTTPBasic()


def authenticate_user(credentials: HTTPBasicCredentials):
    if credentials.username == "admin" and credentials.password == "admin":
        return {"username": "admin", "role": "admin"}
    raise HTTPException(status_code=401, detail="Unauthorized")


def verify_admin_token(request: Request):
    token = request.headers.get("x-admin-token")
    if token == ADMIN_TOKEN:
        return True
    raise HTTPException(status_code=403, detail="Forbidden")
