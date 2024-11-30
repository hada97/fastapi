from fastapi import FastAPI
from indb import generate_products
from product import Product

app = FastAPI()

products = generate_products()

@app.get("/products")
def get_products():
    return {"products": products}


@app.post("/products")
def created_products(product: Product):

    print("New Product", product)

    return {"status" : inserted}

