import os
from fastapi import APIRouter, Depends, UploadFile, HTTPException, status
from sqlalchemy.util import is_exit_exception
from search_with_documents.settings import settings
from search_with_documents.models import FileMetaData
from search_with_documents.db import get_session
from search_with_documents.schemas import FileMetaDataRead


router = APIRouter()


@router.post("/file", response_model=FileMetaDataRead)
async def file_upload(file: UploadFile, session=Depends(get_session)):
    ext = file.filename.split(".")[1]

    if ext not in settings.ALLOWED_FILES:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"unsupported file {file.filename}, only support  {settings.ALLOWED_FILES}",
        )
    is_exisist = (
        session.query(FileMetaData).filter(FileMetaData.name == file.filename).first()
    )

    if is_exisist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="file already exisit."
        )
    try:
        upload_path = settings.UPLOAD_PATH / str(file.filename)
        os.makedirs(upload_path.parent, exist_ok=True)
        with open(upload_path, "wb") as f:
            f.write(file.file.read())

        new_file = FileMetaData(name=file.filename, type=ext)
        session.add(new_file)
        session.commit()
        return new_file
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error : {e}"
        )


@router.get("/file", response_model=list[FileMetaDataRead])
def read_file_metadata(session=Depends(get_session)):
    try:
        return session.query(FileMetaData).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"error : {e}"
        )
