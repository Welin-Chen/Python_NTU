n = int(input())
for i in range(1, n+1):
    m = n-i
    for j in range(m):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()
