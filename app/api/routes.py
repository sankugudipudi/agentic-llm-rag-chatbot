from fastapi import APIRouter, HTTPException, status
from app.schemas.chat import IngestRequest, IngestResponse, ChatRequest, ChatResponse
from app.core.rag_engine import rag_engine
from app.core.agent import assistant_agent

router = APIRouter()

@router.post("/ingest", response_model=IngestResponse, status_code=status.HTTP_201_CREATED, tags=["Ingestion"])
async def ingest_document(payload: IngestRequest):
    try:
        chunks = rag_engine.chunk_document(payload.document_text, payload.metadata)
        return IngestResponse(
            status="success",
            chunks_created=len(chunks),
            message=f"Successfully indexed {len(chunks)} chunks into Pinecone vector store."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ChatResponse, tags=["Conversational Agent"])
async def chat_interaction(payload: ChatRequest):
    try:
        result = await assistant_agent.answer_query(payload.session_id, payload.message)
        return ChatResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))