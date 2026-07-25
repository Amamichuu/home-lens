from fastapi import FastAPI

from app.routers.apartments import router as apartment_router

app = FastAPI(
    title="HomeLens API",
    description="Backend API for HomeLens.",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(apartment_router)
