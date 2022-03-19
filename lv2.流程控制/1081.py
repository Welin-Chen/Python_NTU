n = int(input())
lst = list(range(1, n+1))
Tom = lst[0]
Jerry = lst[len(lst)-1]

while(True):
    Tom += 1
    if(Tom == Jerry):
        print("Tom")
        break
    Jerry -= 1
    if(Jerry == Tom):
        print("Jerry")
        break
