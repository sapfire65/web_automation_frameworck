import pytest
from base.base_functions import Base
from page.vacancy_page import VacancyPage
from config.lincs import Links


class TestAnnotations:

    base_functions = Base
    vacancy_page = VacancyPage
    lincs = Links


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.base_functions = Base(driver)
        request.cls.vacancy_page = VacancyPage(driver)
        request.cls.lincs = Links()
