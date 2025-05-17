from selenium.webdriver.common.by import By

def test_checkout_flow(driver):
    driver.find_element(By.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(By.ACCESSIBILITY_ID, "username").send_keys("standard_user")
    driver.find_element(By.ACCESSIBILITY_ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ACCESSIBILITY_ID, "login-button").click()

    driver.find_element(By.ACCESSIBILITY_ID, "test-Item 1 title").click()
    driver.find_element(By.ACCESSIBILITY_ID, "Add To Cart button").click()
    driver.find_element(By.ACCESSIBILITY_ID, "cart").click()
    driver.find_element(By.ACCESSIBILITY_ID, "Proceed To Checkout button").click()

    assert "Checkout Complete" in driver.page_source
