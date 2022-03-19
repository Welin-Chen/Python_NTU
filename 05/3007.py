n1 = int(input())
n2 = int(input())
n3 = int(input())

n = [n1, n2, n3]
max = n1
for i in range(len(n)):
    if(n[i] > max):
        max = n[i]
print(max)
