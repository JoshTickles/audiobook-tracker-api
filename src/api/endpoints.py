from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Response
from sqlalchemy.orm import Session
from sqlalchemy import text
from crud.crud import create_audiobook, get_all_audiobooks, update_audiobook, delete_audiobook, get_audiobook, upload_cover_image, get_cover_image
from schemas.schemas import AudiobookCreate, AudiobookResponse, AudiobookUpdate
from models.models import AudiobookUpdate
from dependencies import get_db, get_api_key
from uuid import UUID


router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Audiobook Tracker API."}

@router.post("/audiobooks/", response_model=AudiobookResponse, dependencies=[Depends(get_api_key)])
def create_audiobook_endpoint(audiobook: AudiobookCreate, db: Session = Depends(get_db)):
    return create_audiobook(db=db, audiobook=audiobook)

@router.get("/audiobooks/", response_model=list[AudiobookResponse], dependencies=[Depends(get_api_key)])
def read_audiobooks(db: Session = Depends(get_db)):
    return get_all_audiobooks(db=db)

@router.get("/audiobooks/{audiobook_id}", response_model=AudiobookResponse)
def read_audiobook(audiobook_id: UUID, db: Session = Depends(get_db)):
    audiobook = get_audiobook(db, audiobook_id)
    if not audiobook:
        raise HTTPException(status_code=404, detail="Audiobook not found")
    return audiobook

@router.put("/audiobooks/{audiobook_id}", response_model=AudiobookResponse, dependencies=[Depends(get_api_key)])
def update_audiobook_endpoint(audiobook_id: UUID, payload: AudiobookUpdate, db: Session = Depends(get_db)):
    update_data = payload.dict(exclude_unset=True)
    audiobook = update_audiobook(db, audiobook_id, update_data)
    if not audiobook:
        raise HTTPException(status_code=404, detail="Audiobook not found")
    return audiobook

@router.post("/audiobooks/{audiobook_id}/cover", dependencies=[Depends(get_api_key)])
def upload_audiobook_cover(audiobook_id: UUID, file: UploadFile = File(...), db: Session = Depends(get_db)):
    allowed_mime_types = ["image/jpeg", "image/png"]
    if file.content_type not in allowed_mime_types:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PNG and JPG are allowed.")
    
    audiobook = get_audiobook(db, audiobook_id)
    if not audiobook:
        raise HTTPException(status_code=404, detail="Audiobook not found")
    cover_image = file.file.read()
    updated_audiobook = upload_cover_image(db, audiobook_id, cover_image)
    if not updated_audiobook:
        raise HTTPException(status_code=404, detail="Error uploading cover image")
    return {"message": "Cover image uploaded successfully"}

@router.get("/audiobooks/{audiobook_id}/cover", dependencies=[Depends(get_api_key)])
def get_audiobook_cover(audiobook_id: UUID, db: Session = Depends(get_db)):
    cover_image = get_cover_image(db, audiobook_id)
    if not cover_image:
        raise HTTPException(status_code=404, detail="Cover image not found")
    return Response(cover_image, media_type="image/jpeg")

@router.delete("/audiobooks/{audiobook_id}", status_code=200, dependencies=[Depends(get_api_key)])
def delete_audiobook_endpoint(audiobook_id: UUID, db: Session = Depends(get_db)):
    success = delete_audiobook(db, audiobook_id)
    if not success:
        raise HTTPException(status_code=404, detail="Audiobook not found")
    return {"detail": "Audiobook deleted successfully"}

@router.get("/health", dependencies=[Depends(get_api_key)])
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": "unhealthy", "details": str(e)})