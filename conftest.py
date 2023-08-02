import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver



@pytest.fixture(params=[
    ("Credencetest@test.com","Credence@123")
])
def getDataforLogin(request):
    return request.param