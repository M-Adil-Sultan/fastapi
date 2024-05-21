from sqlalchemy.orm import Session
from models.cart import Cart

def create_cart(db: Session, user_id: int):
    cart = Cart(user_id=user_id)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

def add_product_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
    cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def remove_product_from_cart(db: Session, cart_item_id: int):
    cart_item = db.query(Cart).filter(Cart.id == cart_item_id).first()
    db.delete(cart_item)
    db.commit()
    return cart_item

def get_cart_contents(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).all()
