class Person(object):
    '''
    定义一个Person类
    '''
    def __init__(self, name):
        self.name = name

    def say(self):
        print('说话')


class Student(Person):
    pass


try:
    s01 = Student() 
# 直接调用会报错，因为父类中要传入name参数，发现name参数不加引号也会报错。目前无法理解。
    s02 = Student(ls)
except(Exception):
    s03 = Student('ls')
    s03.say()
