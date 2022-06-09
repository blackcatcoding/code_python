# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:19
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

def f1():

    print('我在f1中')


def f2():
    print('我在f2中')

def f3(f):

    f()

def f4(f):

    print('我是f4')

    return f

f3(f1)
f3(f2)

ret_func = f4(f2)
ret_func()
