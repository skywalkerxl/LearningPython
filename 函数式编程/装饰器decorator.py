# -*-coding:utf-8 -*-
#  本质上来说，decorator 就是一个返回函数的高阶函数,类似于javascript里面的闭包???
#  定义一个打印日志的generator


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


#  把 log 放在函数定义处，相当于执行了语句 log(now)
@log
def now():
    print('2017-09-14')

now()


#  三层嵌套的decorator
def log3(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log3('execute')
def now3():
    print('2015-02-15')

now3()
print(now3.__name__)

