# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 11:17
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

class People:

    # 静态属性 类属性
    # name = 'cat'
    # age = 10

    def set_attr(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        print(self.name, self.age)

cat1 = People()
# print(cat1.name, cat1.age)
cat1.set_attr('cat1', '10')
cat1.output()
cat2 = People()
cat2.set_attr('cat2', '12')
cat2.output()
# print(cat2.name, cat2.age)
# print(id(cat2.name))
# People.output()

# print(People.name, People.age)
# print(id(People.name))


