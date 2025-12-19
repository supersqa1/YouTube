"""
Example: Selenium Local WebDriver

This script demonstrates how to use Selenium with a local Chrome WebDriver
to execute a simple test that retrieves a webpage title. This example uses
a local browser instance (not Docker-based).

Prerequisites:
    - Chrome browser installed
    - ChromeDriver installed and in PATH
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("Starting Selenium script...")

options = Options()
# options.add_argument("--headless")

try:
    driver = webdriver.Chrome(options=options)
    driver.get("http://demostore.supersqa.com")
    
    print("**************************************************")
    print(f"\nPage Title: {driver.title}\n")
    print("**************************************************")
    
    time.sleep(2)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'driver' in locals():
        driver.quit()
