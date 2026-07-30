from pydantic import BaseModel, ConfigDict, Field


class ApartmentBase(BaseModel):
    title: str = Field(description="Apartment title or name")
    price: float = Field(description="Monthly rent price")
    location: str = Field(description="Apartment location")

    area: float | None = Field(
        default=None,
        description="Apartment size in square meters",
    )

    bedrooms: int | None = Field(
        default=None,
        description="Number of bedrooms",
    )

    bathrooms: int | None = Field(
        default=None,
        description="Number of bathrooms",
    )

    url: str | None = Field(
        default=None,
        description="Original listing URL",
    )

    notes: str | None = Field(
        default=None,
        description="Personal notes about the apartment",
    )


class ApartmentCreate(ApartmentBase):
    pass


class ApartmentResponse(ApartmentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
