# main.py
from fastapi import FastAPI

app = FastAPI()

products = [
    {
        id: 1,
        name: "Laptop",
        price: 999.99
    },
    {
        id: 2,
        name: "Smartphone",
        price: 499.99
    }
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: dict):
    return products.append(item)

if __name__ == "__main__":
    main()
