from uuid import uuid1
from typing import Tuple
from chromadb import PersistentClient
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from search_with_documents.settings import settings
from search_with_documents.rag.preprocessor import get_chunks, load_doc


class VectorStoreManager:
    def __init__(self, collection_name: str = settings.CHROMA_COLLECTION_NAME) -> None:
        self.client = PersistentClient(path=settings.CHROMA_PATH)
        self.collection = self.client.get_or_create_collection(name=collection_name)
        self.embdder = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)
        self.lang_client = Chroma(
            client=self.client,
            collection_name=collection_name,
            persist_directory=str(settings.CHROMA_PATH),
            embedding_function=self.embdder,
        )

    def add_new_document(self, doc_path: str, file_id: str) -> Tuple[bool, str]:
        try:
            docs = load_doc(doc_path=doc_path, file_id=file_id)
            chunks = get_chunks(docs=docs)
            ids = [str(uuid1()) for _ in chunks]
            self.lang_client.add_documents(documents=chunks, ids=ids)
            return True, "documents added successfully!"
        except Exception as e:
            return False, str(e)

    def retriever(self, query: str, file_id: str) -> str:
        try:
            result = self.lang_client.similarity_search(
                query=query, filter={"file_id": file_id}, k=2
            )

            cleaned = " ".join(
                [" ".join(each.page_content.split("\n")) for each in result]
            )
            return cleaned
        except Exception as e:
            print(f"error on {e}")
            return ""
