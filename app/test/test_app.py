from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)
# pytest --cov=. --cov-fail-under=90
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}