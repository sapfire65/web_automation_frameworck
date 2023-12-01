from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from config.lincs import Links

class Base:
    LOCATOR = ('xpath', '')


    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)


    def open(self, url):
        self.driver.get(url)

    def open_ozone_page(self):
        url = Links.JOB_URL
        self.open(url)

