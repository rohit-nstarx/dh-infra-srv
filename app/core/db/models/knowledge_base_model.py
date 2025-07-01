from sqlalchemy import Column, String, BigInteger, Boolean, JSON, DateTime
from app.core.db.connections.postgres import Base
from datetime import datetime

class KnowledgeBaseModel(Base):
    __tablename__ = 'knowledge_bases'

    id = Column(String, primary_key=True)  # e.g., "KB0001"
    collection_name = Column(String, nullable=False)
    documents = Column(JSON, nullable=False)  # stores {"count": 114, "items": [...]}
    type = Column(String)
    description = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "collection_name": self.collection_name,
            "documents": self.documents,
            "type": self.type,
            "description": self.description,
            "created_on": self.created_on.isoformat() if self.created_on else None
        }

    def __repr__(self):
        return (
            f"<KnowledgeBaseModel(id={self.id}, collection_name={self.collection_name}, "
            f"documents={self.documents}, type={self.type}, "
            f"description={self.description}, created_on={self.created_on})>"
        )