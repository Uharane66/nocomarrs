import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from utilties.Logger import LogGenerator


class Test_Login:
    log = LogGenerator.loggen()

    def test_login(self, setup):
        self.driver = setup
        self.log.info("Opening Browser ")
        self.lp = LoginPage(self.driver)
        # self.lp.implicity_wait(5)
        self.log.info("Start to login")
        self.lp.Enter_Email("admin@yourstore.com")
        self.log.info("Username Genret")

        self.lp.Enter_Password("admin")
        self.log.info("Password Genret ")
        self.lp.Click_Login()
        self.log.info("Login Button click succesfull")
        self.lp.Customer_Click1()
        self.log.info("Customer button click ")
        self.lp.Serch_customer_click()
        self.log.info("Customer Button click")
        self.lp.Add_EMP_button()
        self.log.info("start to add employee")
        self.lp.Input_Email("yashwati@xyz.com")
        self.log.info("employee email is yashwati@xyz.com")
        self.lp.Input_Password("1234879")
        self.lp.Input_First_name("Priyaka")
        self.lp.Input_Last_name("Chopda")
        self.lp.Click_Gender_button()
        self.lp.Click_data_button()
        time.sleep(6)
        self.lp.Click_date_button_second()
        self.lp.Company_name("Cummins")
        time.sleep(2)
        self.lp.Save_button()

