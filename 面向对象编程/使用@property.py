# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, score):
        self._score = score

    #  可读
    @property
    def score(self):
        return self._score

    #  可写
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integar')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


stu = Student(99)
print(stu.score)
stu.score = 50
print(stu.score)


#  请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    def __init__(self, width=None, height=None):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def resolution(self):
        return 'width: %s, height: %s' % (self.__width, self.__height)

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value


scr = Screen()
scr.width = 50
scr.height = 100
print(scr.width)
print(scr.height)
print(scr.resolution)

scr2 = Screen(30, 100)
print(scr2.height)
print(scr2.width)