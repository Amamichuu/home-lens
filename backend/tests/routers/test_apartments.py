from fastapi.testclient import TestClient
from sqlalchemy import delete

from app.db.session import SessionLocal
from app.main import app
from app.models.apartment import Apartment

client = TestClient(app)


def setup_function():
    db = SessionLocal()
    db.execute(delete(Apartment))
    db.commit()
    db.close()


def test_should_create_apartment():
    apartment_data = {
        "title": "Nice apartment",
        "price": 1200,
        "location": "Lisbon",
    }

    response = client.post("/apartments/", json=apartment_data)

    assert response.status_code == 201
    assert response.json()["id"] > 0
    assert response.json()["title"] == apartment_data["title"]
    assert response.json()["price"] == apartment_data["price"]
    assert response.json()["location"] == apartment_data["location"]


def test_should_list_apartments():
    response = client.get("/apartments/")

    assert response.status_code == 200
    assert response.json() == []


def test_should_return_created_apartment():
    apartment_data = {
        "title": "Nice apartment",
        "price": 1200,
        "location": "Lisbon",
    }

    client.post("/apartments/", json=apartment_data)

    response = client.get("/apartments/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == apartment_data["title"]


def test_should_not_create_invalid_apartment():
    response = client.post(
        "/apartments/",
        json={
            "title": "Nice apartment",
        },
    )

    assert response.status_code == 422
