from store import Store
from products import Product


def display_menu():
    print("""
    Store Menu
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """)


def main():
    # Create some products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    # Create a store and add products

    best_buy = Store([bose, mac, pixel])

    while True:
        display_menu()
        try:
            choice = int(input("Please choose a number: "))
            if choice == 1:
                # List all products in store
                print("------")
                for i, product in enumerate(best_buy.get_all_products(), start=1):
                    print(f"{i}. {product}")
                print("------")
            elif choice == 2:
                # Show total amount in store
                total_quantity = best_buy.get_total_quantity()
                print(f"Total amount in store: {total_quantity} items")
            elif choice == 3:
                # Make an order
                print("Available products:")
                for i, product in enumerate(best_buy.get_all_products(), start=1):
                    print(f"{i}. {product}")
                shopping_list = []
                while True:
                    try:
                        product_index = int(input("Enter the product number (or 0 to finish): "))
                        if product_index == 0:
                            break
                        product = best_buy.get_all_products()[product_index - 1]
                        quantity = int(input(f"Enter quantity for {product.name}: "))
                        shopping_list.append((product, quantity))
                    except (ValueError, IndexError):
                        print("Invalid input. Please try again.")
                if shopping_list:
                    total_cost = best_buy.order(shopping_list)
                    print(f"Order placed successfully! Total cost: ${total_cost}")
            elif choice == 4:
                # Quit
                print("Thank you for using the Store Menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()