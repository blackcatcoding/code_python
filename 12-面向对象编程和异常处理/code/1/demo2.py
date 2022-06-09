# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 11:27
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class People:

    # 减少全局变量冲突
    count = 0
    # 创建对象时自动执行
    def __init__(self, name, age):
        print('>>>>')
        self.name = name
        self.age = age
        print('self =', id(self))

        People.count += 1

    def output(self):
        print(self.name, self.age)

cat1 = People('cat1', 16)
print(id(cat1))

cat2 = People('cat2', 18)
print(id(cat2))

print(People.count)
# print(People.name)