from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import ArchitectureRequest, ArchitectureResponse
from services.architecture_service import generate_architecture

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI System Architecture Generator")

# CORS Configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


# CORS Configuration (FIXED)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "AI System Architecture Generator API is running."}

@app.post("/generate-architecture", response_model=ArchitectureResponse)
def generate_architecture_endpoint(request: ArchitectureRequest):
    try:
        # Use provided API key or fall back to environment variable
        api_key = request.api_key or os.getenv("GOOGLE_API_KEY")
        
        response = generate_architecture(request.app_description, api_key)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
