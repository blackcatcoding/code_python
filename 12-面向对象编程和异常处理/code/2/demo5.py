# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 17:11
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

# 多态：同一个对象的多种形态

class Bird:

    def fly(self):
        print('小鸟在天空飞翔')

class Plane:

    def fly(self):
        print('飞机在天空飞翔')


class Rocket:

    def fly(self):
        print('火箭在太空飞翔')

def fly(obj):

    obj.fly()

bird = Bird()
plane = Plane()
rocket = Rocket()

fly(bird)
fly(plane)
fly(rocket)