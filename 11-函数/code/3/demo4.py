# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:24
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

def wrapper():

    print('我在外层')
    num = 1

    def inner():

        nonlocal num
        num += 1

        print('我在内层')
        print('内层函数调用时：num =', num)
        print('内层函数结束')

    print('内层函数调用之前：num =', num)
    inner()
    print('内层函数调用之后：num =', num)

    print('外层函数结束')

wrapper()
