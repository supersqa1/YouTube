"""
Example: Selenium Remote WebDriver with Docker Selenium Grid

This script demonstrates how to connect to a Selenium Grid hub running in Docker
and execute a simple test to get a webpage title. The script supports both
Chrome and Firefox browsers through the remote WebDriver.

Prerequisites:
    - Docker Selenium container running on localhost:4444
    - Selenium Grid hub accessible at http://localhost:4444/wd/hub
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

# Configuration
BROWSER = "chrome"  # Options: "chrome", "firefox"
HUB_URL = "http://localhost:4444/wd/hub"

print(f"Starting Remote Selenium script with {BROWSER}...")

# Set options based on BROWSER variable
if BROWSER.lower() == "chrome":
    options = ChromeOptions()
elif BROWSER.lower() == "firefox":
    options = FirefoxOptions()
else:
    raise ValueError(f"Unsupported browser: {BROWSER}")

try:
    # Initialize Remote WebDriver
    driver = webdriver.Remote(
        command_executor=HUB_URL,
        options=options
    )
    
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
