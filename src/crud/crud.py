from sqlalchemy.orm import Session
from models.models import Audiobook
from schemas.schemas import AudiobookCreate
from uuid import UUID

def create_audiobook(db: Session, audiobook: AudiobookCreate):
    db_audiobook = Audiobook(**audiobook.dict())
    db.add(db_audiobook)
    db.commit()
    db.refresh(db_audiobook)
    return db_audiobook

def get_all_audiobooks(db: Session):
    return db.query(Audiobook).all()

def get_audiobook(db: Session, audiobook_id: UUID):
    return db.query(Audiobook).filter(Audiobook.id == audiobook_id).first()

def update_audiobook(db: Session, audiobook_id: UUID, audiobook_data: dict):
    audiobook = db.query(Audiobook).filter(Audiobook.id == audiobook_id).first()
    if audiobook:
        for key, value in audiobook_data.items():
            setattr(audiobook, key, value)
        db.commit()
        db.refresh(audiobook)
    return audiobook

def update_audiobook_end_date(db: Session, audiobook_id: UUID, end_date):
    audiobook = db.query(Audiobook).filter(Audiobook.id == audiobook_id).first()
    if audiobook:
        audiobook.end_date = end_date
        db.commit()
        db.refresh(audiobook)
    return audiobook

def upload_cover_image(db: Session, audiobook_id: UUID, image_data: bytes):
    audiobook = db.query(Audiobook).filter(Audiobook.id == audiobook_id).first()
    if audiobook:
        audiobook.cover_image = image_data
        db.commit()
        db.refresh(audiobook)
    return audiobook

def get_cover_image(db: Session, audiobook_id: UUID):
    audiobook = get_audiobook(db, audiobook_id)
    if audiobook and audiobook.cover_image:
        return audiobook.cover_image
    return None
def delete_audiobook(db: Session, audiobook_id: UUID):
    audiobook = db.query(Audiobook).filter(Audiobook.id == audiobook_id).first()
    if audiobook:
        db.delete(audiobook)
        db.commit()
        return True
    return False