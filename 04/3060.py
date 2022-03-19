n = int(input())
sum = 0
cnt = 0
maxval = 0
maxpos = 0
minval = 1e5
minpos = 0
while n != -1:
    sum += n
    cnt += 1
    avg = sum/cnt
    if(n > maxval):
        maxval = n
        maxpos = cnt
    if(n < minval):
        minval = n
        minpos = cnt
    n = int(input())
print(sum)
print(avg)
print(maxval)
print(maxpos)
print(minval)
print(minpos)
