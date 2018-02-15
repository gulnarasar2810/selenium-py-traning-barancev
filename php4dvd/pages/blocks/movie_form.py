from php4dvd.pages.page import Page
from selenium.webdriver.common.by import By


class MovieForm(Page):
    @property
    def movietitle_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def movieyear_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def movieformat_field(self):
        return self.driver.find_element_by_id("formats")

    @property
    def submit_button(self):
        return self.driver.find_element_by_name("submit")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "img[alt='Save']"))





