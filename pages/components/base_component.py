from playwright.sync_api import Locator


class BaseComponent:
    def __init__(self, root: Locator) -> None:
        self._root = root

    def is_visible(self) -> bool:
        """
        Returns whether the root locator is visible.
        """
        return self._root.is_visible()
