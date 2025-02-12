class Product:
    def __init__(self, name:str, price:float,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    #getter method
    def get_quantity(self)->int:
        return self.quantity

    #setter method
    def set_quantity(self, quantity:int):
        self.quantity = quantity

    def is_active(self)->bool:
        return self.active

    def activate(self):
        self.active = True

    def deactive(self)->bool:
        self.active = False

    def show(self) ->str:
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}")

    def buy(self, quantity:int) -> float:
        if self.quantity >= quantity:
            self.quantity -= quantity
            return self.price * quantity
        else:
            print("Not enough quantity")

