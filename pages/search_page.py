from playwright.sync_api import Page

from .base_page import BasePage
from .components import ProductGridComponent


class SearchPage(BasePage):
    URL = "/search"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.search_header = self._root.get_by_role("heading", name="Search Results")
        self.showing_results_for = self._root.get_by_text("Showing results for")

        self.product_grid = ProductGridComponent(
            self._root.locator(".product-grid div")
        )
