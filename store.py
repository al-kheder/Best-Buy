from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product] = None):
        """Initializes the store with a list of products."""
        if products is not None:
            if not isinstance(products, list):
                raise TypeError("Products must be a list.")
            if not all(isinstance(product, Product) for product in products):
                raise TypeError("All items in the products list must be instances of Product.")
        self.products = products if products is not None else []

    def add_product(self, product: Product):
        """Adds a product to the store, ensuring it's a valid Product instance."""
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product.")
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store if it exists, otherwise raises a ValueError."""
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of Product.")
        if product not in self.products:
            raise ValueError(f"Product '{product.name}' not found in the store.")
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.quantity for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple[Product, int]]) -> float:
        """Processes an order and returns the total cost."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Each item in shopping list must be a tuple (Product, int).")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer.")

            if product in self.products:
                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Product {product.name} is not available in the store.")
        return total_price
