from typing import Tuple
from pathlib import Path


class Settings:
    BASE_PATH: Path = Path(__file__).resolve().parents[1]
    ARTIFCATS_PATH: Path = BASE_PATH / "artifacts"

    ALLOWED_FILE_TYPES: Tuple[str, str] = ("pdf", "docx")

    MODEL_PATH: Path = Path(__file__).resolve().parents[3] / "models"
    MODEL_NAME: str = "tinyllama_1_1b_chat_v1_0_gguf.gguf"

    TOP_K: int = 40
    TOP_P: float = 0.96
    TEMPERATURE: float = 0.8
    N_THREADS: int = 3
    N_CTX: int = 2048


settings = Settings()
