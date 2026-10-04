from playwright.sync_api import Locator

from .base_component import BaseComponent


class HeaderComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)
        # Search
        self.searchbox = self._root.get_by_placeholder("Search")
        # Links
        self.search_link = self._root.get_by_role("link", name="Search")
        self.about_us_link = self._root.get_by_role("link", name="About Us")
        self.login_link = self._root.get_by_role("link", name="Log In")
        self.sign_up_link = self._root.get_by_role("link", name="Sign up")
        # Cart
        self.my_cart_link = self._root.get_by_role("link", name="My Cart")
        self.checkout_link = self._root.get_by_role("link", name="Check Out")
        # Info
        self.logo = self._root.locator("#logo")
        self.description = self._root.locator("#tagline")
