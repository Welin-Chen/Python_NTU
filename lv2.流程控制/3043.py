s = input()
s = s.split()
t = 0
i_old = 0
for i in s:
    if(i == "A" or i == "B"):
        i = 0
    i = int(i)
    slope = i-i_old
    if(slope == 0):
        t += 5
    elif(slope > 0):
        t += (slope*10)
    elif(slope < 0):
        t += (-slope*6)
    i_old = i
print(t-5)
