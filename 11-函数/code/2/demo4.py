# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 23:32
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

def f1(*args):

    return sum(args)

print(f1(1, 2))
print(f1(3, 4, 5, 6))

def f(**kwargs):

    print(kwargs)

f(a=1, b=2, name="xz")



