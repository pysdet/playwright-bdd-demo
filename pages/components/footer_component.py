from playwright.sync_api import Locator

from .base_component import BaseComponent


class FooterComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)

        self.footer_header = self._root.get_by_role("heading", name="Footer")
        self.search_link = self._root.get_by_role("link", name="Search")
        self.about_us_link = self._root.get_by_role("link", name="About Us")

        self.about_us_header = self._root.get_by_role("heading", name="About Us")
        self.about_us_description = self._root.locator("#footer-content p")

        self.american_express = self._root.get_by_alt_text("We accept Amex")
        self.visa = self._root.get_by_alt_text("We accept Visa")
        self.mastercard = self._root.get_by_alt_text("We accept Mastercard")

        self.copyright = self._root.locator(".legals")
