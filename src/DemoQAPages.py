from src.BaseApp import BasePage
from selenium.webdriver.common.by import By


class DemoQASearchLocators:
    LOCATOR_ELEMENTS_BUTTON = (By.XPATH,
                               '//div[@class="card-body"]/*[contains(text(),"Elements")]')
    LOCATOR_CHECKBOX_BUTTON = (By.XPATH,
                               '//ul[@class="menu-list"]/li/span[contains(text(),"Check Box")]')
    LOCATOR_TOGGLE_HOME = (By.XPATH,
                           '//label[@for="tree-node-home"]/preceding::button[@title="Toggle"][1]')
    LOCATOR_TOGGLE_DOWNLOADS = (By.XPATH,
                                '//label[@for="tree-node-downloads"]/preceding::button[@title="Toggle"][1]')
    LOCATOR_CHECK_WORDFILE = (By.XPATH, '//label[@for="tree-node-wordFile"]')
    LOCATOR_CHECK_EXCELFILE = (By.XPATH, '//label[@for="tree-node-excelFile"]')
    LOCATOR_RESULT = (By.ID, 'result')


class SiteHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(DemoQASearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_elements_button(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_ELEMENTS_BUTTON, time=2).click()

    def select_checkbox_in_menu(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_CHECKBOX_BUTTON, time=2).click()

    def expand_home(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_TOGGLE_HOME, time=2).click()

    def expand_downloads(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_TOGGLE_DOWNLOADS, time=2).click()

    def check_wordfile(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_CHECK_WORDFILE, time=2).click()

    def check_excelfile(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_CHECK_EXCELFILE, time=2).click()

    def check_result(self):
        return self.find_element(DemoQASearchLocators.LOCATOR_RESULT, time=2).text
