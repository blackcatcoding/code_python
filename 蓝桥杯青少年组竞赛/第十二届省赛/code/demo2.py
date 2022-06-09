# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 9:38
# @Author  : 黑猫
# 公众号   : 黑猫编程
# 网址     : ac.blackcat1995.com

n = int(input())

s = 0
for i in range(1, n + 1):
    if i & 1:
        s += i

print(s)