
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def test_1():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.python.org")

    assert "Python" in driver.title
    driver.close()
