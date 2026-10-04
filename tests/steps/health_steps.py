from playwright.sync_api import expect
from pytest_bdd import then, when

from pages import PageObjectManager


@when("I open the home page")
def i_open_the_home_page(pom: PageObjectManager):
    pom.home.goto()


@then("the home page is displayed")
def the_home_page_is_displayed(pom: PageObjectManager):
    expect(pom.home.header.logo).to_be_visible()
