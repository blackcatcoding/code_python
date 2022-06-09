# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/24 23:11
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

def is_prime(x):

    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

for i in range(1, 1001):
    s = str(i)
    if '3' in s:
        if '33' in s:
            s = '&' + s
        if is_prime(i):
            s = s + '*'

        print(s)