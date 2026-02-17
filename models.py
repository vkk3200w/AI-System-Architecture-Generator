from pydantic import BaseModel
from typing import Optional

class ArchitectureRequest(BaseModel):
    app_description: str
    api_key: Optional[str] = None # Optional API key if user wants to use their own

class ArchitectureResponse(BaseModel):
    frontend: str
    backend: str
    database: str
    cache: str
    queue: str
    storage: str
    auth: str
    deployment: str
    explanation: str
