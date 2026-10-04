from playwright.sync_api import Locator

from .base_component import BaseComponent


class BlogEntryComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)

        self.date = self._root.locator(".date")
        self.title = self._root.locator("h2")
        self.author = self._root.get_by_text("Posted by")
        self.description = self._root.locator(".content div").last
