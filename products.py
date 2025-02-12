class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, quantity: int) -> float:
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.quantity}")
        self.quantity -= quantity
        return self.price * quantity

    def is_active(self) -> bool:
        return self.quantity > 0

    def __str__(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
