from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main():
    response = client.get("/api/v1/transaction")
    assert response.status_code == 200
