n = int(input())
for i in range(n):
    m = n-i
    for k in range(i):
        print(' ', end='')
    for j in range(m):
        print('*', end='')
    print()
