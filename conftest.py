import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11.0",  # 📌 Update if you're using another version
        "deviceName": "emulator-5554",  # 📌 Make sure this matches your AVD
        "app": "app/Android-MyDemoAppRN.1.3.0.buil-244.apk",  # ✅ Relative path to your APK
        "appPackage": "com.saucelabs.mydemoapp.rn",
        "appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
        "automationName": "UiAutomator2"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()
