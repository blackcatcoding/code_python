# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 17:00
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class Person:

    def __init__(self, name, gender, skill):

        self.name = name
        self.gender = gender
        self.skill = skill

class Policeman(Person):

    def __init__(self, name, gender, skill, country):
        super().__init__(name, gender, skill)
        self.country = country

    def output(self):
        print(self.name, self.gender, self.skill, self.country)


class Thief(Person):

    def __init__(self, name, gender, skill, country):
        # super().__init__(name, gender, skill)
        Person.__init__(self, name, gender, skill)
        self.country = country

    def output(self):
        print(self.name, self.gender, self.skill, self.country)

Jack = Policeman('Jack', 'm', '翻跟斗', '巨人国')
Jack.output()

Sam = Thief('Sam', 'm', '翻墙', '小人国')
Sam.output()