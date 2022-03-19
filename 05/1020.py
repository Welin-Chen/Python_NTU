x = int(input())
cnt = 0
num = 0
for i in range(x):
    cnt += 1
    if(cnt % 4 == 0):
        cnt += 1
if((cnt+1) % 4 == 0):
    print(cnt+1)
else:
    print(cnt)
