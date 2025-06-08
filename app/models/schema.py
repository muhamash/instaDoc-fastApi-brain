from typing import Dict, List

from pydantic import BaseModel


class FileItem(BaseModel):
    path: str
    type: str  # "file" or "dir"
    content: str = ""


class RepoRequest(BaseModel):
    repo_name: str
    structure: List[FileItem]


class RepoDocResponse(BaseModel):
    readme: str
    stack: List[str]
    summaries: Dict[str, str]
