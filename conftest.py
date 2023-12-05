import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True, scope='function')
def driver(request):
    ua_string = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'

    chrome_options = Options()
    chrome_options.add_argument(f'--user-agent={ua_string}')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--ignore-ssl-errors")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-certificate-errors-spki-list")
    # chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--homedir=/tmp")
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.close()
    driver.quit()


'''

console comands to START:
pytest --alluredir=report;  allure serve report

'''