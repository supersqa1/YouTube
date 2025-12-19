import requests
from bs4 import BeautifulSoup

# This requires external libraries!
url = "http://demostore.supersqa.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(f"Checking {url}...")
print(f"Status Code: {response.status_code}")
print(f"Page Title: {soup.title.string}")