class student:
    def __init__(self, na, se):
        self.name = na
        self.gender = se
        self.grades = []

    def avg(self):
        return sum(self.grades)/len(self.grades)

    def add(self, grade):
        self.grades.append(grade)

    def fcount(self):
        fct = 0
        for g in self.grades:
            if g < 60:
                fct += 1
        return fct

    def show(self):
        # print("Name:", self.name)
        # print("Gender:", self.gender)
        # print("Grades:", self.grades)
        # print("Avg:", self.avg())
        # print("Fail ct:", self.fcount())
        print(self.name)
        print("%.2f" % self.avg())
        print(self.fcount())


s1 = student(input(), input())
for i in range(1, 4):
    s1.add(int(input()))
s1.show()
