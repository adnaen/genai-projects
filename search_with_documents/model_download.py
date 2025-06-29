import os
import shutil
import requests
from typing import Tuple
from search_with_documents.settings import settings


def download_model() -> Tuple[bool, str]:

    full_path: str = str(settings.MODEL_PATH / settings.LLM_NAME)
    if os.path.exists(full_path):
        return False, "Already exists"

    try:
        print(f"downloading model from {settings.MODEL_DOWNLOAD_URL} ⏱...")
        with requests.get(settings.MODEL_DOWNLOAD_URL, stream=True) as r:
            os.makedirs(settings.MODEL_PATH, exist_ok=True)
            with open(str(settings.MODEL_PATH / settings.LLM_NAME), "wb") as file:
                shutil.copyfileobj(r.raw, file)
        print(f"model download completed, saved in {full_path} ✅")
        return True, full_path

    except Exception as e:
        return False, str(e)
