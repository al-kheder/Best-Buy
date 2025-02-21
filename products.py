class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.quantity}")

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)  # Using set_quantity to update stock

        return self.price * quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
