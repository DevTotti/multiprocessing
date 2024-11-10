from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_aggregate_data():
    response = client.get("/aggregate-data")
    assert response.status_code == 200
    data = response.json()
    assert "animals" in data
    assert "countries" in data
    assert "sports" in data


def test_rate_limit():
    for _ in range(99):
        response = client.get("/aggregate-data")
        assert response.status_code == 200
    
    response = client.get("/aggregate-data")
    assert response.status_code == 429