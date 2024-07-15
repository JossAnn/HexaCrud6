from infrastructure.sqlite_product_repository import SQLiteProductRepository
from infrastructure.mysql_product_repository import MySQLProductRepository
from infrastructure.mongodb_product_repository import MongoDBProductRepository
from infrastructure.s3_product_repository import S3ProductRepository
from infrastructure.local_product_repository import LocalProductRepository
from application.product_service import ProductService
from interface.cli import menu

def main():
    print("Select Repository:")
    print("1. SQLite")
    print("2. MySQL")
    print("3. MongoDB")
    print("4. S3")
    print("5. Local Storage")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        repository = SQLiteProductRepository()
    elif choice == "2":
        repository = MySQLProductRepository()
    elif choice == "3":
        repository = MongoDBProductRepository()
    elif choice == "4":
        repository = S3ProductRepository()
    elif choice == "5":
        repository = LocalProductRepository()
    else:
        print("Invalid choice. Exiting.")
        return
    
    service = ProductService(repository)
    menu(service)

if __name__ == "__main__":
    main()
