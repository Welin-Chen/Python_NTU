n1 = int(input())
n2 = int(input())
n3 = int(input())
n = [n1, n2, n3]
product = 1
for x in n:
    product *= x

print('sum is', sum(n))
print('average is', '%.2f' % (sum(n)/len(n)))
print('product is', product)
print('smallest is', min(n))
print('largest is', max(n))
# sum is 54
# average is 18.00
# product is 4914
# smallest is 13
# largest is 27
