from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from search_with_documents.routes import router
from search_with_documents.db import Base, engine

Base.metadata.create_all(bind=engine)  # migrate all models.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
