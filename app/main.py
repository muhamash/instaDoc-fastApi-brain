from fastapi import FastAPI

from app.api.v1.endpoints import router as doc_router

app = FastAPI(title="InstaDoc doc generation app")
app.include_router(doc_router, prefix="/api/v1")
