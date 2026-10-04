import json
from pathlib import Path

from helpers.types import Product

PATH = Path(__file__).resolve().parent


def load_products() -> list[Product]:
    """
    Returns the list of products from the json file.
    """
    products_file = PATH.joinpath("json/products.json")
    with products_file.open() as file:
        return json.load(file)


def get_product(key: str, value: str) -> Product | None:
    """
    Returns a product by a specified key and value.
    """
    products = load_products()
    return next(
        filter(lambda item: item[key] == value, products),
        None,
    )
