from fastapi import FastAPI
from app.api.controllers.auth import product_controller, cart_controller, order_controller, auth_controller
from database.connection import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_controller.router)
app.include_router(cart_controller.router)
app.include_router(order_controller.router)
app.include_router(auth_controller.router)
