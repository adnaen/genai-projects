from typing import Tuple
from pathlib import Path


class Settings:
    BASE_PATH: Path = Path(__file__).resolve().parents[1]
    ARTIFCATS_PATH: Path = BASE_PATH / "artifacts"

    ALLOWED_FILE_TYPES: Tuple[str, str] = ("pdf", "docx")


settings = Settings()
