from database.database import SessionLocal
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from config import API_KEY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

api_key_header = APIKeyHeader(name="access_token", auto_error=False)

async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    else:
        raise HTTPException(status_code=404, detail="Not Found")