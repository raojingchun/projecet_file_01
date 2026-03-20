# a = "ndsfdhfd"
# print(a.startswith("d"))
# def run():
#     for i in range(1, 3):
#         print(i)
#
#
# run()

# 优化代码格式：ctrl+alt+l

a = "ndsfdhfd"
print(a.startswith("d"))


# 面向对象
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def play(self):
        # return "{} 岁的 {} plays ball".format(self.age, self.name)
        # return f"{self.age} 岁的 {self.name} plays ball"
        return "%s 岁的 %s plays ball" % (self.age, self.name)


p = Person('lihua', 18, 'male')
print(p.play())

# 异常处理
num = 10
# if num % 2 != 1:
#     raise ValueError('余数不能为零')

try:
    assert num % 2 == 1, AssertionError('余数错误') # assert断言
    print(3)
except AssertionError as e:
    print(e)
