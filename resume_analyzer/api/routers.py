import os
from fastapi import APIRouter, HTTPException, Request, UploadFile, status
from api.core.settings import settings
from api.services import fetch_resume


router = APIRouter(tags=["Analyzer"])


@router.post("/analyze")
def analyze_resume_(request: Request, file: UploadFile):
    ext = file.filename.split(".")[1]
    if not ext in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File format only support : {settings.ALLOWED_FILE_TYPES} but Got {ext} instead",
        )

    os.makedirs(settings.ARTIFCATS_PATH, exist_ok=True)
    with open(str(settings.ARTIFCATS_PATH / file.filename), "wb") as f:
        f.write(file.file.read())

    content = fetch_resume(
        file_path=settings.ARTIFCATS_PATH / file.filename, file_type=ext
    )
    return {"content": content}
