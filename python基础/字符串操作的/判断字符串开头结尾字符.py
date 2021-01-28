# 脚本中,判断字符串的开头结尾字符
# 与去字符结合使用
'''
startswith:判断开头
endswith:判断结尾
'''
# 判断某行是否是注释 # 开头的
# 如果开头有空格，需要先用 lstrip去掉空格
s = "#hello world=Ture"
print(s.startswith("#"))  # 是 返回True
print(s.endswith("!"))  # 否 返回 False
