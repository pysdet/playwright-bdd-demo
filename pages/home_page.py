from playwright.sync_api import Page

from .base_page import BasePage
from .components import ProductCardComponent


class HomePage(BasePage):
    URL = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)
        # Cards
        self._product_cards = page.locator(".product-grid div")

    def get_product_card(self, id: int) -> ProductCardComponent:
        """
        Returns a product card by id.
        """
        product_card = self._product_cards.filter(
            has=self._page.locator(f"#product-{id}")
        )
        return ProductCardComponent(product_card)
