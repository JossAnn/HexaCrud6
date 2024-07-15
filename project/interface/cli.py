from application.product_service import ProductService

def menu(service: ProductService):
    while True:
        print("\nProduct Management System")
        print("1. Add product")
        print("2. View products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            service.add_product(name, price, quantity)
            print("Product added successfully!")
        
        elif choice == "2":
            products = service.get_products()
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        
        elif choice == "3":
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            price = float(input("Enter new product price: "))
            quantity = int(input("Enter new product quantity: "))
            service.update_product(product_id, name, price, quantity)
            print("Product updated successfully!")
        
        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            service.delete_product(product_id)
            print("Product deleted successfully!")
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice. Please try again.")
