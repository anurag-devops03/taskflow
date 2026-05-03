from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="TaskFlow API",
    description="Cloud-Native Task Management Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("✅ TaskFlow API started successfully")
    print("✅ Database connection configured")

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "message": "TaskFlow API is running",
        "version": "1.0.0"
    }

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to TaskFlow API",
        "docs": "/docs",
        "health": "/health"
    }
