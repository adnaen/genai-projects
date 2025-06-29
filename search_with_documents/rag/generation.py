from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from langchain.prompts import ChatPromptTemplate
from search_with_documents.settings import settings
from search_with_documents.model_download import download_model


class LLMInferenceManager:
    def __init__(self) -> None:
        download_model()

        self.llm = ChatLlamaCpp(
            model_path=str(settings.MODEL_PATH / settings.LLM_NAME),
            top_k=settings.TOP_K,
            top_p=settings.TOP_P,
            streaming=True,
            verbose=False,
            temperature=settings.TEMPERATURE,
            n_threads=settings.N_THREADS,
            max_tokens=settings.MAX_TOKENS,
            n_ctx=settings.N_CTX,
        )

    def inference(self, query: str, context: str):
        prompt = self._setup_chat_template()
        chain = prompt | self.llm
        for each in chain.stream({"query": query, "context": context}):
            yield each.content

    def _setup_chat_template(self) -> ChatPromptTemplate:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful AI assistant. Answer the user's questions only using the given context. "
                    "If the answer is not found in the context, reply with: 'I can't find answer relate to this question, please contact our team.'",
                ),
                ("user", "{context}\n\nQuestion: {query}"),
            ]
        )
        return prompt
