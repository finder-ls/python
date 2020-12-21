L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(next(g))
for n in g:
    print(n)
