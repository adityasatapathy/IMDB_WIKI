from selenium import webdriver
import Utilities.customlogger as cl
from base.baseclass import Baseclass1

""" This class is used for choosing the browser type at run time.
As of now in framework we are using chromedirver,
 but user can modify later by installing geckodriver and safari driver"""


class WebDriverClass:
    log = cl.customlogger()

    def getWebdriver(self, browserName):
        driver = None
        base = Baseclass1()
        if browserName == "chrome":
            driver = webdriver.Chrome(base.configReader("cred", "driver_obj"))
            driver.maximize_window()
            self.log.info("Chrome Driver is initializing")
        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Passed")
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="")
            self.log.info("Passed")
        return driver