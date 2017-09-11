# -*- coding:utf-8 -*-

# 首先编写一个计算x2的函数
def power(x):
    return x*x;

print(power(3));

# 再编写一个计算X的n次方的函数
def powerN(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(powerN(5, 3))

# 设置默认参数
def powerDefault(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print (powerDefault(3))
print (powerDefault(2, 4))
"""
  在这里，默认函数的作用就派上了用场，当只有一个参数时，仍然可以正常使用，而不会报错
  设置默认参数时，有几个需要注意的地方：
    1. 必选参数在前，默认参数在后面，否则Python的解释器会报错
"""

# 使用默认参数的最大的好处就是能够降低调用函数的难度

# 在这里我们可以把 年龄和城市信息设为默认参数
def enroll(name, gender, age = 5, city='Beijing'):
    print ('name' , name)
    print ('gender', gender)
    print ('age', age)
    print ('city', city)

print ( enroll('Bob', 'M') );

# 但是默认参数有个容易出错的地方
# 例如我们先定义一个函数，传入一个list,添加一个END再返回
def add_end( L = [] ):
    L.append('END')
    return L

# 我们使用这个函数来测试
print(add_end([1, 2, 3]))
print(add_end()) # ['END']
print(add_end()) # ['END', 'END']

"""
  到这里我们不难发现，这里出现了一个问题，似乎L被 “记住了”
  Python函数在定义的时候，默认参数L的值就被计算出来了，即[],因为默认参数L也是一个变量，它指向[] 
  每次调用该函数，如果改变了L的内容，则下次调用时，L的内容就改变了，不再是函数定义时的L
"""
# 如果我们要是实现我们想要的效果
"""
  我们可以让L指向一个固定值，也就是不变的对象
"""
def add_end_v2( L = None ):
    if L is None :
        L = []
    L.append('END')
    return L


# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

# print( calc( [1, 2, 3] ) )
# print( calc( (1, 2, 3, 4) ) )
# print( calc( [1, 2, 3, 4, 5] ) )
print(calc(2, 3, 4))

# 关键字参数


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 我们传入多个参来实现关键字参数的功能
print(person('Lisa', '18', city='Beijing'))
print(person('LiMing', '19', city='WuHan', gender='M'))
'''
  命名关键字参数
'''


def person_v2(name, age, **kw):
    if 'city' in kw:  # 有city参数
        pass
    if 'job' in kw:  # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person_v2('Jack', '24', city='Beijing', addr='Chaoyang'))