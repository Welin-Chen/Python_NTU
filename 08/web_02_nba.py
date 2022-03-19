import requests
from bs4 import BeautifulSoup
url = "https://www.ptt.cc/bbs/NBA/index.html"
r = requests.get(url)
html = r.text
# print(html)
soup = BeautifulSoup(html, 'html5lib')
lines = soup.find_all(class_='title')
print(lines)
s = ''
for line in lines:
    s += line.text.strip()+'\n'
    # print(line.a['href'])
print(s)
f1 = open('web01_02_nba.txt', 'w', encoding='utf-8')
f1.write(s)
f1.close()
