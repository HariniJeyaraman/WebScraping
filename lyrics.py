import requests
from bs4 import BeautifulSoup
query=input("Enter the Song Name:  ")
#print(query.split())
array=query.split()
url="https://www.google.co.in/search?q=+lyrics"
for ch in url:
	if ch=='=':
		url+=str(array)
#res=requests.get("https://www.google.co.in/search?q=hall+of+fame+lyrics")
res=requests.get(url)
res.text
soup=BeautifulSoup(res.text,'html.parser')
for links in soup.find_all('a'):
    if "azlyrics" in links.get('href'):
         start=links.get('href').find("https")
         end=links.get('href').find("html")
         myLink = links.get('href')[start:end+4] 
res=requests.get(myLink)
res.text
soup=BeautifulSoup(res.text,'html.parser')
print(soup.find_all('div')[21].get_text())
