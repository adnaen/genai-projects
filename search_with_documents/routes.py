import os
from fastapi import (
    Request,
    Depends,
    APIRouter,
    UploadFile,
    HTTPException,
    status,
)
from search_with_documents.db import get_session
from search_with_documents.settings import settings
from search_with_documents.models import FileMetaData
from search_with_documents.schemas import FileMetaDataRead, Prompt


router = APIRouter()


@router.post("/ask")
async def llm_response(request: Request, prompt: Prompt, session=Depends(get_session)):
    file = session.query(FileMetaData).filter(FileMetaData.id == prompt.file_id).first()
    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="file not found"
        )

    result = request.app.state.vector_store_manager.retriever(
        query=prompt.prompt, file_id=str(prompt.file_id)
    )
    print(result)
    return {"prompt": prompt.prompt, "data": result}


@router.post("/file", response_model=FileMetaDataRead)
async def file_upload(request: Request, file: UploadFile, session=Depends(get_session)):
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
        session.refresh(new_file)

        result = request.app.state.vector_store_manager.add_new_document(
            doc_path=new_file.name, file_id=str(new_file.id)
        )

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
