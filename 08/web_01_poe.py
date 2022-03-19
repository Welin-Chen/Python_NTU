# 爬蟲
# 載入套件
import requests
from bs4 import BeautifulSoup
url = "https://jgirl.ddns.net/WebPages/%E9%95%B7%E6%81%A8%E6%AD%8C.htm"
# 讀取資料
r = requests.get(url)
# print(r.content[:200].decode('utf-8'))
# 把文字部分取出
html = r.text
# print(html.find('漢皇重色思傾國，御宇多年求不得。'))
# 使用解析器html5lib
soup = BeautifulSoup(html, 'html5lib')
lines = soup.find_all(class_='MsoNormal')
# print(type(lines))
# print(lines)
# print(lines[0].text)
s = ''
for line in lines:
    s += line.text+'\n'
print(s)

f1 = open('web01_01_poe.txt', 'w', encoding='utf-8')
f1.write(s)
f1.close()
