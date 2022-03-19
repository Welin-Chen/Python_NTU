s = input()
lst = s.split(",")
sum_even = 0
sum_odd = 0

for i in lst:
    if(int(i) % 2 == 0):
        sum_even += int(i)
    else:
        sum_odd += int(i)
print(sum_odd)
print(sum_even)
print(sum_odd+sum_even)
