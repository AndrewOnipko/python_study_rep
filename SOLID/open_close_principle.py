# Соответствует OCP
 
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    
    def apply_discount(self, price: float) -> float:
        return price
    
class SomeDiscount(DiscountStrategy):

    def __init__(self, discount:float):
        self.discount = discount

    def apply_discount(self, price):
        return price / self.discount
    

class CalculateDiscount:
    def __init__(self, product_name: str, price: float, discount_strategy: DiscountStrategy):
        self.product_name = product_name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price(self) -> float:

        return self.discount_strategy.apply_discount(self.price)
    

discount_calculator = CalculateDiscount("Shopper", 100.0, NoDiscount())
print(f"{discount_calculator.product_name}: {discount_calculator.get_price()}")

# Не соответствует OCP

class CalculateDiscount:
    def __init__(self, product_name: str, price: float, discount_strategy: str):
        self.product_name = product_name
        self.price = price
        self.discount_strategy = discount_strategy

    def get_price(self) -> float:

        if self.discount_strategy == "NoDiscount":
            pass
        elif self.discount_strategy == "SomeDiscount":
            pass
        else:
            ...