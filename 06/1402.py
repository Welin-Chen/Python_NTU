import re
# import numpy as np
n = []
n2 = []

# x = np.arange(9)
dict = {'A': 10, 'J': 18, 'S': 26,
        'B': 11, 'K': 19, 'T': 27,
        'C': 12, 'L': 20, 'U': 28,
        'D': 13, 'M': 21, 'V': 29,
        'E': 14, 'N': 22, 'W': 32,
        'F': 15, 'O': 35, 'X': 30,
        'G': 16, 'P': 23, 'Y': 31,
        'H': 17, 'Q': 24, 'Z': 33,
        'I': 34, 'R': 25}
s = input().capitalize()
li = re.findall(r'[0-9]+|[A-z]+', s)
a = dict.get(li[0])

length = len(str(a))
num = int(a)
for i in range(length):
    n.append(num//10**(length-i-1) % 10)

length = len(li[1])
num = int(li[1])
for i in range(length):
    n.append(num//10**(length-i-1) % 10)

n1 = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

for i in range(len(n)):
    n2.append(n1[i]*n[i])

if(sum(n2) % 10 == 0 and len(n) == 11):
    print("real")
else:
    print("fake")


# for i in range(length):
#     x[i] = num//10**(length-i-1) % 10
# print(x)
# print(x[8])
