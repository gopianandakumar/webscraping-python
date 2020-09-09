import requests
from bs4 import BeautifulSoup
import json

url='https://www.flipkart.com/the-intelligent-investor/p/itmfbqhvgjgsee2q?pid=9780062312686&lid=LSTBOK9780062312686DKBBRK&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&fm=SEARCH&iid=676c816c-a067-46ce-85ea-aaae8304020e.9780062312686.SEARCH&ppt=sp&ppn=sp&ssid=5j4senmlasci2g3k1599389809615&qH=542ef4698401d0de'
res=requests.get(url).content

soup=BeautifulSoup(res,'html.parser')

title=soup.find('span',class_='_35KyD6')
price=soup.find('div',class_='_1vC4OE _3qQ9m1')
#price=soup.find('div',class_='')
print(title.text)

print('price:',price.text.encode("utf-8"))

data=soup.find('script',id='jsonLD')
#print(data.encode('utf-8'))

context= json.loads(data)

print(context.encode('utf-8'))
