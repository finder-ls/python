# =====写脚本的时候 常利用find 返回状态-1
# 与index方法不同的是，查不到返回-1 不会报错，程序可继续执行。
s = "hello world"
print(s.find("d"))
print(s.find("m"))


# === index，查不到的时候会报错
s = "hello world"
print(s.index("d"))
print(s.index("m"))
