# a = 137
# a = list(str(a))
# b = "7" in a
# print("b", b)
s = input()
lst = s.split()
n0 = int(lst[0])
n1 = int(lst[1])
flag = 0
for i in range(n0, n1+1):
    if(i % 7 == 0):
        if(flag == 0):
            print(i, end='')
            flag = 1
        else:
            print(" &", i, end='')
print()
flag = 0
for i in range(n0, n1+1):
    a = "7" in list(str(i))
    if(a == True):
        if(flag == 0):
            print(i, end='')
            flag = 1
        else:
            print(" &", i, end='')
print()
