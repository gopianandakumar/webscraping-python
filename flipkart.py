import requests
from bs4 import BeautifulSoup


res=requests.get('https://www.indiatoday.com/')

print(res.status_code)

data=res.content

soup=BeautifulSoup(data,'html.parser')

print(soup.a.text)
links=soup.find_all('a')
for i in links:
    print(i.text.encode('utf-8'));

#heads=soup.find_all('a')
#for s in heads:
 #   print(s.attrs['href'])'''