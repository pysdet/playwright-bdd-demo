from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):
    URL = "/account/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.login_header = self._root.get_by_role("heading", name="Customer Login")

        self.email_label = self._root.locator("label", has_text="Email Address")
        self.email_field = self._root.locator("#customer_email")

        self.password_label = self._root.locator("label", has_text="Password")
        self.password_field = self._root.locator("#customer_password")

        self.forgot_password_link = self._root.get_by_role(
            "link", name="Forgot your password?"
        )

        self.sign_in_button = self._root.get_by_role("button", name="Sign In")
