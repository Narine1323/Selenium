import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.Locators import Locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement
from Pages.Common.baseClass import BaseClass

class Password_field(BaseClass):
    def __init__(self, driver):
        BaseClass.__init__(self, driver)


    def fill_password(self, password):
        password_field = self.driver.find_element(self.locators.passwordTextBox[0], self.locators.passwordTextBox[1])
        password_field.clear()
        password_field.send_keys("Amazon131313")


    def checkBox(self):
        checkBox = self.driver.find_element(self.locators.checkBox[0], self.locators.checkBox[1])
        time.sleep(2)
        checkBox.click()

    def signIn(self):
        signIn_Btn = self.driver.find_element(self.locators.sign_in[0], self.locators.sign_in[1])
        signIn_Btn.click()