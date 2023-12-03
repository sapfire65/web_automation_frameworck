import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from colorama import Fore, Style
from config.lincs import Links
from base.base_functions import Base
from time import sleep

class AllModels(Base):


    LOGO_BMW = ('xpath', '(//a[@class="cmp-globalnavigation__logo"])[1]')
    FIRST_AUTO_ICON = ('xpath', '(//button[@class="cmp-modelcard__button"])[1]')
    PREVIEW_CAR = ('xpath', '//img[@class="cmp-modelselection__detail-view--image style-lazyload__loaded"]')
    SELECTOR = ('xpath', '')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)



    @allure.step("Logo BMW is visible")
    def logo_is_visible(self):
        """Лого отображается"""
        self.element_is_visible(self.LOGO_BMW)
        self.make_screenshot('PASS', self.LOGO_BMW)

    @allure.step("Logo BMW is clickable")
    def logo_is_clickable(self):
        """Логотип кликабельный"""
        self.element_is_clickable(self.LOGO_BMW)
        self.make_screenshot('PASS', self.LOGO_BMW)


    @allure.step("First Icon Auto is clickable")
    def first_auto_is_klickable(self):
        """Картинки машин кликабельны"""
        self.click(self.FIRST_AUTO_ICON)
        self.make_screenshot('PASS', self.FIRST_AUTO_ICON)

    @allure.step("Open preview is car")
    def car_preview_after_click(self):
        """После клика по первой картике, отображается превью - подробнее о машине"""
        self.click(self.FIRST_AUTO_ICON)
        self.element_is_visible(self.PREVIEW_CAR)
        self.make_screenshot('PASS', self.PREVIEW_CAR)

