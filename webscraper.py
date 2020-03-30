# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://live.euronext.com'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

links = soup.findAll('a')


for i in range(len(links)):
    if 'AEX' in str(links[i]):
        aex_link = links[i]['href']
        
data = urllib.request.urlopen(url+aex_link)
        
aex_response = requests.get(url+aex_link)
spans = soup.findAll('a')

for i in range(len(spans)):
    if 'csv' in str(spans[i]):
        price = links[i]['href']