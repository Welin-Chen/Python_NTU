import math
A = input().split()
ax = float(A[0])
ay = float(A[1])

B = input().split()
bx = float(B[0])
by = float(B[1])

C = input().split()
cx = float(C[0])
cy = float(C[1])

# s(bc)=a,s(ac)=b,s(ab)=c
a = math.sqrt((bx-cx)**2+(by-cy)**2)
b = math.sqrt((ax-cx)**2+(ay-cy)**2)
c = math.sqrt((ax-bx)**2+(ay-by)**2)

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('%.2f' % (area))
