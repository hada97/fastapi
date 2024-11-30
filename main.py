from fastapi import FastAPI
from product import Product
from json_db import JsonDB

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get("/products")
def get_products():
    products = productDB.read()
    return {"products": products}

@app.post("/products")
def created_products(product: Product):
    productDB.insert(product)
    print("New Product:", product)
    return {"products": product}
