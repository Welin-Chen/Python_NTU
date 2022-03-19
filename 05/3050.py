n = int(input())
cnt = 0
for i in range(n):
    m = i+1
    for j in range(m):
        cnt += 1
        print(cnt, '', end='')
    print()
