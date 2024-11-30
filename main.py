from fastapi import FastAPI
from product import Product
from json_db import JsonDB

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get("/products")
def get_products():
    products = productDB.read()
    if not products.get('products'):
        return {"message": "Nenhum produto encontrado."}
    return {"message": "Produtos recuperados com sucesso.", "products": products['products']}


@app.post("/products")
def created_products(product: Product):
    productDB.insert(product)
    return {"message": "Produto criado com sucesso!", "product": product}



@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        productDB.delete_by_id(product_id)
        return {"message": f"Produto com ID {product_id} foi deletado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    try:
        productDB.update_by_id(product_id, updated_product)
        return {"message": f"Produto com ID {product_id} foi atualizado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

