from app.core.db.models.knowledge_base_model import KnowledgeBaseModel
from app.core.db.connections.postgres import get_db

class KnowledgeBaseRepository:
    
    def fetch_latest_knowledge_base(self):
        with get_db() as db:
            return (
                db.query(KnowledgeBaseModel)
                .order_by(KnowledgeBaseModel.created_on.desc())
                .first()
            )