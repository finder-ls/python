# 定义两个整数变量 en_score, ch_score 两门中有一门高于60分就是算输出考试通过

en_score = 59
ch_score = 60
if en_score >= 60 or ch_score >= 60:
    print('考试通过，您的成绩为 %d' % (en_score + ch_score))
else:
    print('考试未通过,请继续考试')
