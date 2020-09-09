import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
url='https://www.flipkart.com/mobiles/~cs-e52ve74yvr/pr?sid=tyy%2C4io&collection-tab-name=Samsung%20A21s%204GB&otracker=clp_banner_1_13.bannerX3.BANNER_mobile-phones-store_A8LBUBO4X2ZJ&fm=neo%2Fmerchandising&iid=M_f7948cc8-9227-41a4-affa-6de2a5e74fc2_13.A8LBUBO4X2ZJ&ppt=clp&ppn=mobile-phones-store&ssid=hc0ri540400000001599629520836'
res=requests.get(url).content

#print(res.status_code)

#data=res.content

soup=BeautifulSoup(res,'html.parser')

#links=soup.find_all('a')
#for i in links:
 #   print(i.text.encode('utf-8'))
titles=soup.find_all('div',class_='_3wU53n')


prices=soup.find_all('div',class_='_1vC4OE _2rQ-NK')

reviews=soup.find_all('span',class_='_38sUEc')


ratings=soup.find_all('div',class_='hGSR34')

mobiles=[]
m_ratings=[]
m_reviews=[]
m_prices=[]


for title,price,review,rating in zip(titles,prices,reviews,ratings):
    #print("Ratings:",c,rating.text.strip())

    #print("Price:",price.text.strip().encode('utf-8'))
    #print("Titles:",title.text.strip())
    #print("Reviews:",review.text.strip())
    mobiles.append(title.text)
    m_ratings.append(rating.text)
    m_reviews.append(review.text)
    m_prices.append(price.text)

data = {'mobiles':mobiles,'ratings':m_ratings,'reviews':m_reviews,'prices':m_prices}

df=pd.DataFrame(data=data)

print(df.head())