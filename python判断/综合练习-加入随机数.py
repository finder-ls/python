# 在石头剪刀布的基础 上增加电脑随机数
# 在python中要使用随机数，就要导入随机数的模块
import random

p = input('请输入要出拳的数字-石头（1）／剪刀（2）／布（3）：')
c = int(random.randint(1, 3))
if p == c:
    print('平局')
elif ((p == '1' and c == '2') or
      (p == '2' and c == '3') or
      (p == '3' and c == '1')):
    print('电脑%s你赢了' % c)
else:
    print('电脑%s赢了' % c)
