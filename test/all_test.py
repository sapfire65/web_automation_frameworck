import pytest
import allure
from annatations.for_all_test import TestAnnotations
from time import sleep


@allure.feature("Profile Functionality")
class TestAll(TestAnnotations):

    @allure.title("Logo BMW is visible")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_logo_bmw_is_visible(self):
        """Ожидаем что на странице отображается логотип компании BMW"""
        self.base_functions.open(self.lincs.ALL_MODELS)
        self.base_functions.is_opened(self.lincs.ALL_MODELS)
        self.all_models_page.logo_is_visible()

    @allure.title("BMW logo is clickable")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_logo_bmw_is_clickable(self):
        """Ожидаем что логотип BMW - кликабельный"""
        self.base_functions.open(self.lincs.ALL_MODELS)
        self.base_functions.is_opened(self.lincs.ALL_MODELS)
        self.all_models_page.logo_is_clickable()

    @allure.title("First icon auto is clickable")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_first_auto_is_klickable(self):
        """Ожидаем что первая иконка с машиной - кликабельна"""
        self.base_functions.open(self.lincs.ALL_MODELS)
        self.base_functions.is_opened(self.lincs.ALL_MODELS)
        self.all_models_page.first_auto_is_klickable()

    @allure.title("Car preview after click")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_car_preview_after_click(self):
        """Ожидаем что после коика на иконку, отображается превью модели машины"""
        self.base_functions.open(self.lincs.ALL_MODELS)
        self.base_functions.is_opened(self.lincs.ALL_MODELS)
        self.all_models_page.car_preview_after_click()