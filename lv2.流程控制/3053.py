n = int(input())
for i in range(n):
    flag = 0
    for j in range(n):
        if(j < n-1-i):
            print(' ', end='')
        else:
            if(flag == 0):
                print("*", end='')
                flag = 1
            else:
                print(" *", end='')
    print()
