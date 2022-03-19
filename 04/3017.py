n = int(input())
sum = 0
cnt = 0
maxval = 0
maxpos = 0
while n != -1:
    sum += n
    cnt += 1
    avg = sum/cnt
    if(n > maxval):
        maxval = n
        maxpos = cnt
    n = int(input())
print(sum)
print(avg)
print(maxval)
print(maxpos)
