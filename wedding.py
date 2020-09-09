import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.wedmegood.com/vendors/bangalore/planners/'
res=requests.get(url).content
#print(res.status_code)
#print(res.text.encode('utf-8'))
soup=BeautifulSoup(res,'html.parser')

infos=soup.find('div',class_='vendor-info')

#print(infos)
c=1
planners=[]
locations=[]
reviews=[]
ratings=[]
prices=[]
for info in infos:
      planner=info.find('a',class_='vendor-detail')
      #print(c,planner.text.strip())
      planners.append(planner)

      rating=info.find('span',class_='StarRating')
      #print(rating.text.strip())
      ratings.append(rating)

      location=info.find('p',class_='vendor-detail')
      #print(location.text.strip())
      locations.append(location)

      review=info.find('span',class_='review-cnt')
      #print(review.text.strip())
      reviews.append(review)

      price=soup.find('span',class_=" ")
      #print(price)
      prices.append(price)
      #print(' ')
      c+=1

data={'Planners':planners,'Ratings':ratings,'Prices':prices,'Locations':locations,'Reviews':reviews}

df=pd.DataFrame(data=data)
print(df.head())
