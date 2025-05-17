from selenium.webdriver.common.by import By

def test_logout(driver):
    driver.find_element(By.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(By.ACCESSIBILITY_ID, "username").send_keys("standard_user")
    driver.find_element(By.ACCESSIBILITY_ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ACCESSIBILITY_ID, "login-button").click()

    driver.find_element(By.ACCESSIBILITY_ID, "open menu").click()
    driver.find_element(By.ACCESSIBILITY_ID, "menu item logout").click()

    assert "Login" in driver.page_source
