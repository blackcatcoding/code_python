# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 23:39
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

# 1 1 2 3 5 8 13 21

def fib(n):

    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(8))