import requests
from bs4 import BeautifulSoup

url='http://devpyjp.com/'
res=requests.get(url).content
soup=BeautifulSoup(res,'html.parser')

images=soup.find_all('img')

for img in images:
    print(img['src'])