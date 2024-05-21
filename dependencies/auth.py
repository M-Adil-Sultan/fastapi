from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database.connection import get_db
from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Validate token and retrieve user
    user = db.query(User).filter(User.username == "test_user").first()  # Simplified for example
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user.id
