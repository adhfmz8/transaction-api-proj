from fastapi.testclient import TestClient
from main import app  # Import your app

client = TestClient(app)


def test_get_all_transactions():
    response = client.get("/api/v1/transaction")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_transaction():
    new_transaction = {"name": "Test Transaction", "cost": 100}
    response = client.post("/api/v1/transaction", json=new_transaction)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test Transaction"
    assert data["cost"] == 100


def test_get_transaction():
    # First, create a transaction to get
    new_transaction = {"name": "Get Transaction", "cost": 50}
    post_response = client.post("/api/v1/transaction", json=new_transaction)
    transaction_id = post_response.json()["id"]

    response = client.get(f"/api/v1/transaction/{transaction_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["name"] == "Get Transaction"
    assert data["cost"] == 50.0

    # Test non-existent transaction
    response = client.get("/api/v1/transaction/9999")
    assert response.status_code == 404


def test_update_transaction():
    # Create transaction to update
    new_transaction = {"name": "Update Transaction", "cost": 25}
    post_response = client.post("/api/v1/transaction", json=new_transaction)
    transaction_id = post_response.json()["id"]

    # Update transaction
    update_data = {"name": "Updated Transaction", "cost": 75}
    response = client.put(f"/api/v1/transaction/{transaction_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["name"] == "Updated Transaction"
    assert data["cost"] == 75

    # Test updating non-existent transaction
    response = client.put("/api/v1/transaction/9999", json=update_data)
    assert response.status_code == 404

    # Test partial update
    partial_update = {"name": "Partially Updated"}
    response = client.put(f"/api/v1/transaction/{transaction_id}", json=partial_update)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Partially Updated"
    assert data["cost"] == 75  # Cost remains unchanged
