"""
Embedding Manager Wrapper
"""
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.config import settings

def get_embedding_function():
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )