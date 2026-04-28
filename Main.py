# main.py

from Product import Product
from Inventory import Inventory
from Utils import apply_global_discount, format_currency

inventory = Inventory()

# добавляем товары
inventory.add_product(Product("Laptop", 4000, 2))
inventory.add_product(Product("Mouse", 50, 10))
inventory.add_product(Product("Keyboard", 120, 5))

print("=== PRODUCTS ===")
inventory.show_all()

print("\n=== TOTAL VALUE ===")
print(format_currency(inventory.total_inventory_value()))

# применяем скидку 10%
apply_global_discount(inventory.products, 10)

print("\n=== AFTER DISCOUNT ===")
inventory.show_all()

print("\n=== NEW TOTAL VALUE ===")
print(format_currency(inventory.total_inventory_value()))