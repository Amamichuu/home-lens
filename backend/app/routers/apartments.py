from fastapi import APIRouter

from app.schemas.apartment import Apartment
from app.storage import apartments

router = APIRouter(prefix="/apartments", tags=["Apartments"])


@router.get("/", response_model=list[Apartment])
def list_apartments() -> list[Apartment]:
    return apartments


@router.post("/", response_model=Apartment, status_code=201)
def create_apartment(apartment: Apartment) -> Apartment:
    apartments.append(apartment)
    return apartment
