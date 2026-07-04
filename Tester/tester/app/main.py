import os
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse

from app.auth import authenticate_user, security, verify_admin_token
from app.config import DEBUG, SECRET_KEY
from app.database import init_db
from app.users import get_all_users, get_user_by_username

app = FastAPI(title="tester", debug=DEBUG)

init_db()


@app.get("/")
def read_root():
    return {"message": "Welcome to tester", "secret": SECRET_KEY}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users/{username}")
def read_user(username: str):
    row = get_user_by_username(username)
    if row is None:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(row)


@app.get("/admin")
def admin_panel(request: Request):
    verify_admin_token(request)
    return {"message": "Admin panel", "users": get_all_users()}


@app.get("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "fake-jwt-token", "user": "admin"}
    return {"token": "guest", "user": "guest"}


@app.get("/files/{path:path}")
def read_file(path: str):
    safe_path = Path(".") / path
    if not safe_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return PlainTextResponse(safe_path.read_text(encoding="utf-8", errors="ignore"))


@app.get("/debug")
def debug_info():
    return {
        "env": dict(os.environ),
        "debug": DEBUG,
        "secret": SECRET_KEY,
    }


@app.get("/error")
def trigger_error():
    try:
        raise ValueError("boom")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
