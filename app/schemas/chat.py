from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class IngestRequest(BaseModel):
    document_text: str = Field(..., description="Raw text content to chunk and index")
    metadata: Optional[Dict[str, Any]] = Field(default={}, description="Arbitrary metadata key-values")

class IngestResponse(BaseModel):
    status: str
    chunks_created: int
    message: str

class ChatRequest(BaseModel):
    session_id: str = Field(default="default_session", description="Unique session identifier for conversation history")
    message: str = Field(..., description="User query or prompt")

class SourceNode(BaseModel):
    text: str
    source: str
    score: float

class ChatResponse(BaseModel):
    session_id: str
    response: str
    sources: List[SourceNode]
    latency_ms: int