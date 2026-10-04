from playwright.sync_api import Page

from .components import FooterComponent, HeaderComponent, MenuComponent


class BasePage:
    def __init__(self, page: Page, url: str) -> None:
        self._page = page
        self._url = url
        # Components
        self.header = HeaderComponent(page.locator("header"))
        self.menu = MenuComponent(page.locator("#sidebar"))
        self.footer = FooterComponent(page.locator("footer"))

    def goto(self, params: dict[str, str | int | bool] | None = None) -> str:
        """
        Goes to the page url using the params if any and waits for the content to load.
        Returns the generated url.
        """
        url = self._url
        if params:
            url_params = [
                f"{'&' if index else '?'}{key}={value}"
                for index, (key, value) in enumerate(params.items())
            ]
            url += "".join(url_params)
        self._page.goto(url, wait_until="domcontentloaded")
        return url

    def get_current_url(self) -> str:
        """
        Returns the url in the current page.
        """
        return self._page.url
