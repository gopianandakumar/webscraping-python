import mechanize
from bs4 import BeautifulSoup

mc=mechanize.Browser()

url='https://www.findandtrace.com/trace-mobile-number-location'

mc.open(url)
mc.select_form('trace')
mc['mobilenumber']=input('enter number')

res=mc.submit().read()

#print(res)
soup=BeautifulSoup(res,'html.parser')

table=soup.find('table',class_='shop_table')

print(table)

data= table.find('tfoot')

#print(data)
c=0
for i in data:
    c+=1
    if c in (1,4,6,8):
        continue
    th = i.find('th')
    td = i.find('td')
    print('-',th.text,td.text)