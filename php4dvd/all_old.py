# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox() #Remote('http://192.168.234.130:4444/wd/hub', webdriver.DesiredCapabilities.FIREFOX )#Firefox()  #Ie() #Remote('http://127.0.0.1:12345/wd/hub', webdriver.DesiredCapabilities.FIREFOX() )
        self.driver.implicitly_wait(30)
        self.base_url = "http://yandex.ru"#"http://localhost:9080"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_first(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #def number = random.randrange(0, 101, 2)

    def test_add(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        rnd_number = random.randrange(0, 10000)
        movie_name = "Movie name" + str(rnd_number)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie_name)
        driver.find_element_by_name("year").clear()
        rnd_year = random.randrange(1900, 2017)
        driver.find_element_by_name("year").send_keys(rnd_year)
        driver.find_element_by_id("submit").click()

        try:
            self.assertEqual(movie_name + " (" + str(rnd_year) + ")", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h2"))
        except AssertionError as e: self.verificationErrors.append(str(e))

        try:
            self.assertEqual("DVD", driver.find_element_by_css_selector("div.duration").text)
        except AssertionError as e: self.verificationErrors.append(str(e))


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_delete(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        movie_name = driver.find_element_by_css_selector(".movie_box .title").text
        driver.find_element_by_css_selector(".movie_box").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random




class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:9080/"
        self.verificationErrors = []
        self.accept_next_alert = True



    def test_try_add(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        rnd_number = random.randrange(0, 10000)
        movie_name = "Movie name" + str(rnd_number)
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(movie_name)
        driver.find_element_by_id("submit").click()

        try: self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='updateform']/table/tbody/tr[4]/td[2]/label"))
        except AssertionError as e: self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import NoAlertPresentException
    import unittest, time, re, random


    class Untitled(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://localhost:9080/"
            self.verificationErrors = []
            self.accept_next_alert = True

        def test_search(self):
            driver = self.driver
            driver.get(self.base_url + "/php4dvd/")
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin")
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys("admin")
            driver.find_element_by_name("submit").click()
            driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()

            rnd_number = random.randrange(0, 10000)
            movie_name = "Movie name" + str(rnd_number)
            driver.find_element_by_name("name").clear()
            driver.find_element_by_name("name").send_keys(movie_name)
            driver.find_element_by_name("year").clear()
            rnd_year = random.randrange(1900, 2017)
            driver.find_element_by_name("year").send_keys(rnd_year)
            driver.find_element_by_id("submit").click()

            try:
                self.assertEqual(movie_name + " (" + str(rnd_year) + ")",
                                 driver.find_element_by_css_selector("h2").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "h2"))
            except AssertionError as e:
                self.verificationErrors.append(str(e))
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.duration"))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

            driver.find_element_by_css_selector("h1").click()
            driver.find_element_by_id("q").clear()
            driver.find_element_by_id("q").send_keys(movie_name)
            try:
                self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.title"))
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        def test_search_no_result(self):
            driver = self.driver
            driver.get(self.base_url + "/php4dvd/")
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin")
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys("admin")
            driver.find_element_by_name("submit").click()
            driver.find_element_by_id("q").clear()
            driver.find_element_by_id("q").send_keys("test123456")
            driver.find_element_by_id("q").send_keys(Keys.ENTER)
            try:
                self.assertEqual("No movies where found.", driver.find_element_by_css_selector("div.content").text)
            except AssertionError as e:
                self.verificationErrors.append(str(e))

        def is_element_present(self, how, what):
            try:
                self.driver.find_element(by=how, value=what)
            except NoSuchElementException as e:
                return False
            return True

        def is_alert_present(self):
            try:
                self.driver.switch_to_alert()
            except NoAlertPresentException as e:
                return False
            return True

        def close_alert_and_get_its_text(self):
            try:
                alert = self.driver.switch_to_alert()
                alert_text = alert.text
                if self.accept_next_alert:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            finally:
                self.accept_next_alert = True

        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)


    if __name__ == "__main__":
        unittest.main()
