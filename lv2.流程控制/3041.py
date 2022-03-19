s = input()
lst = s.split()
n = lst[0]
m = lst[1]
num = []
flag = 0
for i in range(int(n), int(m)):
    sum = 0
    for j in list(str(i)):
        sum += int(j)**len(str(i))
    if(sum == i):
        num.append(sum)
        if(flag == 0):
            print(i, end='')
            flag = 1
        else:
            print(' &', i, end='')
if(flag == 0):
    print("none")
