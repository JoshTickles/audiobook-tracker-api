from datetime import date, time
from pydantic import BaseModel, constr
from typing import Optional
from uuid import UUID

class AudiobookBase(BaseModel):
    title: str
    author: str
    # length: constr(regex=r'^\d{1,3}:\d{2}:\d{2}$')  # Regex for "HH:MM:SS"
    length: str
    start_date: date
    end_date: Optional[date]

class AudiobookCreate(AudiobookBase):
    pass

class AudiobookUpdate(AudiobookBase):
    cover_image: Optional[bytes] = None  

class Audiobook(AudiobookBase):
    id: UUID

    class Config:
        orm_mode = True

class AudiobookResponse(AudiobookBase):
    id: UUID

    class Config:
        orm_mode = True