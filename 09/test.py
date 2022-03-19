class demo:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("hello", self.name)


d = demo("Tom")
print(type(demo))
print(type(d))
print("d.name:%s" % d.name)
d.hello()
