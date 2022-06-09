# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 23:15
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : http://www.blackcat1995.com/

import math

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


n = int(input())

for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")