min = 1
max = 100
ans = int(input())

while True:
    print(min, '< ? <', max)
    n = int(input())
    if not min < n < max:
        print('out of range')
        continue
    if n > ans:
        max = n
        print('wrong answer, guess smaller')
    elif n < ans:
        min = n
        print('wrong answer, guess larger')
    else:
        print('bingo answer is', ans)
        break
