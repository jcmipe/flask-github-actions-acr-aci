from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_expected_json():
    client = app.test_client()
    response = client.get("/")
    data = response.get_json()

    assert data["status"] == "ok"
    assert "GitHub Actions" in data["message"]


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
