# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:19
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def f():

    a = 1
    yield a

    b = 2
    yield b

    c = 3

    yield c

print(f())

g = f()

print(g.__next__())
print(g.__next__())
print(next(g))
# print(next(g))