from selenium.webdriver.common.by import By
from base.baseclass import Baseclass1
import Utilities.customlogger as cl


"""This class specify all the required locators for the IMDB page,
And respective function which invokes the locators"""
class wiki(Baseclass1):
    def __init__(self, driver):
        self.driver = driver

    _release_data_wiki = "//div[contains(text(),'Release date')]/../../td/div/ul/li"
    _country_origin_wiki = "//th[contains(text(),'Country')]/../td"
    _text_release_date = (By.XPATH, "//div[contains(text(),'Release date')]/../../td/div/ul/li")
    _text_release_country = (By.XPATH, "//th[contains(text(),'Country')]/../td")

    def get_release_date_wiki(self):
        self.scrollto(self._release_data_wiki, "xpath")
        cl.allurelogs("Release date fetched successfully")
        cl.customlogger().info("Release date fetched successfully")

    def text_release_date_wiki(self):
        return self.driver.find_element(*wiki._text_release_date)

    def get_country_region_wiki(self):
        self.scrollto(self._country_origin_wiki, "xpath")
        cl.allurelogs("Region fetched successfully")
        cl.customlogger().info("Region fetched successfully")

    def text_release_country_wiki(self):
        return self.driver.find_element(*wiki._text_release_country)
