from pydantic import BaseModel
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    
    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str
    
    class Config:
        from_attributes = True
