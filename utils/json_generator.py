import json

structure = [
    {
        "path": "main.py",
        "type": "file",
        "content": """from fastapi import FastAPI

from app.api.v1.endpoints import router as doc_router

app = FastAPI(title="InstaDoc doc generation app")
app.include_router(doc_router, prefix="/api/v1")
""",
    },
    {
        "path": "endpoints.py",
        "type": "file",
        "content": """from fastapi import APIRouter

from app.models.schema import RepoDocResponse, RepoRequest
from app.services.doc_generator import generate_documentation

router = APIRouter()

@router.post("/generate-docs", response_model=RepoDocResponse)
def generate_docs(payload: RepoRequest):
    return generate_documentation(payload)
""",
    },
]

payload = {"repo_name": "fast-api", "structure": structure}

print(json.dumps(payload))
