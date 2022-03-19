import requests
import matplotlib.pylab as plt
from bs4 import BeautifulSoup
from collections import Counter
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontManager

# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2007001000&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page="

list_1 = []
for page in range(1, 151):  # 爬多個page
    r = requests.get(url + str(page))  # 讀取網站
    html = r.text  # 讀取網站的文字
    # print(html)
    soup = BeautifulSoup(html, 'html5lib')  # 解析網站的文字
    lines = soup.find_all(class_='js-job-link')  # 尋找網站class標籤後的文字
    # lines = soup.find_all(class_='b-block__left')
    # lines = soup.find_all(id='js-job-content')

    # print(lines)
    if(page == 1):
        s = ''
    for line in lines:
        s += line.text+'\n'  # 將網站文字存進字串
        list_1.append(line.text)  # 將字串存進串列
    # print(s)

f1 = open('web01_final.txt', 'w', encoding='utf-8')  # 開啟檔案
f1.write(s)  # 寫入檔案
f1.close()  # 關閉檔案

words = list_1
word_counts = Counter(words)  # 計數串列
# 出現頻率最高的3個單詞
top_three = word_counts.most_common(5)  # 挑出串列中出現頻率最高的詞
# print(top_three)
list_word = []
for i in top_three:
    list_word.append(list(i))  # 將出現頻率高的詞以串列存儲
    print(i)

name = []
num = []
for i in range(len(list_word)):
    name.append(list_word[i][0])
    num.append(list_word[i][1])

text_name = "總樣本數="+str(len(list_1))
print(text_name)
y = num
x = range(len(num))
plt.bar(x, y, 0.35)
plt.title('軟體工程師職缺分析')  # 表格名稱
plt.text(len(num)-1.5, num[0], text_name)
plt.ylabel('數量')  # y軸標題
plt.xticks(x, name)  # 設定x軸刻度
plt.show()  # 顯示繪製的圖形
