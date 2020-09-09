import requests
from bs4 import BeautifulSoup

url="https://www.indiatoday.com/"

res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')

#print(soup.prettify().encode('utf-8'))
#a_tag=soup.find_all('a')
#for i in a_tag:
#   print(i.get('href'))

#h3_tag=soup.find_all('h3')
#for i in h3_tag:
 #   print(i.text)
 # 
for h3_tag in soup.find_all('h3'):
    for a_tag in h3_tag.find_all('a'):
        print(a_tag.text) 
        print(url+a_tag.get('href'))