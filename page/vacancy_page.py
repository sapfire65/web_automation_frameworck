import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from colorama import Fore, Style
from config.lincs import Links
from base.base_functions import Base
from time import sleep

class VacancyPage(Base):

    LIST_CITY = ('xpath', '//div[@class="select__trigger has-value"]')
    BUTTON_SAVE = ('xpath', '(//button[@type="button"])[1]')
    FRAME = ('xpath', '//div[@class="modal__content"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)


    @allure.step("The city selection window is open")
    def city_selection_window_is_opened(self):
        self.element_is_visible(self.FRAME)

    @allure.step("Click button SAVE for city")
    def click_button_save(self):
        self.click(self.BUTTON_SAVE)


