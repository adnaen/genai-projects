from fastapi import FastAPI
from search_with_documents.routes import router
from search_with_documents.db import Base, engine

Base.metadata.create_all(bind=engine)  # migrate all models.

app = FastAPI()

app.include_router(router, prefix="/api/v1")
