
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import os
os.getcwd()

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("http://www.python.org")



try:
    assert "Python" in driver.title
    print("Pass")

except Exception()  as e:
    print("Fail")


elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
