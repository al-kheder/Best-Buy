import products
from store import Store

from products import Product

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))

def start(store):
    while True:
        print("""
        1. List all products in store 
        2. Show total amount in store
        3. Make an order
        4.Quit
        """)
        actions = {
            1: store.get_all_products,
            2: store.get_total_quantity,
            3: store.order,
            4: Quit
        }
        choice = int(input("Enter your choice: "))
        if choice == 4:
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice")


