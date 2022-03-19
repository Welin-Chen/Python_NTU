s1 = input()
s2 = input()

pos = s1.find(s2)

while(pos != -1):
    print(pos)
    pos = s1.find(s2, pos+1)
