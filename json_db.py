from pydantic import BaseModel
import json
from product import Product


class JsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data


    def insert(self, product: Product):
        data = self.read()
        data['products'].append(product.dict())
        f = open(self.path, 'w')
        f.write(json.dumps(data))
        f.close()


    def delete_by_id(self, product_id: int):
        data = self.read()

        # Filtra os produtos que não possuem o id correspondente
        data['products'] = [product for product in data['products'] if product['id'] != product_id]

        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def update_by_id(self, product_id: int, updated_product: Product):
        data = self.read()

        # Encontra o produto e substitui-o
        for i, product in enumerate(data['products']):
            if product['id'] == product_id:
                data['products'][i] = updated_product.dict()
                break

        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
