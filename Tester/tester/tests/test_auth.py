from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_is_not_secure():
    response = client.get("/login", params={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    assert response.json()["token"] == "secure-token"
