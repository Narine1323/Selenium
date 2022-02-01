from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CustomFindElement():
    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self, locator):
        try:

            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            #element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "exports_desktop_qualifiedBuybox_atc_feature_div"))).click()


        except:
            print("apsos")

        return element


