from playwright.sync_api import Locator

from .base_component import BaseComponent
from .product_card_component import ProductCardComponent


class ProductGridComponent(BaseComponent):
    def __init__(self, root: Locator) -> None:
        super().__init__(root)

    def get_product_card(self, name: str) -> ProductCardComponent:
        """
        Returns a product card by name.
        """
        product_card = self._root.filter(has_text=name)
        return ProductCardComponent(product_card)
