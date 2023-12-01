import pytest
from annatations.for_all_test import TestAnnotations
from time import sleep

class TestAll(TestAnnotations):

    def test_1(self):
        self.base_functions.open_ozone_page()

        sleep(10)