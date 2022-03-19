num = int(input())
n = list(str(num))

for i in range(len(n)):
    n1 = int(n[i])
    if((n1 % 7 == 0 and n1 != 0) or num % 7 == 0):
        print('YES')
        break
else:
    print('NO')
