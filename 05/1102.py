m = int(input())
n = int(input())

for i in range(1, m+1):
    for j in range(1, n+1):
        print(i, '*', j, '=', '%2i' % (i*j), end=' ', sep='')
    print('\n', end='')
