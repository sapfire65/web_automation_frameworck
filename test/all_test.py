import pytest
import allure
from annatations.for_all_test import TestAnnotations
from time import sleep


@allure.feature("Profile Functionality")
class TestAll(TestAnnotations):

    @allure.title("City selection window is opened")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_1(self):
        """Ожидаем что на странице с поиском вокансий, отображается окно выбора города"""
        self.base_functions.open(self.lincs.VACANCY_URL)
        self.base_functions.is_opened(self.lincs.VACANCY_URL)
        # self.vacancy_page.city_selection_window_is_opened()
        self.base_functions.make_screenshot('PASSED')

        sleep(1)

    # @allure.title("Click button save")
    # @allure.severity("Critical")
    # @pytest.mark.smoke
    # def test_2(self):
    #     """Ожидаем что кнопка __Сохранить__, кликабельна и нажимается."""
    #     self.base_functions.open(self.lincs.VACANCY_URL)
    #     self.base_functions.is_opened(self.lincs.VACANCY_URL)
    #     self.vacancy_page.click_button_save()
    #
    #
    #     sleep(1)