from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title_span = "//span[@data-test='title']"

    def is_product_title_visible(self):
        return self.is_element_visible(self.title_span)

    def get_product_title_text(self):
        return self.get_element_text(self.title_span)
