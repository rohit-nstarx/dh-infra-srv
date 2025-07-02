from fastapi import APIRouter
from app.schema.base import ConversationCreate
from app.core.db.repository.conversation_repository import ConversationRepository

conversation_router = APIRouter()
repo = ConversationRepository()


@conversation_router.post("/conversations")
def save_conversation(convo: ConversationCreate):
    saved = repo.save_conversation(convo.user_query, convo.llm_response)
    return {"message": "Conversation saved"}


@conversation_router.get("/conversations")
def save_conversation():
    conversations = repo.get_all_conversations()
    return {"data": conversations}
