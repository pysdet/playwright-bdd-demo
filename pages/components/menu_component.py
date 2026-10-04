from playwright.sync_api import Locator

from .base_component import BaseComponent


class MenuComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)
        # Options
        self._options = self._root.locator("#main-menu")
        # Socials
        self.facebook = self._root.locator(".facebook")
        self.twitter = self._root.locator(".twitter")
        self.instagram = self._root.locator(".instagram")
        self.pinterest = self._root.locator(".pinterest")

    def select_option(self, option: str) -> None:
        """
        Selects an option from the menu.
        """
        menu_option = self._options.filter(has_text=option)
        menu_option.click()
