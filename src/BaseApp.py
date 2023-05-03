from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager


class BasePage:

    def __init__(self, driver, base_url='https://ya.ru'):
        # Browsers = {
        #     'firefox': webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())),
        #     'chrome': webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
        #     'safari': webdriver.Safari
        # }
        if driver.lower() == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif driver.lower() == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif driver.lower() == 'ie':
            self.driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
        else:
            raise ('Unsupported Browser')

        # self.driver = Browsers[driver]()
        self.driver.implicitly_wait(10)
        self.base_url = base_url

    def __del__(self):
        self.driver.quit()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(expected_conditions.presence_of_element_located(locator),
                  message=f'Can not find element by locator {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time). \
            until(expected_conditions.presence_of_all_elements_located(locator),
                  message=f'Can not find elements by locator {locator}')

    def go_to_site(self):
        return self.driver.get(self.base_url)
