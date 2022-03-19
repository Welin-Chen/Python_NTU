n = int(input())
if(n > 0 and n < 2000000000):
    while(True):
        ans = input()
        if(len(ans) > 0 and len(ans) < 100):
            if(int(ans) == n):
                print("Correct!")
                break
            else:
                print("Wrong Password!")
        else:
            print("sss")
            # print("Wrong Password!")
else:
    print("Wrong Password Setting!")
