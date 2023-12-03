import allure
import io
from PIL import Image, ImageDraw
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from config.lincs import Links

class Base:

    LOCATOR = ('xpath', '')


    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)


    def open(self, url: str) -> None:
        with allure.step(f'Open {url} page'):
            self.driver.get(url)

    def is_opened(self, url: str) -> None:
        with allure.step(f'Page {url} is opened'):
            self.wait.until(EC.url_to_be(url))


    def element_is_visible(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def element_not_visible(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator: tuple) -> object:
        """Проверка видимости элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))


    def click(self, locator: tuple) -> object:
        self.element_is_visible(locator)
        self.element_is_clickable(locator).click()


    def make_screenshot(self, screen_name, element_selector):
        # Получение скриншота страницы
        screenshot = self.driver.get_screenshot_as_png()

        # Открытие скриншота с использованием Pillow
        image = Image.open(io.BytesIO(screenshot))
        draw = ImageDraw.Draw(image)

        # Получение элемента для выделения рамкой
        element = self.element_is_visible(element_selector)
        element_location = element.location
        element_size = element.size

        # Отрисовка рамки вокруг элемента
        draw.rectangle(
            [
                (element_location['x'], element_location['y']),
                (element_location['x'] + element_size['width'], element_location['y'] + element_size['height'])
            ],
            outline="green",  # Цвет рамки (красный)
            width=5  # Ширина рамки
        )

        # Сохранение отредактированного изображения
        screenshot = io.BytesIO()
        image.save(screenshot, format='PNG')

        allure.attach(
            body=screenshot.getvalue(),
            name=f"{screen_name}",
            attachment_type=AttachmentType.PNG
        )







