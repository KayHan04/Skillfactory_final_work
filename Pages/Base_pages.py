import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/auth"
        self.url_lk = "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Not find{locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver).until(EC.presence_of_all_elements_located(locator),
                                                  message=f"Not find{locator}")

    def go_to_main_url_lk(self):
        return self.driver.get(self.url_lk)


