from fastapi import APIRouter

from app.models.schema import RepoDocResponse, RepoRequest
from app.services.doc_generator import generate_documentation

router = APIRouter()


@router.get("/")
def home_route():
    return {"message": "Hello from InstaDoc FastApi Brain!", "status": "ok"}


@router.post("/generate-docs", response_model=RepoDocResponse)
def generate_docs(payload: RepoRequest):
    return generate_documentation(payload)
