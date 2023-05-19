import email
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from utilties.Logger import LogGenerator
class Test_Login:
    log=LogGenerator.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.log.info("Opening Browser ")
        self.lp = LoginPage(self.driver)
        self.log.info("Start to login")
        self.lp.Enter_Email("admin@yourstore.com")
        self.log.info("Enter Username")
        self.log.info("Enter Username ")

        self.lp.Enter_Password("admin")
        self.log.info("Enter Username ")

        self.lp.Click_Login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.lp.Click_Logout()
            assert True
        else:
            assert False
