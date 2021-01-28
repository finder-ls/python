class Student(object):
    def __init__(self, name, score):
        '''增加一个特殊的函数__init__;并且方法(属性)前增加__变为私有方法(属性)'''
        self.__name = name
        self.__score = score

    def print_score(self):
        '''Student类中增加获取成绩的方法(函数)，供外部访问内部'''
        print('%s:%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__socre = score

    def set_scorelmt(self, score):
        '''定义一个有逻辑判断的方法(函数)，提供数据校验功能'''
        if 0 <= score >= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


# 通过Student类创建一个实例bart，并传入类要求的固定参数
bart = Student('liming', 60)
# 通过Student类创建多个实例
a, b, c, d = Student('a', 1), Student('b', 2), Student('c', 2), Student('d', 2)
# print(bart.__name)
# 调用bart实例中的获取名称的方法+参数，获取实例的名字
print(bart.get_name())
# 调用bart实例中的获取成绩的方法，获取该实例的成绩
# 只调用方法不传入参数，打印的是方法本身的东西。
# #结果比较费解，后边学了定制类后可改善。
# <bound method Student.get_score of
# <__main__.Student object at 0x00000189FF268790>>
print(bart.get_score)
# 调用实例bart的修改成绩的方法，并传入具体的成绩作为参数
# 试了试，不行，调用修改的方法待解决！！！
bart.set_score(90)
print(bart.get_score())
