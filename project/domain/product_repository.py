from abc import ABC, abstractmethod
from .product import Product

class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, product: Product):
        pass

    @abstractmethod
    def delete(self, product_id: int):
        pass
