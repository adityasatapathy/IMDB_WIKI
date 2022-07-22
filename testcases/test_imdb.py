import unittest
import pytest
from PageObject.imdb_page import Imdb
from base.baseclass import Baseclass1
from selenium.webdriver.common.by import By


class Test_demo(Baseclass1, unittest.TestCase):
    urls = ['https://www.imdb.com/title/tt9389998/?ref_=nv_sr_srsg_0',
            'https://en.wikipedia.org/wiki/Pushpa:_The_Rise']

    @pytest.fixture(autouse=True)
    def object(self):
        self.base = Baseclass1()
        self.imdb = Imdb(self.driver)

    def test_releasedate_IMDB(self):
        self.driver.get(self.urls[0])
        self.imdb.get_release_date()
        release_date = self.driver.find_element(By.XPATH, "//a[contains(text(),'Release date')]/../div/ul/li").text
        print(f"Release date is:{release_date}")

    def test_releasecountry_IMDB(self):
        self.driver.get(self.urls[0])
        self.imdb.get_country_region()
        release_country = self.driver.find_element(By.XPATH, "//span[contains(text(),'Country of origin')]/../div/ul/li").text
        print(f"Release country:{release_country}")