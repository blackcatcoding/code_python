# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 14:17
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

# 函数名的本质 地址

def f1():

    print('hello cat.')

print(f1)

f2 = f1
f3 = f2

f3()