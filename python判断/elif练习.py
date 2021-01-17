# 定义一个节日变量，判断节日变量执行不同的语句。
# 注意条例中需要用到逻辑运算等于，不是赋值符号。

holiday = '平安夜'

if holiday == '平安夜':
    print('今天是%s,我们去：' % (holiday))
    print('吃苹果')
    print('看电影')
elif holiday == '圣诞节':
    print('看电影')
    print('吃大餐')
elif holiday == '生日':
    print('买蛋糕')
