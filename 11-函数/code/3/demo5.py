# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:30
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

def average():

    li = []

    def inner(value):

        li.append(value)

        return sum(li) / len(li)

    return inner

avg = average()
print(avg(6000))
print(avg(7000))
print(avg(8000))

