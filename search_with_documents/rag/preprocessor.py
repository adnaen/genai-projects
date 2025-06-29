from typing import Any, List
from langchain_core.documents import Document
from search_with_documents.settings import settings


def _get_loader(doc_path: str) -> Any:
    ext = doc_path.split(".")[1]

    match ext:
        case "txt" | "md":
            from langchain_community.document_loaders import TextLoader

            return TextLoader

        case "pdf":
            from langchain_community.document_loaders import PyPDFLoader

            return PyPDFLoader

        case _:
            raise ValueError(f"un supported file {ext}")


def load_doc(doc_path: str, file_id: str) -> List[Document]:
    loader_cls = _get_loader(doc_path=doc_path)
    loader = loader_cls(str(settings.UPLOAD_PATH / doc_path))
    docs = loader.load()
    for doc in docs:
        doc.metadata["file_id"] = file_id

    return docs


def get_chunks(docs: List[Document]) -> List[Document]:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.split_documents(docs)
