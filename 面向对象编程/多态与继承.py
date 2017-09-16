# -*-coding:utf-8 -*-

#  class Student


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_score(self):
        return self.__score


student = Student('Liming', '2333')
print(student.get_score())


# class Animal

class Animal(object):
    def __init__(self, name, shout):
        self.__name = name
        self.__shout = shout

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__shout

    def set_shout(self, shout):
        if 1 <= shout <= 100:
            self.__shout = shout

        else:
            raise ValueError('shout Error')


    def print_info(self):
        print('name: %s, shout: %s' % (self.__name, self.__shout))

    def run(self):
        print('Animal is running')

#  多态表示不同的对象可以执行相同的动作，但是要通过他们自己的代码来执行


class Dog(Animal):
    def run(self):
        print('Dog is running')
    pass


class Cat(Animal):
    def run(self):
        print('Cat is running')
    pass


dog = Dog('Husky', '100')

print(dog.get_name())
print(dog.print_info())
print(dog.run())
dog.set_shout(100)
