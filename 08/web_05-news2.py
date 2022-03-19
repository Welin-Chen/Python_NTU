import requests
from bs4 import BeautifulSoup
url = "https://cn.wsj.com/articles/who%E6%8E%88%E4%BA%88%E4%B8%AD%E5%9C%8B%E5%9C%8B%E8%97%A5%E9%9B%86%E5%9C%98%E7%9A%84%E6%96%B0%E5%86%A0%E7%96%AB%E8%8B%97%E7%B7%8A%E6%80%A5%E4%BD%BF%E7%94%A8%E6%8E%88%E6%AC%8A-11620437411"
my_headers = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=my_headers)
print(r)
html = r.text
# print(html)
soup = BeautifulSoup(html, 'html5lib')
lines = soup.find_all(class_='wsj-snippet-body')
# print(lines)
s = ''
for line in lines:
    s += line.text+'\n'
print(s)

f1 = open('web01_05_news.txt', 'w', encoding='utf-8')
f1.write(s)
f1.close()
