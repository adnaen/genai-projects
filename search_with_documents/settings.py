from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_PATH: Path = Path(__file__).resolve().parent
    UPLOAD_PATH: Path = BASE_PATH / "uploads"
    CHROMA_PATH: Path = BASE_PATH / "chroma"
    MODEL_PATH: Path = Path(__file__).resolve().parents[2] / "models"

    ALLOWED_FILES: List[str] = ["pdf", "txt", "md"]

    CHROMA_COLLECTION_NAME: str = "document_searcher"
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"

    SQLITE_URI: str = "sqlite:///./search_with_documents/database.db"

    # llm config
    MODEL_DOWNLOAD_URL: str = (
        "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf?download=true"
    )

    LLM_NAME: str = "tinyllama_1_1b_chat_v1_0_gguf.gguf"
    TOP_P: float = 0.9
    TOP_K: int = 50
    TEMPERATURE: float = 0.8
    N_THREADS: int = 3  # no.of cores - 1
    MAX_TOKENS: int = 2000
    N_CTX: int = 2048


settings = Settings()
