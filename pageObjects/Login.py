import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    Text_Email_XPATH = (By.XPATH, "//input[@id='Email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Click_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_customer_list = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    Click_serch_button = (By.CSS_SELECTOR, "body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)")
    Search_Emp_Email_Xpath=(By.XPATH,"//input[@id='SearchEmail']")
    Search_button_click_Xpath=(By.XPATH,"//button[@id='search-customers']")
    Click_add_emp_Xpath=(By.XPATH,"//a[@class='btn btn-primary']")
    Insert_Emali_New_Emp_Xpath=(By.XPATH,"//input[@id='Email']")
    Insert_Password_New_Emp_Xpath=(By.XPATH,"//input[@id='Password']")
    Insert_First_name_New_Emp_Xpath=(By.XPATH,"//input[@id='FirstName']")
    Insert_Last_name_New_Emp_Xpath=(By.XPATH,"//input[@id='LastName']")

    Insert_Gender_New_Emp_Xpath=(By.XPATH,"//input[@id='Gender_Male']")
    Insert_Data_of_multipe_button_New_Emp_Xpath=(By.XPATH,"//span[@class='k-icon k-i-calendar']")
    Insert_Data_of_button_New_Emp_Xpath=(By.XPATH,"//a[@title='Tuesday, May 9, 2023']")
    Insert_Company_New_Emp_Xpath=(By.XPATH,"//input[@id='Company']")
    Insert_Save_info_Xpath=(By.XPATH,"//button[@name='save']")






    CLick_Logout_XPATH = (By.XPATH, "//i[@class='fas fa-cogs']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Email(self, email):
        self.driver.find_element(*LoginPage.Text_Email_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_XPATH).clear()
        self.driver.find_element(*LoginPage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*LoginPage.Click_Login_XPATH).click()

    def Customer_Click1(self):
       time.sleep(6)
       self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")))
       self.driver.find_element(*LoginPage.Click_customer_list).click()


    def Serch_customer_click(self):
        time.sleep(5)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(3) > aside:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > p:nth-child(2)")))
        self.driver.find_element(*LoginPage.Click_serch_button).click()

    def Add_EMP_button(self):
        time.sleep(4)
        self.driver.find_element(*LoginPage.Click_add_emp_Xpath).click()

    def Input_Email(self,Email_emp):
        time.sleep(2)
        self.driver.find_element(*LoginPage.Insert_Emali_New_Emp_Xpath).send_keys(Email_emp)

    def Input_Password(self,Password):
        self.driver.find_element(*LoginPage.Insert_Password_New_Emp_Xpath).send_keys(Password)

    def Input_First_name(self,First_name):
        self.driver.find_element(*LoginPage.Insert_First_name_New_Emp_Xpath).send_keys(First_name)

    def Input_Last_name(self,Last_name):
        self.driver.find_element(*LoginPage.Insert_Last_name_New_Emp_Xpath).send_keys(Last_name)

    def Click_Gender_button(self):
        self.driver.find_element(*LoginPage.Insert_Gender_New_Emp_Xpath).click()

    def Click_data_button(self):
        self.driver.find_element(*LoginPage.Insert_Data_of_multipe_button_New_Emp_Xpath).click()

    def Click_date_button_second(self):
        self.driver.find_element(*LoginPage.Insert_Data_of_button_New_Emp_Xpath).click()

    def Company_name(self,company):
        self.driver.find_element(*LoginPage.Insert_Company_New_Emp_Xpath).send_keys(company)

    def Save_button(self):
        self.driver.find_element(*LoginPage.Insert_Save_info_Xpath).click()
    def Search_Emp_Email(self,email):
        time.sleep(4)
        self.driver.find_element(*LoginPage.Search_Emp_Email_Xpath).send_keys(email)

    def Search_Emp_button(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Click_serch_button).click()

    def Click_Logout(self):
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "//i[@class='fas fa-cogs']")))
        self.driver.find_element(*LoginPage.CLick_Logout_XPATH).click()






