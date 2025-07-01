from app.core.db.models.avatar_model import AvatarModel
from app.core.db.connections.postgres import get_db

class AvatarRepository:
    
    def fetch_all_avatars(self):
        with get_db() as db:
            return db.query(AvatarModel).all()
    
    def fetch_active_avatar(self):
        with get_db() as db:
            return db.query(AvatarModel).filter(AvatarModel.is_active == True).first()
    
    def fetch_avatar_by_id(self, avatar_id: int):
        print('in fetch avatar')
        with get_db() as db:
            return db.query(AvatarModel).filter(AvatarModel.id == avatar_id).first()
    
    def remove_avatar(self, avatar_id: int):
        with get_db() as db:
            avatar = db.query(AvatarModel).filter(AvatarModel.id == avatar_id).first()
            if avatar:
                db.delete(avatar)
                db.commit()
                return True
            return False
    