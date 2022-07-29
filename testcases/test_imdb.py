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
        release_date = self.imdb.text_release_date().text
        # print(f"Release date is:{release_date}")
        release_date_split = release_date.split(" (United States)")
        print(release_date_split[0])
        return release_date_split[0]

    def releasecountry_IMDB(self):
        self.driver.get(self.urls[0])
        self.imdb.get_country_region()
        release_country = self.driver.find_element(By.XPATH, "//span[contains(text(),'Country of origin')]/../div/ul/li").text
        print(f"Release country:{release_country}")
        return release_country

    def releasedate_wiki(self):
        self.driver.get(self.urls[1])
        self.imdb.get_release_date()
        release_date_wiki = self.driver.find_element(By.XPATH, "//div[contains(text(),'Release date')]/../../td/div/ul/li").text
        print(f"Release date is:{release_date_wiki}")
        return release_date_wiki

    def releasecountry_wiki(self):
        self.driver.get(self.urls[1])
        self.imdb.get_country_region()
        release_country_wiki = self.driver.find_element(By.XPATH, "//th[contains(text(),'Country')]/../td").text
        print(f"Release country:{release_country_wiki}")
        return release_country_wiki

    def test_relase_date_both(self):
        release_date_imdb = self.releasedate_IMDB()
        release_date_wiki = self.releasedate_wiki()
        assert release_date_imdb == release_date_wiki

    def test_relase_country_both(self):
        release_country_imdb = self.releasecountry_IMDB()
        print(type(release_country_imdb))
        release_country_wiki = self.releasecountry_wiki()
        print(type(release_country_wiki))
        assert release_country_imdb==release_country_wiki

