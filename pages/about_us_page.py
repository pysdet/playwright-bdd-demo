from playwright.sync_api import Page

from .base_page import BasePage


class AboutUsPage(BasePage):
    URL = "/pages/about-us"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.about_us_header = self._root.get_by_role("heading", name="About Us")
        self.about_us_description = self._root.locator("p")
