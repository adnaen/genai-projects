from typing import Literal, List
from pathlib import Path
from langchain_core.documents import Document
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders.base import BaseLoader
from langchain.document_loaders.word_document import Docx2txtLoader


def _get_loaders(
    file_path: str | Path, file_type: Literal["pdf", "docx"]
) -> BaseLoader:
    match file_type:
        case "pdf":
            return PyPDFLoader(file_path=file_path)

        case "docx":
            return Docx2txtLoader(file_path=file_path)


def analyze(file_path: str | Path, file_type: Literal["pdf", "docx"]) -> List[Document]:
    loader = _get_loaders(file_path=file_path, file_type=file_type)
    content = loader.load()
    return content
