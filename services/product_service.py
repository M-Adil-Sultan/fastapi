from sqlalchemy.orm import Session
from models.product import Product

def create_product(db: Session, product_data):
    product = Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session, category: str = None):
    if category:
        return db.query(Product).filter(Product.category == category).all()
    return db.query(Product).all()

def update_product(db: Session, product_id: int, product_data):
    product = db.query(Product).filter(Product.id == product_id).first()
    for key, value in product_data.items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return product
