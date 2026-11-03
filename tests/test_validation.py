
import pytest
from app import app, FEATURES

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200

def test_empty_form(client):
    response = client.post("/", data={})
    assert response.status_code == 200
    assert b"Enter a value for WBC." in response.data

def test_invalid_text_input(client):
    data = {feature: "5" for feature in FEATURES}
    data["WBC"] = "abc"

    response = client.post("/", data=data)
    assert response.status_code == 200
    assert b"WBC must be a non-negative number." in response.data

def test_negative_input(client):
    data = {feature: "5" for feature in FEATURES}
    data["PLT"] = "-10"

    response = client.post("/", data=data)
    assert response.status_code == 200
    assert b"PLT must be a non-negative number." in response.data
