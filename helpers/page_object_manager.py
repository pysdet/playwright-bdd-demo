from playwright.sync_api import Page

from pages import (
    AboutUsPage,
    BlogPage,
    CatalogPage,
    HomePage,
    LoginPage,
    MyCartPage,
    ProductPage,
    ResetPasswordPage,
    SearchPage,
    SignUpPage,
)


class PageObjectManager:
    def __init__(self, page: Page) -> None:
        self.about_us = AboutUsPage(page)
        self.blog = BlogPage(page)
        self.catalog = CatalogPage(page)
        self.home = HomePage(page)
        self.login = LoginPage(page)
        self.my_cart = MyCartPage(page)
        self.product = ProductPage(page)
        self.reset_password = ResetPasswordPage(page)
        self.search = SearchPage(page)
        self.sign_up = SignUpPage(page)
