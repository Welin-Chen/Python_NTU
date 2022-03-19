math = {"柯南", "灰原", "步美", "美環", "光彦"}
english = {"柯南", "灰原", "丸尾", "野口", "步美"}

list1 = sorted(math-english)
list2 = sorted(english-math)
list3 = sorted(english & math)

print(list1)
print(list2)
print(list3)
