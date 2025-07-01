from app.core.db.models.conversation_model import ConversationModel
from app.core.db.connections.postgres import get_db

class ConversationRepository:

    def save_conversation(self, user_query: str, llm_response: str):
        with get_db() as db:
            conversation = ConversationModel(
                user_query=user_query,
                llm_response=llm_response
            )
            db.add(conversation)
            db.commit()
            db.refresh(conversation)
            return conversation

    def get_all_conversations(self):
        with get_db() as db:
            return db.query(ConversationModel).order_by(ConversationModel.created_on.desc()).all()
