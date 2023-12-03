import pytest
from base.base_functions import Base
from page.all_models_page import AllModels
from config.lincs import Links


class TestAnnotations:

    base_functions = Base
    all_models_page = AllModels
    lincs = Links


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.base_functions = Base(driver)
        request.cls.all_models_page = AllModels(driver)
        request.cls.lincs = Links()
