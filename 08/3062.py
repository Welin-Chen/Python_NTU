n = int(input())
list1 = []
for i in range(n, 0, -1):
    list1.append(i)
for i in list1:
    print("data", i)
print()
for i in range(len(list1)):
    print("data", list1.pop())
