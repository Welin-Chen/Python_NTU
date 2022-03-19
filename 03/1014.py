n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
    if(i != n):
        print(i, '+', end='', sep='')
    else:
        print(i, end='')
else:
    print(' =', sum)
