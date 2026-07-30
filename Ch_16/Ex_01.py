'''
    - Create a Laptop class with following attributes:
        * brand name
        * model name
        * price
        * laptop name
    - Create two objects of Laptop class
'''


class Laptop:
    def __init__(self, brand_name: str, model_name: str, laptop_price: int):    # Constructor
        print('Constructor Initialized')
        self.brand = brand_name
        self.model = model_name
        self.price = laptop_price
        self.name = f"{self.brand} {self.model}"

l1 = Laptop('Lenovo', 'ThinkBook', 150000)
print(l1.brand)
print(l1.model)
print(l1.name)
print(l1.price)
print()

l2 = Laptop('HP', 'Elitebook', 65000)
print(l2.brand)
print(l2.model)
print(l2.name)
print(l2.price)