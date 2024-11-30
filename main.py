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
    # Adicionando o produto à lista (simulando inserção no banco de dados)
    #products.append(product)
    print("New Product:", product)
    # Retornando o status de sucesso
    return {"status": "Product inserted successfully", "product": product}
