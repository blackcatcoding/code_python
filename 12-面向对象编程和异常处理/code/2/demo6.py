# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 17:15
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class Person:

    def __init__(self, name, gender, skill):

        self.__name = name
        self.__gender = gender
        self.__skill = skill

    def output(self):
        print(self.__name, self.__gender, self.__skill)

p1 = Person('小明', 'm', 10)
# print(p1.__name)
p1.output()
print(p1._Person__name, p1._Person__gender, p1._Person__skill)