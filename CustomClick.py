











'''from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECimport CustomClick


class CustomFind():
    def __init__(self, driver):
        self.driver = driver

    def custom_find(self, type : By, value = str):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((Type, value)))
        return element'''