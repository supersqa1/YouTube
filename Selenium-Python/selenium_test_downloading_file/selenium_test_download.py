from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import tempfile
import time

temp_download_dir = tempfile.mkdtemp()
expected_file_name = 'data.csv'
expected_path = os.path.join(temp_download_dir, expected_file_name)

current_file_path = os.path.dirname(os.path.realpath(__file__))
html_file = os.path.join(current_file_path, 'index.html')

chrome_options = Options()

chrome_options.add_experimental_option("prefs", {
    "download.default_directory": temp_download_dir
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("file://" + html_file)
driver.find_element(By.ID, "main_download").click()

max_wait = 3  # sec
timeout = time.time() + max_wait

while time.time() < timeout:
    print(os.listdir(temp_download_dir))
    if os.path.isfile(expected_path):
        with open(expected_path, 'r') as f:
            downloaded_content = f.read()
        break
    else:
        time.sleep(.5)


with open(os.path.join(current_file_path, 'data.csv'), 'r') as f:

    originla_content = f.read()

assert originla_content == downloaded_content
print("PASS")