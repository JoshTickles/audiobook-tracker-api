from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.models import Base
from database.database import engine
from api.endpoints import router as api_router

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add more origins as needed
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router from endpoints
app.include_router(api_router)

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)