from playwright.sync_api import Page

from .base_page import BasePage


class MyCartPage(BasePage):
    URL = "/cart"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.my_cart_header = self._root.get_by_role("heading", name="My Cart")

        self.continue_shopping_link = self._root.get_by_role(
            "link", name="Continue Shopping"
        )
        self.total_amount = self._root.locator(".total")

        self.add_note_field = self._root.locator("textarea")

        self.update_button = self._root.get_by_role("button", name="Update")
        self.checkout_button = self._root.get_by_role("button", name="Check Out")
