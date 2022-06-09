# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/23 22:38
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def square(x):

    return x ** 2

print(map(square, [1, 2, 3, 4, 5]))
print(list(map(square, [1, 2, 3, 4, 5])))

print(list(map(lambda x : x ** 3, [1, 2, 3, 4, 5])))
print(list(map(lambda m, n : m + n, [1, 2, 3, 4, 5], [1, 1, 1, 1, 1])))