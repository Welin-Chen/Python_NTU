nn = input().split()
n = int(nn[0])
x = int(nn[1])
y = int(nn[2])

T = 20
for i in range(1, n+1):
    if(i % 2 != 0):
        T += x
    else:
        T -= y
        if(T < 20):
            T = 20
Tmax = T

T = 20
for i in range(1, n+1):
    if(i % 2 == 0):
        T += x
    else:
        T -= y
        if(T < 20):
            T = 20
if(T > Tmax):
    Tmax = T

print(Tmax)
