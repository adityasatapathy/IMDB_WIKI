import configparser
import time
from traceback import print_stack
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import Utilities.customlogger as cl
import allure


@pytest.mark.usefixtures("setup_browser")
class Baseclass1:
    pass

    log = cl.customlogger()

    # function to read the data from config file
    def configReader(self, section, field):
        """
        Function to read the config file
        :param section:
        :param field:
        :return:
        """
        try:
            config = configparser.RawConfigParser()
            # config.read('..\\Configuration\\config_local.properties')
            config.read('C://Users//user//PycharmProjects//IMDB_WIKI//Cofiguration//config_local.properties')
            return config.get(section, field)
        except Exception as e:
            self.log.error(f"Exception '{e}' while reading config file")

    # function which invoking driver and opens the URl
    def lunch_webpage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info(f"Web Page lunched wth url:{url}")
        except:
            self.log.info(f"Web Page failed to lunch with url:{url}")

    # function which identifies the locator type as per page object
    def getlocatortype(self, locatortype):
        """ This method defines the locator types for the page object"""
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "tag":
            return By.TAG_NAME
        elif locatortype == "link_text":
            return By.LINK_TEXT
        elif locatortype == "p_link_text":
            return By.PARTIAL_LINK_TEXT
        elif locatortype == "class":
            return By.CLASS_NAME
        else:
            self.log.error(f"locator type with:{locatortype} not found")
            return False

    # function which can be used through out the framework to find the WebElement
    def get_web_element(self, locatorvalue, locatortype="id"):
        """This method is commonly used function by which we can get any web element"""
        webelement = None
        try:
            locatortype = locatortype.lower()
            locatorBytype = self.getlocatortype(locatortype)
            webelement = self.driver.find_element(locatorBytype, locatorvalue)
            self.log.info(f"Web Element found with the locator value:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Web Element not found with the locator value:{locatorvalue} with the locator type:{locatortype}")
            print_stack()
            self.take_screenshot(locatortype)
        return webelement

    # Generic function which can be used to wait for the element until it's visible on the screen
    def wait_for_element(self, locatorvalue, locatortype):
        """This function uses explicit wait for all the element which invoke this function"""
        webelement = None
        try:
            locatortype = locatortype.lower()
            locatorBytype = self.getlocatortype(locatortype)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webelement = wait.until(ec.presence_of_element_located((locatorBytype, locatorvalue)))
            self.log.info(f"Web Element found with the locator value:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Web Element not found with the locator value:{locatorvalue} with the locator type:{locatortype}")
            print_stack()
            self.take_screenshot(locatortype)
        return webelement

    # Generic function which can be used to select any WebElement
    def click_webelement(self, locatorvalue, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            webelement = self.wait_for_element(locatorvalue, locatortype)
            webelement.click()
            self.log.info(f"Clicked on webelement with locatorvalue:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Unable to click on webelement:{locatorvalue} with the locator type:{locatortype}")
            self.take_screenshot(locatortype)
            print_stack()

    # Generic function which can be used to send text
    def sendtext(self, text, locatorvalue, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            webelement = self.wait_for_element(locatorvalue, locatortype)
            webelement.send_keys(text)
            self.log.info(f"Sent text:{text} with locatorvalue:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Unable to send text:{locatorvalue} with the locator type:{locatortype}")
            self.take_screenshot(locatortype)
            print_stack()

    # Generic function which can be used to get the text of any error message or text
    def gettext(self, locatorvalue, locatortype="id"):
        elementtext = None
        try:
            locatortype = locatortype.lower()
            webelement = self.wait_for_element(locatorvalue, locatortype)
            elementtext = webelement.text
            self.log.info(f"Got the text with locator value:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Unable to get text:{locatorvalue} with the locator type:{locatortype}")
            print_stack()
            self.take_screenshot(locatortype)
        return elementtext

    # Generic function which can be used to validate whether element is present or not
    def iselementpresent(self, locatorvalue, locatortype="id"):
        elementdisplayed = None
        try:
            locatortype = locatortype.lower()
            webelement = self.wait_for_element(locatorvalue, locatortype)
            elementdisplayed = webelement.is_displayed()
            self.log.info(f"Web element is displayed on the webpage with locator value:{locatorvalue}with the locator type:{locatortype}")
        except:
            self.log.error(f"Web element is not displayed on the webpage with locator value:{locatorvalue} with the locator type:{locatortype}")
            print_stack()
            self.take_screenshot(locatortype)
        return elementdisplayed

    # Generic function which can scroll the web page until the WebElement is displayed
    def scrollto(self, locatorvalue, locatortype="id"):
        actions = ActionChains(self.driver)
        try:
            locatortype = locatortype.lower()
            webelement = self.wait_for_element(locatorvalue, locatortype)
            actions.move_to_element(webelement).perform()
            self.log.info(f"Scrolled to webelement with locatorvalue:{locatorvalue} with the locator type:{locatortype}")
        except:
            self.log.error(f"Unable to scroll to webelement with locatorvalue:{locatorvalue} with the locator type:{locatortype}")
            print_stack()
            self.take_screenshot(locatortype)

    # function which can take screenshot and attach to report
    def take_screenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    # function which can take screenshot and store it in framework
    def screenshot(self, screenshotname):
        file_name = screenshotname + " " + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshot_location = "../Screenshots/"
        screenshot_path = screenshot_location + file_name
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info(f"Screenshot capture successfully")
        except:
            self.log.error(f"screenshot capture failed")