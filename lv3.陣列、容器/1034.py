lst = []
for i in range(5):
    lst.append(int(input()))
for i in lst:
    print(i, "\t", sep='', end='')
    for j in range(i):
        print("*", sep='', end='')
    print()
