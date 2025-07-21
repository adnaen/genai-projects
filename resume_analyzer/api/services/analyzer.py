from typing import Literal
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders.word_document import Docx2txtLoader


def _get_loaders(
    file_path: str | Path, file_type: Literal["pdf", "docx"]
) -> BaseLoader:
    match file_type:
        case "pdf":
            return PyPDFLoader(file_path=file_path)

        case "docx":
            return Docx2txtLoader(file_path=file_path)


def analyze(file_path: str | Path, file_type: Literal["pdf", "docx"]) -> str:
    loader = _get_loaders(file_path=file_path, file_type=file_type)
    content = loader.load()
    return content[0].page_content
