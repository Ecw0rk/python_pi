#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

# domain ='http://esf.gz.fang.com'
# headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# reqs = requests.get('http://esf.gz.fang.com/house-a072-b07469/', headers=headers)
# reqs.encoding = 'gb2312'
# soup = BeautifulSoup(reqs.text, "html5lib")
# print(len(soup.select('.houseList dl')))
# for house in soup.select('.houseList dl'):
#     if len(house) != 0:
#         # title = house.select('.title')[0].text.strip()
#         url = domain + house.select('.title a')[0]['href']
#         print(url)
#         print("=========================================")

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
res = requests.get()