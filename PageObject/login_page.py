import allure

from base.baseclass import Baseclass1
import Utilities.customlogger as cl
from selenium.webdriver.common.by import By

from constants.login_constants import LoginConstants

"""This class specifies to login amazon.in and performing actions
"""


class LogIn(Baseclass1, LoginConstants):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Login to amazon page")
    def login_home(self):
        try:
            self.lunch_webpage(self.home_url, self.home_title)
            cl.allurelogs("Amazon website lunched successfully")
            cl.customlogger().info("Amazon website lunched successfully")
        except Exception as e:
            cl.allurelogs(f"Amazon website lunch failed with exception {e}")
            cl.customlogger().error(f"Amazon website lunch failed with exception {e}")

    @allure.step("clicking on hamburger menu and clicking on tv and appliance button")
    def click_tv(self):
        try:
            self.click_webelement(self.hamburger_menu_icon, "xpath")
            self.scrollto(self.tv_appliance_button, "xpath")
            self.click_webelement(self.tv_appliance_button, "xpath")
            self.click_webelement(self.tv_button, "xpath")
            self.scrollto(self.samsung_tv_select, "xpath")
            self.click_webelement(self.samsung_tv_select, "xpath")
            self.scrollto(self.all_result_button, "xpath")
            self.click_webelement(self.all_result_button, "xpath")
            cl.allurelogs("performed all the operation and navigated to all result section")
            cl.customlogger().info("performed all the operation and navigated to all result section")
        except Exception as e:
            cl.allurelogs(f"Hamburger menu operation failed with exception:{e}")
            cl.customlogger().error(f"Hamburger menu operation failed with exception:{e}")

    @allure.step("Working on sort by feature")
    def sort_by_price(self):
        try:
            self.click_webelement(self.filter_button, "xpath")
            self.click_webelement(self.high_low_sort, "xpath")
            cl.allurelogs("clicked on filter and sorted")
            cl.customlogger().info("clicked on filter and sorted")
        except Exception as e:
            cl.allurelogs(f"price selection failed with exception:{e}")
            cl.customlogger().error(f"price selection failed with exception:{e}")

    @allure.step("Getting all the prices and performing different action on it")
    def price_manipulation(self):
        try:
            list_of_price = self.get_web_elements(self.list_of_all_price, "xpath")
            list_temp = []
            for element in list_of_price:
                list_temp.append(element.text)
                list_temp = list(dict.fromkeys(list_temp))
            return list_temp
        except Exception as e:
            cl.allurelogs(f"Failed to work on price list with exception:{e}")
            cl.customlogger().error(f"Failed to work on price list with exception:{e}")


