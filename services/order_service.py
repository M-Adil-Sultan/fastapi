from sqlalchemy.orm import Session
from models.order import Order, OrderItem
from models.cart import Cart

def place_order(db: Session, user_id: int):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    total_cost = sum(item.quantity * item.product.price for item in cart_items)
    
    order = Order(user_id=user_id, total_cost=total_cost)
    db.add(order)
    db.commit()
    db.refresh(order)
    
    for item in cart_items:
        order_item = OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, price=item.product.price)
        db.add(order_item)
        
    db.query(Cart).filter(Cart.user_id == user_id).delete()
    db.commit()
    
    return order

def get_order_details(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()
