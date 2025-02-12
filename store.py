# composition is a "has a" relationship between two classes
from typing import List

class Store:
    def __init__(self, products: List['Product'] = None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product: 'Product'):
        self.products.append(product)

    def remove_product(self, product: 'Product'):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = sum(product.quantity for product in self.products)
        return total_quantity

    def get_all_products(self) -> List['Product']:
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list: List[tuple['Product', int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products:
                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Product {product.name} is not available in the store.")
        return total_price