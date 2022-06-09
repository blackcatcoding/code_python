# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 11:14
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

x, y, m = [int(i) for i in input().split(',')]

fibs = [0] * (m + 1)

fibs[1] = 1

for i in range(2, m + 1):
    if i == x or i == y:
        fibs[0] = 0
        continue

    fibs[i] = fibs[i - 1] + fibs[i - 2]

print(fibs[m])
