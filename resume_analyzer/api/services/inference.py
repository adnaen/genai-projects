from pathlib import Path
from langchain_community.chat_models.llamacpp import ChatLlamaCpp
from langchain.prompts import ChatPromptTemplate
from api.core.settings import settings


class LLMInferenceManager:
    def __init__(self) -> None:
        self.llm = ChatLlamaCpp(
            verbose=False,
            model_path=str(settings.MODEL_PATH / settings.MODEL_NAME),
            n_threads=settings.N_THREADS,
            top_k=settings.TOP_K,
            top_p=settings.TOP_P,
            n_ctx=settings.N_CTX,
            temperature=settings.TEMPERATURE,
            streaming=False,
        )

    def _settings_up_prompt(self) -> ChatPromptTemplate:
        prompt_template = ChatPromptTemplate.from_messages(
            messages=[
                (
                    "system",
                    """You are a professional resume analyst.

                        Given a resume and a job description, assess the resume in the following areas and return insights in percentage format only:

                        INSIGHTS  
                        - keywords: (match percentage)%  
                        - content quality: (clarity and relevance percentage)%  
                        - structure/order: (logical flow and formatting percentage)%

                        Do not include any additional commentary. Only return the formatted insight output.""",
                ),
                (
                    "user",
                    "Here is the job role: {description}.\nHere is the resume content: {resume_content}.",
                ),
            ]
        )
        return prompt_template

    def ask(self, resume_content: str, description: str | None = None) -> str:
        prompt_template = self._settings_up_prompt()
        chain = prompt_template | self.llm
        result = chain.invoke(
            {
                "resume_content": resume_content,
                "description": description if description else "fetch it from resume",
            }
        )
        return result.content
