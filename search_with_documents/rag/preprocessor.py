from typing import Any, List
from langchain_core.documents import Document


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


def load_doc(doc_path: str) -> List[Document]:
    loader_cls = _get_loader(doc_path=doc_path)
    loader = loader_cls(doc_path)
    return loader.load()


def get_chunks(docs: List[Document]) -> List[Document]:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " ", ""],
        chunk_size=500,
        chunk_overlap=100,
    )
    return splitter.split_documents(docs)
