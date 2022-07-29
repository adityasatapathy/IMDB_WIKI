from base.baseclass import Baseclass1
import Utilities.customlogger as cl
from selenium.webdriver.common.by import By


"""This class specify all the required locators for the IMDB page,
And respective function which invokes the locators"""
class Imdb(Baseclass1):
    def __init__(self, driver):
        self.driver = driver

    _release_data = "//a[contains(text(),'Release date')]/../div/ul/li"
    _country_origin = "//span[contains(text(),'Country of origin')]/../div/ul/li"
    _text_release_date = (By.XPATH, "//a[contains(text(),'Release date')]/../div/ul/li")
    _text_release_country = (By.XPATH, "//span[contains(text(),'Country of origin')]/../div/ul/li")

    def get_release_date(self):
        self.scrollto(self._release_data, "xpath")
        cl.allurelogs("Release date fetched successfully")
        cl.customlogger().info("Release date fetched successfully")

    def text_release_date(self):
        return self.driver.find_element(*Imdb._text_release_date)

    def get_country_region(self):
        self.scrollto(self._country_origin, "xpath")
        cl.allurelogs("Region fetched successfully")
        cl.customlogger().info("Region fetched successfully")

    def text_release_country(self):
        return self.driver.find_element(*Imdb._text_release_country)
