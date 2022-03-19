score = int(input())
if score >= 95:
    money = 2000
elif score >= 90:
    money = 1000
elif score >= 80:
    money = 500
else:
    money = 0

print('獎金',money,'元')