from playwright.sync_api import Page

from .base_page import BasePage
from .components import ProductGridComponent


class ProductPage(BasePage):
    URL = "/collections/frontpage/products"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.image = self._root.get_by_role("img")
        self.name = self._root.locator("h1")
        self.price = self._root.locator(".product-price")

        self.add_to_cart_button = self._root.get_by_role("button", name="Add to cart")

        self.description = self._root.locator("#product-info")

        self.related_products_header = self._root.get_by_role(
            "heading", name="You Might Also Like..."
        )
        self.related_product_grid = ProductGridComponent(
            self._root.locator("#related-products div")
        )
