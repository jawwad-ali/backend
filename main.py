# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Define a proper model
class Item(BaseModel):
    id: int
    name: str
    price: float

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: Item):  # Now uses Pydantic model
    product_dict = item.model_dump()  # Convert to dict
    products.append(product_dict)
   

    return {"message": "Item added", "items": products}