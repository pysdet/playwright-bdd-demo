from playwright.sync_api import Page

from .base_page import BasePage
from .components import ProductGridComponent


class CatalogPage(BasePage):
    URL = "/collections/all"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.products_header = self._root.get_by_role("heading", name="Products")
        self.product_grid = ProductGridComponent(
            self._root.locator(".product-grid div")
        )
