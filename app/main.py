from fastapi import FastAPI
from app.routes import gpt

app = FastAPI()

app.include_router(gpt.router)
