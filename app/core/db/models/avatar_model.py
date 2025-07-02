from sqlalchemy import Column, String, BigInteger, Boolean
from app.core.db.connections.postgres import Base


class AvatarModel(Base):
    __tablename__ = "avatars"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String)
    image_url = Column(String)
    role = Column(String)
    language = Column(String)
    voice_id = Column(String)
    description = Column(String)
    personality = Column(String)
    is_active = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "role": self.role,
            "language": self.language,
            "voice_id": self.voice_id,
            "description": self.description,
            "personality": self.personality,
            "is_active": self.is_active,
        }

    def __repr__(self):
        return (
            f"<AvatarModel(id={self.id}, name={self.name}, image_url={self.image_url}, role={self.role}, "
            f"language={self.language}, voice_id={self.voice_id}, "
            f"description={self.description}, personality={self.personality}, "
            f"is_active={self.is_active})>"
        )
