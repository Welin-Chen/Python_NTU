def avg(lst):
    ans = 0
    ans = sum(lst)/(len(lst))
    return ans


lst = [[76, 73, 85],
       [88, 84, 76],
       [92, 82, 92],
       [82, 91, 85],
       [72, 74, 73]]

sum1 = []
avg1 = []
for i in range(len(lst)):
    print("student", i+1)
    for j in range(len(lst[i])):
        print(" %d: %d" % (j+1, lst[i][j]))
    sum1.append(sum(lst[i]))
    print(" sum: %d" % sum1[i])
    avg1.append(avg(lst[i]))
    print(" avg: %4.2f" % avg1[i])
print("total: %d, avg: %4.2f" % (sum(sum1), avg(avg1)))
print("highest avg: student %d: %4.2f" % (avg1.index(max(avg1))+1, max(avg1)))
