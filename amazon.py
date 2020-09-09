import requests
from bs4 import BeautifulSoup


res=requests.get('https://www.amazon.com/')

print(res.status_code)

data=res.content

soup=BeautifulSoup(data,'html.parser')

links=soup.find_all('h2')
for i in links:
    print(i.text);