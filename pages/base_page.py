from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def is_element_visible(self, selector: str):
        return self.page.is_visible(selector)

    def get_element_text(self, selector: str):
        return self.page.inner_text(selector)
