import pytest
from pydantic import ValidationError

from app.schemas.apartment import ApartmentCreate


def test_should_create_apartment():
    # Arrange
    apartment_data = {
        "title": "Nice apartment",
        "price": 1200,
        "location": "Lisbon",
    }

    # Act
    apartment = ApartmentCreate(**apartment_data)

    # Assert
    assert apartment.title == "Nice apartment"
    assert apartment.price == 1200
    assert apartment.location == "Lisbon"


def test_apartment_requires_basic_information():
    with pytest.raises(ValidationError):
        ApartmentCreate()
