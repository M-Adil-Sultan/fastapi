from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.auth_service import authenticate_user, create_user
from models.user import User
from database.connection import get_db

router = APIRouter()

@router.post("/auth/signup", response_model=User)
def create_user_endpoint(user_data: User, db: Session = Depends(get_db)):
    return create_user(db, user_data.username, user_data.password)

@router.post("/auth/login")
def login_user_endpoint(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    # Generate JWT token here
    return {"token": "fake-jwt-token"}
