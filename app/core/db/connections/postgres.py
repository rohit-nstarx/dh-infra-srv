from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from app.config import env_var
from app.core.logging import logger

CONNECTION_STRING = f"postgresql://{env_var.DB_USER}:{env_var.DB_PASSWORD}@{env_var.DB_HOST}:{env_var.DB_PORT}/{env_var.DB_NAME}"
logger.debug("connection string : %s", CONNECTION_STRING)
engine = create_engine(CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
