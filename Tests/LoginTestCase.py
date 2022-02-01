import time
from Pages.Common.baseClass import BaseClass

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.LogIn.loginpage import LoginPage
from Pages.Home.HomePage import HomePage
from Pages.Home.productdetails import ProductDetails
from Pages.Home.buyNow import Buy_Now
from pathlib import Path
from Locators.Locators import Locators
from Pages.LogIn.customeReviews import Customers_Review_Filter
from Pages.LogIn.passwordPage import Password_field
from Pages.Home.searchpage import SearchPage
from Pages.Home.product_page import ProductPage

import unittest

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.PATH = "../Common/driver/chromedriver.exe"
        cls.driver = webdriver.Chrome(cls.PATH)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)



    def test_signIn(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")


        loginPage = LoginPage(self.driver)
        loginPage.fill_logIn("nan.kalashyan@gmail.com")
        time.sleep(2)
        loginPage.continue_btn()
        passwordPage = Password_field(self.driver)
        passwordPage.fill_password("Amazon131313")
        passwordPage.checkBox()
        passwordPage.signIn()
        searchfield = SearchPage(self.driver)
        searchfield.search_field()
        productPage = ProductPage(self.driver)
        productPage.selectedPrice()
        productPage.customer_review_click()
        productPage.click_on_my_choice()
        producDetails = ProductDetails(self.driver)
        producDetails.select_quantity_of_product()
        producDetails.click_on_selected_quantity()





















    #@classmethod
    #def tearDownClass(cls):
        #cls.driver.close()


    #def tearDown(self):
    # self.driver.close()








