from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.order import Order
from services.order_service import place_order, get_order_details
from database.connection import get_db
from dependencies.auth import get_current_user

router = APIRouter()

@router.post("/orders")
def place_order_endpoint(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return place_order(db, user_id)

@router.get("/orders/{order_id}", response_model=Order)
def get_order_details_endpoint(order_id: int, db: Session = Depends(get_db)):
    return get_order_details(db, order_id)
