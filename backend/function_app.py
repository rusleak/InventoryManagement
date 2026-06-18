import azure.functions as func
import json

from Inventory import Inventory
from Product import Product
from Utils import apply_global_discount

app = func.FunctionApp()

inventory = Inventory()

inventory.add_product(Product("Laptop",4000,2))
inventory.add_product(Product("Mouse",50,10))
inventory.add_product(Product("Keyboard",120,5))


@app.route(route="products",
auth_level=func.AuthLevel.ANONYMOUS)
def get_products(req: func.HttpRequest):

    products=[]

    for p in inventory.products:

        products.append({
            "name":p.name,
            "price":p.price,
            "quantity":p.quantity
        })

    return func.HttpResponse(
        json.dumps(products),
        mimetype="application/json"
    )


@app.route(route="total",
auth_level=func.AuthLevel.ANONYMOUS)
def total(req: func.HttpRequest):

    return func.HttpResponse(
        json.dumps({
            "total":inventory.total_inventory_value()
        }),
        mimetype="application/json"
    )


@app.route(
route="discount",
methods=["POST"],
auth_level=func.AuthLevel.ANONYMOUS
)
def discount(req:func.HttpRequest):

    body=req.get_json()

    percent=body["percent"]

    apply_global_discount(
        inventory.products,
        percent
    )

    return func.HttpResponse(
        json.dumps({
            "message":"Discount applied"
        }),
        mimetype="application/json"
    )