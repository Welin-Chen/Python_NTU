nn = input().split()
L = int(nn[0])
S = int(nn[1])

n = 0
while S != L:
    if(S < L):
        S += 5
    else:
        S -= 2
    n = n+1
else:
    print(n)
