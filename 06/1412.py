from itertools import groupby
dic = {'A': 10, 'J': 18, 'S': 26,
       'B': 11, 'K': 19, 'T': 27,
       'C': 12, 'L': 20, 'U': 28,
       'D': 13, 'M': 21, 'V': 29,
       'E': 14, 'N': 22, 'W': 32,
       'F': 15, 'O': 35, 'X': 30,
       'G': 16, 'P': 23, 'Y': 31,
       'H': 17, 'Q': 24, 'Z': 33,
       'I': 34, 'R': 25}


def ID_Checker(n):
    # 因為有20分的輸入是小寫的，請自行在程式中修改成可以讀取小寫字母也能讓字典索引到。
    # 如果沒有改的話，輸入小寫會runtime error，只會拿到80分。
    if len(n) == 10:
        n = str(dic[n[0]]) + n[1:]
        LIST = []
        for i in range(0, len(n)):
            if i == 0:
                LIST.append(int(n[i]) * 1)
            elif i == 10:
                LIST.append(int(n[i]) * 1)

            else:
                LIST.append(int(n[i]) * (10-i))
        Total = sum(LIST)
        return Total
    else:
        return 1  # 身分證不足10碼回傳1


# s = "T112663836"
while(True):
    s = input()
    if(s == str(-1)):
        break
    if(ID_Checker(s.capitalize()) == 1):
        print("fake")
        continue

    list_s = list(s.capitalize())
    s_0 = list(str(dic[list_s[0]]))
    s_other = list_s[1:len(list_s)]
    new_list_s = s_0+s_other
    s_other.insert(0, s_0)
    # print(new_list_s, type(new_list_s[0]))

    cnt = 0
    for i in new_list_s:
        new_list_s[cnt] = int(i)
        cnt += 1
    # print(new_list_s)

    factor = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    # print(factor)

    for i in range(len(new_list_s)):
        new_list_s[i] *= factor[i]
    # print(new_list_s, sum(new_list_s), sum(new_list_s) % 10 == 0)
    if(sum(new_list_s) % 10 == 0):
        print("real")
    else:
        print("fake")
