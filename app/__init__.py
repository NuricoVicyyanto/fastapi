from fastapi import FastAPI
from app.api import api_router

app = FastAPI(
    title='FastAPI',
    description='FastAPI is a Python 3.6+ framework for building blazing fast APIs.',
)

app.include_router(api_router)