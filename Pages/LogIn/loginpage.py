import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.Locators import Locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement
from Pages.Common.baseClass import BaseClass


class LoginPage(BaseClass):
    def __init__(self, driver):
        #self.driver = driver
        BaseClass.__init__(self, driver)
        #self.locators = locators
        #self.custom = CustomFindElement(driver)

    def continue_btn(self):
            continue_button = self.driver.find_element(By.ID, "continue")
            continue_button.click()

    def fill_logIn(self, logIn):
        login_field = self.driver.find_element(self.locators.logInTextBox[0], self.locators.logInTextBox[1])
        login_field.clear()
        login_field.send_keys("nan.kalashyan@gmail.com")




    def fill_password(self, password):
        password_field = self.driver.find_element(self.locators.passwordTextBox[0], self.locators.passwordTextBox[1])
        password_field.clear()
        password_field.send_keys("Amazon131313")





