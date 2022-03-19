n = int(input())
n1 = int(n/12)
n2 = int(n % 12)
if n2 == 0:
    print(n1, 'dozen')
else:
    print(n1, 'dozen and', n2)
