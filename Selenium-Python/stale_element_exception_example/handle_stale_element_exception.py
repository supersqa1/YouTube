"""
The 'StaleElementReferenceException' occurs in Selenium when the element you're trying to 
interact with is no longer attached to the DOM. This usually happens when the page has been 
updated or the element has been reloaded, causing Selenium to lose its reference to the 
original element. To fix this, you need to refetch the element from the DOM before 
interacting with it again.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import os

driver = webdriver.Chrome()
driver.implicitly_wait(5)

directory = os.path.dirname(os.path.abspath(__file__))
url = os.path.join(f"file://{directory}/page_to_cause_stale_element_exception.html")

driver.get(url)

try:
    button1 = driver.find_element(By.ID, 'myButton1')
    button2 = driver.find_element(By.ID, 'myButton2')

    button1.click()
    button2.click()
except StaleElementReferenceException as e:
    print("A 'StaleElementReferenceException' happened. Retrying in 2 seconds.")
    time.sleep(2)
    button2 = driver.find_element(By.ID, 'myButton2')
    button2.click()

print("PASS")
driver.quit()