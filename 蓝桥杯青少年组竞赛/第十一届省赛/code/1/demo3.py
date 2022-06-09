# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 10:56
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

import math
def is_ws(x):

    s = 0

    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            s += i
            if i != x // i and i != 1:
                s += x // i

    return s == x and x != 1


n = int(input())

cnt = 0

for i in range(1, n):
    if is_ws(i):
        cnt += 1
        print(i)

print('*' + str(cnt))