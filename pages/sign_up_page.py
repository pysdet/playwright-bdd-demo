from playwright.sync_api import Page

from .base_page import BasePage


class SignUpPage(BasePage):
    URL = "/account/register"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.create_account_header = self._root.get_by_role(
            "heading", name="Create Account"
        )

        self.first_name_label = self._root.locator("label", has_text="First Name")
        self.first_name_field = self._root.locator("#first_name")

        self.last_name_label = self._root.locator("label", has_text="Last Name")
        self.last_name_field = self._root.locator("#last_name")

        self.email_label = self._root.locator("label", has_text="Email Address")
        self.email_field = self._root.locator("#email")

        self.password_label = self._root.locator("label", has_text="Password")
        self.password_field = self._root.locator("#password")

        self.create_button = self._root.get_by_role("button", name="Create")
