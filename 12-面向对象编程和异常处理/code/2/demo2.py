# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 16:55
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class Person(object):

    def __init__(self, name, gender, skill):

        self.name = name
        self.gender = gender
        self.skill = skill

class Policeman(Person):

    def job(self):
        print('%s的工作是抓小偷' % self.name)

class Thief(Person):

    def job(self):
        print('%s的工作是偷东西' % self.name)

Jack = Policeman('Jack', 'male', '翻跟斗')
print(Jack.__dict__)
Jack.job()

Sam = Thief('Sam', 'male', '开锁')
Sam.job()
