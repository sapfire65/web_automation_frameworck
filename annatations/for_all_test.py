import pytest
from base.base_functions import Base


class TestAnnotations:

    base_functions = Base


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):

        request.cls.driver = driver
        request.cls.base_functions = Base(driver)
