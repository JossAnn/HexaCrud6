from domain.product_repository import ProductRepository
from domain.product import Product
from .database import connect_mongodb

class MongoDBProductRepository(ProductRepository):
    def __init__(self):
        self.db = connect_mongodb()
        self.collection = self.db['products']

    def add(self, product: Product):
        product_dict = product.__dict__
        self.collection.insert_one(product_dict)

    def get_all(self):
        products = self.collection.find()
        return [Product(p['name'], p['price'], p['quantity'], p['_id']) for p in products]

    def update(self, product: Product):
        self.collection.update_one({'_id': product.id}, 
                                   {'$set': {'name': product.name, 'price': product.price, 'quantity': product.quantity}})

    def delete(self, product_id: int):
        self.collection.delete_one({'_id': product_id})
