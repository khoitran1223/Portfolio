from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pytest

@pytest.fixture(scope="class")
def setup(request):
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 20)
    request.cls.driver = driver
    request.cls.wait = wait
    driver.get("https://www.vemaybay.vn/")
    yield
    driver.close()