from pages.internal_page import InternalPage
from pages.blocks.movie_form import MovieForm
from selenium.webdriver.support.ui import Select


class AddMoviePage(InternalPage):

    def __init__(self, driver, base_url):
        super(AddMoviePage, self).__init__(driver,base_url)
        self.movie_form = MovieForm(self.driver, self.base_url)


