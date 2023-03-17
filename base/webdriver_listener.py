import pytest
from selenium import webdriver
from utilities import read_utils


class WebdriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        browser_name = read_utils.get_value_from_json("../test_data/data.json", "browser")
        if browser_name == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_name == "ff":
            self.driver = webdriver.firefox
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()
