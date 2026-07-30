from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.apartment import Apartment
from app.schemas.apartment import ApartmentCreate


def create_apartment(
    db: Session,
    apartment: ApartmentCreate,
) -> Apartment:
    db_apartment = Apartment(
        title=apartment.title,
        price=apartment.price,
        location=apartment.location,
    )

    db.add(db_apartment)
    db.commit()
    db.refresh(db_apartment)

    return db_apartment


def get_apartments(db: Session) -> list[Apartment]:
    return list(db.scalars(select(Apartment)))
