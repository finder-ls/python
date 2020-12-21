i = 0
while i < 10:
    # 当 i == 7 时，不希望执行需要重复执行的代码
    if i == 7:
        # 在使用 continue 之前，同样应该修改计数器
        # 否则会出现死循环
        i += 1
        continue  # 循环遇到continue 就会跑到循环开始处进行循环，因此continue所在循环后边的代码不执行。
    # 重复执行的代码
    print(i)
    i += 1
