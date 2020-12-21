def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2020年")


f = now
f()
now()
print(now.__name__)
print(f.__name__)

# 增强now函数的功能，使调用他的时候自动打印调用日志，并且不该并now本身的函数
