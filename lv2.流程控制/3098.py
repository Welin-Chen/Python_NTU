flag = 0
cnt = 0
while(True):
    s = input()
    if(s == "q"):
        break
    s = int(s)
    if(flag == 1 and s == 9):
        cnt += 1
    if(s == 1):
        flag = 1
    else:
        flag = 0
print(cnt)
