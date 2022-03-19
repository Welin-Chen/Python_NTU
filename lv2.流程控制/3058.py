K = int(input())
L = int(input())
lst = []
R_score = 0
E_score = 0
while(True):
    s = input()
    if(s == 'q'):
        break
    lst.append(s)
    lst2 = lst[0].split(',')
    lst = []
    if(lst2[1] != "F"):
        if(lst2[2] == "R"):
            R_score += int(lst2[3])
        elif(lst2[2] == "E"):
            E_score += int(lst2[3])

if(R_score >= K and E_score >= L):
    print("yes")
else:
    print("no")
