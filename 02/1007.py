n = int(input())
n1 = n//1000 % 10
n2 = n//100 % 10
n3 = n//10 % 10
n4 = n % 10
n_total = n1+n2+n3+n4
print(n_total)
