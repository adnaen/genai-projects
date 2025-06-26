from pathlib import Path
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_PATH: Path = Path(__file__).resolve().parent
    ALLOWED_FILES: List[str] = ["pdf", "txt", "md"]
    UPLOAD_PATH: Path = BASE_PATH / "uploads"
    SQLITE_URI: str = "sqlite:///./search_with_documents/database.db"


settings = Settings()
