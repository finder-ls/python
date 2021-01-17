L = [x * x for x in range(10)] # 列表
g = (x * x for x in range(10)) # 元组
print(L)
print("--------")
print(g)
print("--------")
print(next(g))
print("--------")
for n in g:
    print(n)
