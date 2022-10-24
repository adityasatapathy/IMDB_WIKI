import unittest
import pytest
from PageObject.login_page import LogIn
from base.baseclass import Baseclass1
from constants.login_constants import LoginConstants


class TestAmazon(Baseclass1, unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object(self):
        self.base = Baseclass1()
        self.loginpage = LogIn(self.driver)
        self.loginconst = LoginConstants()

    def test_tc01_login_func(self):
        self.loginpage.login_home()

    def test_tc02_home(self):
        self.loginpage.click_tv()
        self.loginpage.sort_by_price()
        price_lst = self.loginpage.price_manipulation()
        mx = max(price_lst[0], price_lst[1])
        secondmax = min(price_lst[0], price_lst[1])
        n = len(price_lst)
        for i in range(0, n-1):
            if price_lst[i] > mx:
                secondmax = mx
                mx = price_lst[i]
            elif secondmax < price_lst[i] != mx:
                secondmax = price_lst[i]
            elif mx == secondmax and \
                    secondmax != price_lst[i]:
                secondmax = price_lst[i]

        second_higest = secondmax
        print(second_higest)
        element_selection = f"//span[contains(text(), 'Samsung')]/../../../../div/div[1]/a/span/span/span[2][contains(text(),'{second_higest}')]"
        self.click_webelement(element_selection, "xpath")
