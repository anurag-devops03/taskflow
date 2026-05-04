from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSignup(BaseModel):
    email: EmailStr
    username: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "anurag@example.com",
                "username": "anurag",
                "password": "securepassword123"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "anurag@example.com",
                "password": "securepassword123"
            }
        }

class UserResponse(BaseModel):
    id: str
    email: str
    username: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
