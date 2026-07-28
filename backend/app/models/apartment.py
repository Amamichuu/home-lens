from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Apartment(Base):
    __tablename__ = "apartments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    location: Mapped[str] = mapped_column(String(255))
