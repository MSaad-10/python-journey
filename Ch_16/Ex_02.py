'''
    - Use the same Laptop class from last exercise.
    - Add a new instance method named apply_discount which:
        * will take an integer argument
        * returns the integer percentage off price of laptop
'''


class Laptop:
    def __init__(self, brand_name: str, model_name: str, laptop_price: int):  
        print('Constructor Initialized')
        self.brand = brand_name
        self.model = model_name
        self.price = laptop_price
        self.name = brand_name + " " + model_name

    def apply_discount(self, off: int) -> int:
        return int(self.price - (self.price*(off/100)))


l1 = Laptop('Lenovo', 'ThinkBook', 63000)
print(l1.price)
print(l1.apply_discount(50))