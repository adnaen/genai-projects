from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class FileMetaDataRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    type: str
    created_at: datetime
