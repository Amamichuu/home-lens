from fastapi import FastAPI

app = FastAPI(
    title="HomeLens API",
    description="Backend API for HomeLens.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}