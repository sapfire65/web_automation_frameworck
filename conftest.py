import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True, scope='function')
def driver(request):

    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920, 1080')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()

