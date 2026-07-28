from app.db.base import Base
from app.db.session import engine

# Import all models so SQLAlchemy can register them.
from app.models.apartment import Apartment  # noqa: F401


def create_tables() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully!")
