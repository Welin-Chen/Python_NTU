role = int(input())
if(role == 1 or role == 2):
    score = int(input())
    if(score <= 100 and score >= 0):
        if(role == 1):
            if(score >= 60):
                print('pass')
            else:
                print('fail')
        elif(role == 2):
            if(score >= 70):
                print('pass')
            else:
                print('fail')
    else:
        print('score error')
else:
    print('role error')
