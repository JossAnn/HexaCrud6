from domain.product_repository import ProductRepository
from domain.product import Product
from .database import connect_local
import os
import json

class LocalProductRepository(ProductRepository):
    def __init__(self):
        self.directory = connect_local()

    def add(self, product: Product):
        product_dict = product.__dict__
        with open(os.path.join(self.directory, f'{product.id}.json'), 'w') as f:
            json.dump(product_dict, f)

    def get_all(self):
        products = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as f:
                    product_dict = json.load(f)
                    products.append(Product(**product_dict))
        return products

    def update(self, product: Product):
        self.add(product)

    def delete(self, product_id: int):
        os.remove(os.path.join(self.directory, f'{product_id}.json'))
