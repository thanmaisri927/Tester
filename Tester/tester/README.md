# tester

This FastAPI project is intentionally vulnerable for a cybersecurity hackathon demonstration.

## Features

- Hardcoded secrets
- SQL injection in the user lookup flow
- Plaintext password handling
- Sensitive data exposure via debug and admin endpoints
- Path traversal in the file reader endpoint
- Weak authentication
- Debug mode enabled
- No input validation
- Unsafe exception handling
- A failing pytest test

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. Open http://127.0.0.1:8000/docs for the Swagger UI.

## Run tests

```bash
pytest -q
```
