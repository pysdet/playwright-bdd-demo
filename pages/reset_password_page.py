from playwright.sync_api import Page

from .base_page import BasePage


class ResetPasswordPage(BasePage):
    URL = "/account/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.reset_password_header = self._root.get_by_role(
            "heading", name="Reset Password"
        )

        self.email_label = self._root.locator("label", has_text="Email")
        self.email_field = self._root.locator("#recover-email")

        self.description = self._root.locator("p")

        self.submit_button = self._root.get_by_role("button", name="Submit")
        self.cancel_button = self._root.get_by_role("link", name="Cancel")
