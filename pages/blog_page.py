from playwright.sync_api import Page

from .base_page import BasePage
from .components import BlogEntryComponent


class BlogPage(BasePage):
    URL = "/blogs/news"

    def __init__(self, page: Page) -> None:
        super().__init__(page, self.URL)

        self.blog_entries = self._root.get_by_role("article")

    def get_blog_entry(self, title: str) -> BlogEntryComponent:
        """
        Returns a blog entry by title.
        """
        blog_entry = self.blog_entries.filter(
            has=self._root.locator("h2", has_text=title)
        )
        return BlogEntryComponent(blog_entry)
