from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import router as analyze_router
from api.services.inference import LLMInferenceManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("initializing LLM Inference Class ⏳")
    app.state.llm_inference_manager = LLMInferenceManager()
    print("LLM Inference Class Successfully ✅")
    yield
    print("app was closed.")


app = FastAPI(lifespan=lifespan)
app.include_router(analyze_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
