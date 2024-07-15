class Product:
    def __init__(self, name, price, quantity, product_id=None):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
