sumi = 1
sumf = 1
while True:
    n = input()
    if(n == "q"):
        break
    n = float(n)
    if(n % 1 == 0):
        sumi *= int(n)
    else:
        sumf *= n
print("%.2f" % (sumf))
print(sumi)
if(sumf > sumi):
    print("Float > Int")
elif(sumf == sumi):
    print("Float = Int")
else:
    print("Float < Int")
