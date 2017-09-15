# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

#  create a new object with init
bart = Student('Bart SimpleSon', '95')
#  add a name property
#  bart.name = 'Bart SimpleSon'
print(bart.name)


def print_score(std):
    print('%s:%s' % (std.name, std.score))

print(print_score(bart))
