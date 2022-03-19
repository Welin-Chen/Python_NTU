n1 = float(input())
n2 = float(input())
o = input()
if(o == "+"):
    print("%.2f + %.2f = %.2f" % (n1, n2, n1+n2))
elif(o == "-"):
    print("%.2f - %.2f = %.2f" % (n1, n2, n1-n2))
elif(o == "*"):
    print("%.2f * %.2f = %.2f" % (n1, n2, n1*n2))
elif(o == "/"):
    print("%.2f / %.2f = %.2f" % (n1, n2, n1/n2))
