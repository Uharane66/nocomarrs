import time

from selenium import webdriver

from utilties.Logger import LogGenerator


class Test_Page_Title():
    log = LogGenerator.loggen()
    def test_title(self,setup):
        self.driver=setup
        print(self.driver.title)
        self.log.info("page title testing start")
        self.driver.save_screenshot("D:\\admin_test\\Screenshots\\Testpagetitle.png")
        time.sleep(8)
        if self.driver.title=="Your store. Login":
            self.log.info("page title is ok test case pass")
            assert True
        else:
            self.log.info("page title is not ok test case fail")
            assert False




