
from flask import Blueprint, render_template
from models.product import Product


product_bp = Blueprint(
    "product",
    __name__,
    url_prefix="/products"
)


@product_bp.route("/")
def list_products():
    return render_template(
        "product/list.html",
        products=Product.get_all()
    )
