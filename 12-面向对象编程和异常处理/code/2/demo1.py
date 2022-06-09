# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 16:50
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class Person(object):

    def __init__(self, name, gender, skill):

        self.name = name
        self.gender = gender
        self.skill = skill

p1 = Person('张三', '男', '游泳')
print(p1.__dict__)
print(p1.__dict__['name'])
print(p1.name)

p1.country = '中国'
print(p1.__dict__)

del p1.skill
print(p1.__dict__)