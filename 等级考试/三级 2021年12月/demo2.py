# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 14:44
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

n = int(input())

for i in range(n):
    a = []
    for j in range(0, 4):
        x = int(input())
        a.append(x)
    print(sum(a) / 4)

