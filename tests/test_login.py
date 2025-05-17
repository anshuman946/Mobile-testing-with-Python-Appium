from selenium.webdriver.common.by import By

def test_login_valid(driver):
    driver.find_element(By.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(By.ACCESSIBILITY_ID, "username").send_keys("standard_user")
    driver.find_element(By.ACCESSIBILITY_ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ACCESSIBILITY_ID, "login-button").click()
    assert "Products" in driver.page_source

def test_login_invalid(driver):
    driver.find_element(By.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(By.ACCESSIBILITY_ID, "username").send_keys("wrong_user")
    driver.find_element(By.ACCESSIBILITY_ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ACCESSIBILITY_ID, "login-button").click()
    assert "Username and password do not match" in driver.page_source
