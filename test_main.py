from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_descriptive():
    response = client.post("/descriptive", json={"data": [1, 2, 3, 4, 5]})

    assert response.status_code == 200
    assert response.json() == {
        "mean": 3.0,
        "median": 3.0,
        "variance": 2.5,
        "standard_deviation": 1.5811388300841898,
        "min": 1.0,
        "max": 5.0,
        "range": 4.0,
        "q1": 2,
        "q2": 3,
        "q3": 4
    }
