from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="Cloud-Native Task Management Platform",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "TaskFlow API is running"}
