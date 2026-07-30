from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud import apartment as crud
from app.dependencies import get_db
from app.schemas.apartment import ApartmentCreate, ApartmentResponse

router = APIRouter(
    prefix="/apartments",
    tags=["Apartments"],
)


@router.get("/", response_model=list[ApartmentResponse])
def list_apartments(
    db: Session = Depends(get_db),
) -> list[ApartmentResponse]:
    return crud.get_apartments(db)


@router.post("/", response_model=ApartmentResponse, status_code=201)
def create_apartment(
    apartment: ApartmentCreate,
    db: Session = Depends(get_db),
) -> ApartmentResponse:
    return crud.create_apartment(db, apartment)
