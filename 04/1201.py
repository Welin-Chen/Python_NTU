nn = input().split()
h = int(nn[0])  # 頭
f = int(nn[1])  # 腳
# 雞(c)有兩隻腳，兔子(r)有四隻腳
r = (f-2*h)/2
c = h-r
if(r % 1 == 0 and c % 1 == 0 and r >= 0 and c >= 0):
    print('YES')
    print(int(c), int(r))
else:
    print('NO')
