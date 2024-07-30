from application.product_service import ProductService

def menu(service: ProductService):
    while True:
        print("\nAdministrador de productos")
        print("1. Añadir un producto")
        print("2. Ver Productos")
        print("3. Actualizar un producto")
        print("4. Eliminar un producto")
        print("5. Salir")

        choice = input("Elige tu opcion: ")

        if choice == "1":
            name = input("Ingresa el nombre del producto: ")
            price = float(input("Ingresa el precio del producto: "))
            quantity = int(input("Ingresa la cantidad de productos que se agregan: "))
            service.add_product(name, price, quantity)
            print("Producto Añadido!")
        
        elif choice == "2":
            products = service.get_products()
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        
        elif choice == "3":
            product_id = int(input("Ingresa el ID del producto: "))
            name = input("Ingresa el nuevo nombre del producto: ")
            price = float(input("Ingresa el nuevo precio del producto: "))
            quantity = int(input("Ingresa la nueva cantidad del producto: "))
            service.update_product(product_id, name, price, quantity)
            print("Producto Actualizado!")
        
        elif choice == "4":
            product_id = int(input("Ingresa el ID del producto a eliminar: "))
            service.delete_product(product_id)
            print("Producto Eliminado!")
        
        elif choice == "5":
            break
        
        else:
            print("Seleccion no valida, intentalo de nuevo.")
