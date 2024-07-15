from domain.product_repository import ProductRepository
from domain.product import Product
from .database import connect_mysql

class MySQLProductRepository(ProductRepository):
    def add(self, product: Product):
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", 
                       (product.name, product.price, product.quantity))
        conn.commit()
        conn.close()

    def get_all(self):
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [Product(row[1], row[2], row[3], row[0]) for row in rows]

    def update(self, product: Product):
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s", 
                       (product.name, product.price, product.quantity, product.id))
        conn.commit()
        conn.close()

    def delete(self, product_id: int):
        conn = connect_mysql()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        conn.close()
