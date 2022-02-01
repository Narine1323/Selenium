from Locators.Locators import Locators
from Common.CustomFindElement.CustomFindElement import CustomFindElement


class BaseClass():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators()
        self.custom = CustomFindElement(driver)

