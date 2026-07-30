# Changelog

## Sprint 4 - Database Integration

### Added

- PostgreSQL integration using SQLAlchemy.
- Alembic database migrations.
- Database session dependency (`get_db`).
- SQLAlchemy CRUD layer for apartments.

### Changed

- Replaced in-memory storage with PostgreSQL persistence.
- Refactored apartment schemas into `ApartmentCreate` and `ApartmentResponse`.
- Updated API tests to use the database.

---

## Sprint 3 - Apartment API

### Added

- POST `/apartments`
- GET `/apartments`
- Apartment router
- In-memory storage
- API tests

---

## Sprint 2 - Apartment Domain

### Added

- Apartment domain schema
- Domain documentation
- Schema validation tests

---

## Sprint 1 - Project Foundation

### Added

- FastAPI
- uv
- Ruff
- Pytest
- Initial project structure