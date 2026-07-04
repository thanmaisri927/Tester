import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "hardcoded-secret")
API_KEY = os.getenv("API_KEY", "hardcoded-api-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "admin-token-123")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./demo.db")
