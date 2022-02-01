import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path

rootDir = Path(__file__).parent
PATH = rootDir / "chromedriver.exe"
#PATH = "C:\\Users\\DELL\\Documents\\BDG\\DRIVERS\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.delete_all_cookies()

#SignIN


driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(2)
login_field = driver.find_element(By.ID, "ap_email")
login_field.clear()
login_field.send_keys("nan.kalashyan@gmail.com")
time.sleep(5)
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
time.sleep(5)
password_field = driver.find_element(By.ID, "ap_password")
password_field.clear()
time.sleep(3)
password_field.send_keys("Amazon131313")
time.sleep(3)
checkBox = driver.find_element(By.NAME, "rememberMe")
time.sleep(2)
checkBox.click()
signIn_Btn = driver.find_element(By.ID, "signInSubmit")
signIn_Btn.click()

driver.close()