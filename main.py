# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from piccolo.engine import engine_finder

from auth.endpoints.router import router as auth_router
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = engine_finder()
    await engine.start_connection_pool()
    try:
        yield
    finally:
        await engine.close_connection_pool()

app = FastAPI(
    title="gshbe API",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/swagger",
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
