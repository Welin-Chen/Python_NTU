import matplotlib.pylab as plt
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import FontManager
from collections import Counter

# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 修改中文字型

f1 = open('web01_final.txt', 'r', encoding='utf-8')  # 開啟檔案
s = f1.read()  # 讀檔案
f1.close()  # 關閉檔案
# print(s)

list_s = list(s.split('\n'))  # 檔案資料依行切片存成list_s
print(list_s.pop())  # 刪掉最後一行空白行
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt_other = 0
for i in list_s:
    # print(i)
    if ('前端' in i) or ('front' in i) or ('Front' in i) or ('FRONT' in i):
        cnt1 += 1
    elif ('後端' in i) or ('back' in i) or ('Back' in i) or ('BACK' in i) or ('PHP' in i) or ('php' in i) or ('Php' in i):
        cnt2 += 1
    elif ('學習' in i) or ('深度' in i) or ('機器' in i) or ('AI' in i) or ('ai' in i) or ('Ai' in i) or ('演算法' in i):
        cnt3 += 1
    elif ('app' in i) or ('APP' in i) or ('App' in i) or ('android' in i) or ('Android' in i) or ('ANDROID' in i) or ('安卓' in i):
        cnt4 += 1
    elif ('網頁' in i) or ('全端' in i) or ('web' in i) or ('Web' in i) or ('WEB' in i):
        cnt5 += 1
    elif ('遊戲' in i) or ('game' in i) or ('Game' in i) or ('GAME' in i) or ('電玩' in i):
        cnt6 += 1
    elif ('韌體' in i) or ('embed' in i) or ('Embed' in i) or ('EMBED' in i):
        cnt7 += 1
    elif ('資料' in i) or ('數據' in i) or ('探勘' in i) or ('DATA' in i) or ('Data' in i) or ('data' in i):
        cnt8 += 1
    else:
        cnt_other += 1
        # print(i)
    cnt += 1
print("總筆數=", cnt, "其他=", cnt_other)


dict = {"前端工程師": cnt1, "後端工程師": cnt2, "AI工程師": cnt3, "APP工程師": cnt4, "網頁工程師": cnt5,
        "遊戲工程師": cnt6, "韌體工程師": cnt7, "資料工程師": cnt8}  # 篩選後放進字典
print(dict)

# 字典排序(value高到低)
words = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print(words)

name = []
num = []
for i in range(len(words)):
    name.append(words[i][0])  # 取出字典的key放進list
    num.append(words[i][1])  # 取出字典value放進list

text_name = "總筆數="+str(cnt)+"\n其他="+str(cnt_other)
y = num
x = range(len(dict))

plt.bar(x, y, 0.35)
plt.title('軟體工程師職缺分析')  # 表格名稱
plt.text(len(num)-1.5, num[1], text_name)
plt.ylabel('數量')  # y軸標題
plt.xticks(x, name)  # 設定x軸刻度
plt.show()  # 顯示繪製的圖形


# part2
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt_other = 0
for i in list_s:
    # print(i)
    if ('python' in i) or ('Python' in i) or ('PYTHON' in i):
        cnt1 += 1
    elif ('java' in i) or ('Java' in i) or ('JAVA' in i):
        cnt2 += 1
    elif ('c++' in i) or ('C++' in i):
        cnt3 += 1
    elif ('C#' in i) or ('c#' in i):
        cnt4 += 1
    elif ('php' in i) or ('Php' in i) or ('PHP' in i):
        cnt5 += 1
    else:
        cnt_other += 1
        # print(i)
    cnt += 1
print("總筆數=", cnt, "其他=", cnt_other)

dict = {"Python": cnt1, "Java": cnt2, "C++": cnt3, "C#": cnt4, "PHP": cnt5}
print(dict)

# 字典排序(value高到低)
words = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
print(words)

name = []
num = []
for i in range(len(words)):
    name.append(words[i][0])  # 取出字典的key放進list
    num.append(words[i][1])  # 取出字典value放進list

text_name = "總筆數="+str(cnt)+"\n其他="+str(cnt_other)
y = num
x = range(len(dict))

plt.bar(x, y, 0.35)
plt.title('軟體工程師程式語言分析')  # 表格名稱
plt.text(len(num)-1.5, num[0], text_name)
plt.ylabel('數量')  # y軸標題
plt.xticks(x, name)  # 設定x軸刻度
plt.show()  # 顯示繪製的圖形
