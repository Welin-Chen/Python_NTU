import requests
from bs4 import BeautifulSoup
url = "https://www.dcard.tw/f"
r = requests.get(url)
html = r.text
# print(html)
soup = BeautifulSoup(html, 'html5lib')
lines = soup.find_all(class_='tgn9uw-2')
# print(lines)
s = ''
for line in lines:
    s += line.text+'\n'
print(s)

f1 = open('web01_03_dcard.txt', 'w', encoding='utf-8')
f1.write(s)
f1.close()
