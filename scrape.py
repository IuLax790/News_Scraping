from bs4 import BeautifulSoup

import requests
import pandas as pd
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
my_url = "https://www.cnbc.com/world/?region=world"

my_headers = {'User-Agent':user_agent}
response=requests.get(my_url,headers=my_headers)
data = response.content # The data u need


from bs4 import BeautifulSoup
soup = BeautifulSoup(data,"html.parser")

Markets = []

list1=soup.findAll('span',{"class":"nav-menu-buttonText"})

print()
for child in list1:
    if child.string != None and len(child.string)<30:
        Markets.append(child.string)

my_dict = {'Markets':Markets}
df = pd.DataFrame(my_dict)
df.to_csv('Financial_News.csv')

Titles = []


list2 = soup.findChildren('div')
for elem in list2:
    if elem.string != None and len(elem.string)<30:
        Titles.append(elem.string)
my_dict = {'Titles':Titles}
df1 = pd.DataFrame(my_dict)
df1.to_csv('Headers.csv')
