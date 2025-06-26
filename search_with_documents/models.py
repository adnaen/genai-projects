import uuid
from datetime import datetime
from sqlalchemy import Column, UUID, VARCHAR, DATETIME
from search_with_documents.db import Base


class FileMetaData(Base):
    __tablename__ = "filemetadatas"

    id = Column(UUID, primary_key=True, default=uuid.uuid1)
    name = Column(VARCHAR(length=20), nullable=False, unique=False)
    type = Column(VARCHAR(length=10), nullable=False, unique=False)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now)
