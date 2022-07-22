from base.baseclass import Baseclass1
import Utilities.customlogger as cl


"""This class specify all the required locators for the IMDB page,
And respective function which invokes the locators"""
class wiki(Baseclass1):
    def __init__(self, driver):
        self.driver = driver

    _release_data_wiki = "//div[contains(text(),'Release date')]/../../td/div/ul/li"
    _country_origin_wiki = "//th[contains(text(),'Country')]/../td"

    def get_release_date_wiki(self):
        self.scrollto(self._release_data, "xpath")
        cl.allurelogs("Release date fetched successfully")
        cl.customlogger().info("Release date fetched successfully")

    def get_country_region_wiki(self):
        self.scrollto(self._country_origin, "xpath")
        cl.allurelogs("Region fetched successfully")
        cl.customlogger().info("Region fetched successfully")