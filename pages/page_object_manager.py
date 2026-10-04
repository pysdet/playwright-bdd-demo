from playwright.sync_api import Page

from .about_us_page import AboutUsPage
from .blog_page import BlogPage
from .catalog_page import CatalogPage
from .home_page import HomePage
from .login_page import LoginPage
from .my_cart_page import MyCartPage
from .product_page import ProductPage
from .reset_password_page import ResetPasswordPage
from .search_page import SearchPage
from .sign_up_page import SignUpPage


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
