from fastapi import FastAPI
from api.handlers import router as handlers_router

app = FastAPI()
app.include_router(handlers_router, prefix="/api")