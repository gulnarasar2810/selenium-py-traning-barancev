from php4dvd.pages.internal_page import InternalPage
from pages.blocks.user_form import UserForm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class ViewMoviePage(InternalPage):
    @property
    def movietitle_field(self):
        return self.driver.find_element_by_css_selector(".maininfo_full > h2:nth-child(1)")

    @property
    def movieformat_field(self):
        return self.driver.find_element_by_css_selector("div.duration")

    @property
    def movie_delete_link(self):
        return self.driver.find_element_by_css_selector("img[alt='Remove']") #("nav a[href $= '?go=delete&id=65']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "img[alt='Remove']"))