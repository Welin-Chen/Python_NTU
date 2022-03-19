h = float(input())
m = float(input())
BMI = m/(h/100)**2
print("%.2f" % BMI)
if(BMI < 18.5):
    print("Underweight")
elif(BMI < 24):
    print("Normal")
elif(BMI < 27):
    print("Overweight")
elif(BMI < 30):
    print("Obese Class I")
elif(BMI < 35):
    print("Obese Class II")
else:
    print("Obese Class III")
