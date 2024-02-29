from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)
# pytest --cov=. --cov-fail-under=90
# def coverage = sh(script: "docker run juegnadojenkins pytest --junitxml=./test.xml --cov=. --cov-fail-under=90 | grep TOTAL | awk '{ print \$4 }'", returnStdout: true).trim()
# echo coverage -v ./app:/app 
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}