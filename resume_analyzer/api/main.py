from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import router as analyze_router

app = FastAPI()
app.include_router(analyze_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
