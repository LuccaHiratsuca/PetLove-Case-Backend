import uvicorn
from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api.routes import router

setup_logging()
app = FastAPI(title="Petlove Sales Assistant")

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=3000, reload=True)
