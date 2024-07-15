from domain.product_repository import ProductRepository
from domain.product import Product
from .database import connect_s3
import json

class S3ProductRepository(ProductRepository):
    def __init__(self):
        self.s3 = connect_s3()
        self.bucket_name = 'your-bucket-name'

    def add(self, product: Product):
        product_dict = product.__dict__
        self.s3.put_object(Bucket=self.bucket_name, Key=f'products/{product.id}.json', Body=json.dumps(product_dict))

    def get_all(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix='products/')
        products = []
        for obj in response.get('Contents', []):
            product_data = self.s3.get_object(Bucket=self.bucket_name, Key=obj['Key'])
            product_dict = json.loads(product_data['Body'].read().decode('utf-8'))
            products.append(Product(**product_dict))
        return products

    def update(self, product: Product):
        self.add(product)

    def delete(self, product_id: int):
        self.s3.delete_object(Bucket=self.bucket_name, Key=f'products/{product_id}.json')
