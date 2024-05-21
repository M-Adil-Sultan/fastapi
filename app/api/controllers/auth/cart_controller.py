from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.cart import Cart
from services.cart_service import create_cart, add_product_to_cart, remove_product_from_cart, get_cart_contents
from database.connection import get_db
from dependencies.auth import get_current_user

router = APIRouter()

@router.post("/cart")
def create_cart_endpoint(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_cart(db, user_id)

@router.post("/cart/items")
def add_product_to_cart_endpoint(product_id: int, quantity: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return add_product_to_cart(db, user_id, product_id, quantity)

@router.delete("/cart/items/{cart_item_id}")
def remove_product_from_cart_endpoint(cart_item_id: int, db: Session = Depends(get_db)):
    return remove_product_from_cart(db, cart_item_id)

@router.get("/cart")
def get_cart_contents_endpoint(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_cart_contents(db, user_id)
