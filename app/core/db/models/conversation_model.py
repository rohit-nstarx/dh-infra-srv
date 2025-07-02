from sqlalchemy import Column, BigInteger, String, Text, DateTime
from datetime import datetime
from app.core.db.connections.postgres import Base


class ConversationModel(Base):
    __tablename__ = "conversations"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_query = Column(Text, nullable=False)
    llm_response = Column(Text, nullable=False)
    created_on = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_query": self.user_query,
            "llm_response": self.llm_response,
            "created_on": self.created_on.isoformat(),
        }

    def __repr__(self):
        return (
            f"<ConversationModel(id={self.id}, user_query={self.user_query[:30]}, "
            f"llm_response={self.llm_response[:30]}, created_on={self.created_on})>"
        )
