l1 = int(input())
l2 = int(input())
l3 = int(input())
lst = [l1, l2, l3]
lst1 = sorted(lst, reverse=True)

if(((l1+l2) > l3) and ((l1+l3) > l2) and ((l2+l3) > l1)):
    print(True)
    if(lst1[0]**2 == (lst1[1]**2+lst1[2]**2)):
        print("Right Triangle")
    else:
        print("Non-Right Triangle")
else:
    print(False)
