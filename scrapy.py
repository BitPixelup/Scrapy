import requests
from bs4 import BeautifulSoup

url = input("Paste your url here:")

def fetchdata(url):  # to fetch URL
	r = requests.get(url)  
	return r.text
	
htmldata = fetchdata(url) # to prettify the data
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
	print(item['src'])