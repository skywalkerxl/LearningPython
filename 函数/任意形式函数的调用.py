# -*- coding:utf-8 -*-
'''
 对于任意函数我们都可以通过func(*args, **kw)的形式调用它
 *args是可变参数，接收的是一个元组tuple
 **kw是关键字参数，接收的是一个字典dict
'''


def func(*args, **kw):
    print('args:', args, 'kw:', kw)


print(func(1, 2, 3, loc='Beijing'))
print(func(*(1, 2, 3),**{'a': 1, 'b': 2}))
