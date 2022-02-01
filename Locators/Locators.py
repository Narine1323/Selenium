from selenium.webdriver.common.by import By

class Locators():
    logInTextBox = (By.ID, "ap_email")
    passwordTextBox = (By.ID, "ap_password")
    checkBox = (By.NAME, "rememberMe")
    sign_in = (By.ID, "signInSubmit")
    reviews = (By.ID, "p_72/1248963011")
    selected_price = (By.ID, 'p_36/1253561011')
    myChoice = (By.XPATH, "//img[@class='s-image'][1]")
    select_quantity = (By.XPATH, '//*[@id="selectQuantity"]/span/div/div/span')
    selected_quantity = (By.ID, 'quantity_4')



