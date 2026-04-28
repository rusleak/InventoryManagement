# inventory.py

from Product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def total_inventory_value(self):
        return sum(p.total_value() for p in self.products)

    def show_all(self):
        for p in self.products:
            print(p)

    def find_product(self, name: str):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None