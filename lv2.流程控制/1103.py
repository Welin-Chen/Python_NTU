n = input()
dic = {"0": '', "1": "壹", "2": "貳", "3": "參", "4": "肆",
       "5": "伍", "6": "陸", "7": "柒", "8": "捌", "9": "玖"}
if(int(n) >= 1 and int(n) <= 99999):
    lst = list(n)
    if(len(lst) == 1):
        print(dic[lst[0]], sep='', end='')
    elif(len(lst) == 2):
        print(dic[lst[0]], "拾", sep='', end='')
        if(lst[1] != "0"):
            print(dic[lst[1]], sep='', end='')
    elif(len(lst) == 3):
        print(dic[lst[0]], "佰", sep='', end='')
        if(lst[1] != "0"):
            print(dic[lst[1]], "拾", sep='', end='')
        if(lst[2] != "0"):
            print(dic[lst[2]],  sep='', end='')
    elif(len(lst) == 4):
        print(dic[lst[0]], "仟", sep='', end='')
        if(lst[1] != "0"):
            print(dic[lst[1]], "佰", sep='', end='')
        if(lst[2] != "0"):
            print(dic[lst[2]], "拾", sep='', end='')
        if(lst[3] != "0"):
            print(dic[lst[3]], sep='', end='')
    else:
        print(dic[lst[0]], "萬", sep='', end='')
        if(lst[1] != "0"):
            print(dic[lst[1]], "仟", sep='', end='')
        if(lst[2] != "0"):
            print(dic[lst[2]], "佰", sep='', end='')
        if(lst[3] != "0"):
            print(dic[lst[3]], "拾", sep='', end='')
        if(lst[3] != "0"):
            print(dic[lst[4]], sep='', end='')
    print("元整", sep='')
else:
    print("out of range")
