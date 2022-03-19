import requests
from bs4 import BeautifulSoup
url = "https://news.google.com/topstories?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
r = requests.get(url)
html = r.text
# print(html)
soup = BeautifulSoup(html, 'html5lib')
lines = soup.find_all(class_='DY5T1d')
# print(lines)
s = ''
for line in lines:
    s += line.text+'\n'
print(s)

f1 = open('web01_04_news.txt', 'w', encoding='utf-8')
f1.write(s)
f1.close()
