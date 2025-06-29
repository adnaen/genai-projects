from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from search_with_documents.routes import router
from search_with_documents.db import Base, engine
from search_with_documents.rag import VectorStoreManager, LLMInferenceManager

Base.metadata.create_all(bind=engine)  # migrate all models.


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("setup vector store ⌛")
    app.state.vector_store_manager = VectorStoreManager()
    print("vector store setup completed.✅")

    print("setup LLM inference ⌛")
    app.state.llm_manager = LLMInferenceManager()
    print("LLM inference setup completed.✅")

    yield
    print("app closed ❌")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api/v1")
