# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:22
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

def wrapper():

    print('我在外层')

    def inner():

        print('我在内层')
        print('内层函数结束')

    inner()

    print('外层函数结束')

wrapper()