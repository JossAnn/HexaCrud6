from domain.product import Product
from domain.product_repository import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.repository.add(product)

    def get_products(self):
        return self.repository.get_all()

    def update_product(self, product_id, name, price, quantity):
        product = Product(name, price, quantity, product_id)
        self.repository.update(product)

    def delete_product(self, product_id):
        self.repository.delete(product_id)
