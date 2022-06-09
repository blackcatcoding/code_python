# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 23:37
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

'''
n = n * (n - 1)!
5! = 5 * 4 * 3 * 2 * 1
4! = 4 * 3 * 2 * 1

0! = 1

'''

def fact(n):

    if n == 1:
        return 1

    return n * fact(n - 1)

print(fact(6))