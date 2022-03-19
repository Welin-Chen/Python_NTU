i = 0
container = []
while(True):
    i += 1
    s = input()
    if(s == str(-1)):
        break
    container.append(s)
for j in range(len(container)):
    print(container[j].upper())
