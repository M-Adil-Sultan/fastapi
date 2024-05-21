from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.product import Product
from services.product_service import create_product, get_products, update_product, delete_product
from database.connection import get_db

router = APIRouter()

@router.post("/products", response_model=Product)
def create_product_endpoint(product_data: Product, db: Session = Depends(get_db)):
    return create_product(db, product_data.dict())

@router.get("/products", response_model=List[Product])
def get_products_endpoint(category: str = None, db: Session = Depends(get_db)):
    return get_products(db, category)

@router.put("/products/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, product_data: Product, db: Session = Depends(get_db)):
    return update_product(db, product_id, product_data.dict())

@router.delete("/products/{product_id}", response_model=Product)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)
