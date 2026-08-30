from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Agentic LLM RAG Service"
    PINECONE_API_KEY: str = "mock_pinecone_key"
    PINECONE_ENVIRONMENT: str = "us-east-1-aws"
    PINECONE_INDEX_NAME: str = "enterprise-knowledge"
    GROQ_API_KEY: str = "mock_groq_key"
    MODEL_NAME: str = "llama3-70b-8192"
    EMBEDDING_MODEL_NAME: str = "sentence-transformers/all-MiniLM-L6-v2"
    TOP_K_RESULTS: int = 4
    SIMILARITY_THRESHOLD: float = 0.75

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()