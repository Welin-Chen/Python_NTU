class student:  # 類別(Class)
    def __init__(self, na, se):  # 建構式(Constructor),self:實體物件的參考(s1,s2...)
        self.name = na  # 名字屬性(Attribute)
        self.gender = se  # 性別屬性
        self.grades = []  # 分數屬性

    def avg(self):  # 方法(Method),一定要有self
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
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Grades:", self.grades)
        print("Avg: %.1f" % self.avg())
        print("Fail Number:", self.fcount())
        print()


def top(*students):
    lst = [s1, s2, s3, s4, s5]  # 將物件(s1,s2...)放到串列中
    avgmax = 0
    cnt = 0
    avgmax_pos = 0
    for i in lst:
        i.show()
        if i.avg() > avgmax:
            avgmax = i.avg()
            avgmax_pos = cnt
        cnt += 1
    return lst[avgmax_pos]  # 回傳avg最高的物件


s1 = student("Tom", "M")  # 建立student類別的物件
s2 = student("Jane", "F")
s3 = student("John", "M")
s4 = student("Ann", "F")
s5 = student("Peter", "M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

top_student = top(s1, s2, s3, s4, s5)
print("Top Student:")
top_student.show()
