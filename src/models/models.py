import uuid
from sqlalchemy import Column, String, Date, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from database.database import Base
from pydantic import BaseModel
from datetime import date
from typing import Optional

class Audiobook(Base):
    __tablename__ = "audiobooks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True, nullable=False)
    author = Column(String, nullable=False)
    length = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    cover_image = Column(LargeBinary, nullable=True)  # Store image as binary data

class AudiobookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    length: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class EndDateUpdate(BaseModel):
    end_date: date