n = input()
dic = {"1": "one", "2": "two", "3": "three", "4": "four",
       "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
dic2 = {"1": "ten", "2": "twenty", "3": "thirty", "4": "fourty",
        "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
dic3 = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
        "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}

if(int(n) >= 1 and int(n) <= 9999999):
    lst = list(n)
    num = len(lst)
    n = int(n)
    if(num == 7):
        print(dic[lst[0]], "million", end=' ')
        if(lst[1] != "0"):
            print(dic[lst[1]], "hundred", end=' ')
        if(lst[2] == "1"):
            print(dic3[lst[2]+lst[3]], end=' ')
        else:
            if(lst[2] != "0"):
                print(dic2[lst[2]], end=' ')
            if(lst[3] != "0"):
                print(dic[lst[3]], end=' ')
        if(lst[1] != "0" or lst[2] != "0" or lst[3] != "0"):
            print("thousand", end=' ')
        if(lst[4] != "0"):
            print(dic[lst[4]], "hundred", end=' ')
        if(lst[5] == "1"):
            print(dic3[lst[5]+lst[6]], end=' ')
        else:
            if(lst[5] != "0"):
                print(dic2[lst[5]], end=' ')
            if(lst[6] != "0"):
                print(dic[lst[6]], end=' ')
    if(num == 6):
        if(lst[0] != "0"):
            print(dic[lst[0]], "hundred", end=' ')
        if(lst[1] == "1"):
            print(dic3[lst[1]+lst[2]], end=' ')
        else:
            if(lst[1] != "0"):
                print(dic2[lst[1]], end=' ')
            if(lst[2] != "0"):
                print(dic[lst[2]], end=' ')
        if(lst[0] != "0" or lst[1] != "0" or lst[2] != "0"):
            print("thousand", end=' ')
        if(lst[3] != "0"):
            print(dic[lst[3]], "hundred", end=' ')
        if(lst[4] == "1"):
            print(dic3[lst[4]+lst[5]], end=' ')
        else:
            if(lst[4] != "0"):
                print(dic2[lst[4]], end=' ')
            if(lst[5] != "0"):
                print(dic[lst[5]], end=' ')
    if(num == 5):
        if(lst[0] == "1"):
            print(dic3[lst[0]+lst[1]], end=' ')
        else:
            if(lst[0] != "0"):
                print(dic2[lst[0]], end=' ')
            if(lst[1] != "0"):
                print(dic[lst[1]], end=' ')
        if(lst[0] != "0" or lst[1] != "0"):
            print("thousand", end=' ')
        if(lst[2] != "0"):
            print(dic[lst[2]], "hundred", end=' ')
        if(lst[3] == "1"):
            print(dic3[lst[3]+lst[4]], end=' ')
        else:
            if(lst[3] != "0"):
                print(dic2[lst[3]], end=' ')
            if(lst[4] != "0"):
                print(dic[lst[4]], end=' ')
    if(num == 4):
        if(lst[0] != "0"):
            print(dic[lst[0]], end=' ')
        if(lst[0] != "0"):
            print("thousand", end=' ')
        if(lst[1] != "0"):
            print(dic[lst[1]], "hundred", end=' ')
        if(lst[2] == "1"):
            print(dic3[lst[2]+lst[3]], end=' ')
        else:
            if(lst[2] != "0"):
                print(dic2[lst[2]], end=' ')
            if(lst[3] != "0"):
                print(dic[lst[3]], end=' ')
    if(num == 3):
        if(lst[0] != "0"):
            print(dic[lst[0]], "hundred", end=' ')
        if(lst[1] == "1"):
            print(dic3[lst[1]+lst[2]], end=' ')
        else:
            if(lst[1] != "0"):
                print(dic2[lst[1]], end=' ')
            if(lst[2] != "0"):
                print(dic[lst[2]], end=' ')
    if(num == 2):
        if(lst[0] == "1"):
            print(dic3[lst[0]+lst[1]], end=' ')
        else:
            if(lst[0] != "0"):
                print(dic2[lst[0]], end=' ')
            if(lst[1] != "0"):
                print(dic[lst[1]], end=' ')
    if(num == 1):
        if(lst[0] != "0"):
            print(dic[lst[0]], end=' ')
    if(n == 1):
        print("dollar", sep='')
    else:
        print("dollars", sep='')
else:
    print("out of range")
