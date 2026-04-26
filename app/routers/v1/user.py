from fastapi import APIRouter
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.schemas.user import UserResponse, LoginRequest, AuthResponse
from app.models.user import User
from fastapi import HTTPException
from app.utils import hash_password
from app.utils import create_access_token

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(user: UserCreate,db:Session=Depends(get_db), response_model=UserResponse):
    db_user = User(**user.model_dump()) # this is equivaltent to User(User.name = user.name, User.email = user.email, User.password = user.password)
    db_user.password=hash_password(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def authenticate_user( login_request: LoginRequest,db:Session=Depends(get_db), response_model=AuthResponse):
    db_user = db.query(User).filter(User.email==login_request.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not db_user.verify_password(login_request.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": str(db_user.id)})
    return AuthResponse(token=token)

