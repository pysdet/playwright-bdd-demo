from playwright.sync_api import Locator

from .base_component import BaseComponent


class ProductCardComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)
        self.link = self._root.get_by_role("link")
        self.image = self._root.get_by_role("img")
        self.name = self._root.locator("h3")
        self.price = self._root.locator("h4")
