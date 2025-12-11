# main.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# ---- Sample data (fixed syntax) ----
products = [
    {"id": 1, "name": "Laptop",    "price": 999.99},
    {"id": 2, "name": "Smartphone","price": 499.99},
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# ---- POST endpoint (returns the new list) ----
@app.post("/items/")
def create_item(item: dict):
    products.append(item)
    return {"items": products}

# ---- Railway needs a proper entry point ----
if __name__ == "__main__":
    # Railway injects the $PORT variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)