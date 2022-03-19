n = int(input())
lst = list(range(1, n+1))
for i in lst:
    print(i, end='')
lst2 = list(range(n-1, 0, -1))
for i in lst2:
    print(i, end='')
print()
