import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from config.lincs import Links

class Base:

    LOCATOR = ('xpath', '')


    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)


    def open(self, url: str) -> None:
        with allure.step(f'Open {url} page'):
            self.driver.get(url)

    def is_opened(self, url: str) -> None:
        with allure.step(f'Page {url} is opened'):
            self.wait.until(EC.url_to_be(url))


    def element_is_visible(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_not_visible(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))


    def click(self, locator: tuple) -> object:
        self.element_is_visible(locator)
        self.element_is_clickable(locator).click()


    def make_screenshot(self, screen_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screen_name,
            attachment_type=AttachmentType.PNG
        )





