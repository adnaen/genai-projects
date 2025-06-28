from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_PATH: Path = Path(__file__).resolve().parent
    ALLOWED_FILES: List[str] = ["pdf", "txt", "md"]
    UPLOAD_PATH: Path = BASE_PATH / "uploads"
    CHROMA_PATH: Path = BASE_PATH / "chroma"
    CHROMA_COLLECTION_NAME: str = "document_searcher"
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    SQLITE_URI: str = "sqlite:///./search_with_documents/database.db"


settings = Settings()
