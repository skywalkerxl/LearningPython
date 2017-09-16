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
            raise ValueError('score must bettween 0 ~ 100')
        self._score = value


stu = Student(99)
print(stu.score)
stu.score = 50
print(stu.score)