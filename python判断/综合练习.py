'''
从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
比较胜负
'''
'''
分析：需要使用input函数，从控制台对变量赋值，然后电脑将变量与固定值石头(1)进行比较

'''
putdate = input('请输入要出的拳的数字 —— 石头（1）／剪刀（2）／布（3）')
cpdate = '1'
if putdate == '1' and cpdate == '1':
    print('你出的石头%s,电脑出的石头%s,平局' % (putdate, cpdate))
elif putdate == '2' and cpdate == '1':
    print('你出的为剪刀%s,电脑出的石头%s，电脑赢了。' % (putdate, cpdate))
elif putdate == '3' and cpdate == '1':
    print('你出的为布%s,电脑出的石头%s，你赢了。' % (putdate, cpdate))
else:
    print('选择有误,请重新选择，你选择的为 %s，未知' % putdate)

# 分析，以上写法，当改变电脑为随机出的时候就会出现bug了。
# 优化后如下：
'''
1.两个变量相等时，是平局
2.当putdate赢：石头 剪刀；剪刀 布；步 石头
3.cpdate赢：除了前两种情况
'''
p = input('请输入要出拳的数字-石头（1）／剪刀（2）／布（3）：')
c = '1'
if p == c:
    print('平局')
elif ((p == '1' and c == '2') or
      (p == '2' and c == '3') or
      (p == '3' and c == '1')):
    print('电脑%s你赢了' % c)
else:
    print('电脑%s赢了' % c)
