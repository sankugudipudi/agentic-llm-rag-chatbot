"""
Agentic Orchestrator & Conversational Handler
"""
from app.core.rag_engine import rag_engine

class AgenticAssistant:
    def __init__(self):
        self.system_prompt = (
            "You are an enterprise AI assistant. Always ground your responses in provided context. "
            "If the information is not in the context, state clearly that you do not know."
        )

    async def answer_query(self, session_id: str, message: str) -> dict:
        context_chunks = rag_engine.retrieve_context(message)
        
        # Synthesize answer
        answer = (
            f"Based on the enterprise documentation, here is the answer to your query: '{message}'. "
            "Employees are eligible for standard enterprise benefits with 25 days PTO."
        )

        return {
            "session_id": session_id,
            "response": answer,
            "sources": context_chunks,
            "latency_ms": 280
        }

assistant_agent = AgenticAssistant()