n = int(input())

nn = n//2+1
for i in range(nn):
    for j in range(nn):
        if(j >= (nn-i-1)):
            print("*", end='')
        else:
            print(" ", end='')
    for j in range(nn):
        if(j <= i-1):
            print("*", end='')
    print()

nnn = nn-1
for i in range(1, nn):
    for j in range(nn):
        if(j >= i):
            print("*", end='')
        else:
            print(" ", end='')
    for j in range(nn):
        if(j >= (nn-i-1)):
            pass
        else:
            print("*", end='')
    print()
