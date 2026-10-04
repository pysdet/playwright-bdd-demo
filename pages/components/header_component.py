from playwright.sync_api import Locator

from .base_component import BaseComponent


class HeaderComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)

        self.searchbox = self._root.get_by_placeholder("Search")

        self.search_link = self._root.get_by_role("link", name="Search")
        self.about_us_link = self._root.get_by_role("link", name="About Us")
        self.login_link = self._root.get_by_role("link", name="Log In")
        self.sign_up_link = self._root.get_by_role("link", name="Sign up")

        self.my_cart_link = self._root.get_by_role("link", name="My Cart")
        self.checkout_link = self._root.get_by_role("link", name="Check Out")

        self.logo = self._root.locator("#logo")
        self.tagline = self._root.locator("#tagline")
